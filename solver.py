import tls_client, re, json, asyncio, inspect
import hashlib

from time import time
from groq import Groq
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor

from logger import logger
from main import hsw
from motion import motion_data

session = tls_client.Session(client_identifier="chrome_120", random_tls_extension_order=True)

api_js = session.get('https://hcaptcha.com/1/api.js?render=explicit&onload=hcaptchaOnLoad').text
version = re.findall(r'v1\/([A-Za-z0-9]+)\/static', api_js)[1]

loop = asyncio.get_event_loop()
asyncio.set_event_loop(loop)

client = Groq(api_key="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") # ohh nooo i leaked my key (its free anyways)

session.headers = {
    'accept': '*/*',
    'accept-language': 'de,de-DE;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'cache-control': 'no-cache',
    'pragma': 'no-cache',
    'referer': 'https://discord.com/',
    'sec-ch-ua': '"Microsoft Edge";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'script',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0',
}

class hcaptcha:
    def __init__(self, sitekey: str, host: str, proxy: str = None, rqdata: str = None) -> None:
        logger.info(f"Solving for: {sitekey} - {host}")
        self.sitekey = sitekey
        self.host = host.split("//")[-1].split("/")[0]

        self.rqdata = rqdata
        self.motion = motion_data(session.headers["user-agent"], f"https://{host}")

        self.motiondata = self.motion.get_captcha()
        self.siteconfig = self.get_siteconfig()

        self.captcha1 = self.get_captcha1()
        self.captcha2 = self.get_captcha2()

        self.answers = {}


    def get_siteconfig(self) -> dict:
        s = time()
        siteconfig = session.post(f"https://api2.hcaptcha.com/checksiteconfig", params={
            'v': version,
            'sitekey': self.sitekey,
            'host': self.host,
            'sc': '1', 
            'swa': '1', 
            'spst': '1'
        })
        return siteconfig.json()


    def get_captcha1(self) -> dict:
        s = time()
        data = {
            'v': version,
            'sitekey': self.sitekey,
            'host': self.host,
            'hl': 'de',
            'motionData': json.dumps(self.motiondata),
            'pdc':  {"s": round(datetime.now().timestamp() * 1000), "n":0, "p":0, "gcs":10},
            'n': loop.run_until_complete(hsw(self.siteconfig['c']['req'], self.host, self.sitekey)),
            'c': json.dumps(self.siteconfig['c']),
            'pst': False
        }

        if self.rqdata is not None: data['rqdata'] = self.rqdata

        getcaptcha = session.post(f"https://api.hcaptcha.com/getcaptcha/{self.sitekey}", data=data)
        return getcaptcha.json()
    
    def get_captcha2(self) -> dict:
        s = time()
        data = {
            'v': version,
            'sitekey': self.sitekey,
            'host': self.host,
            'hl': 'de',
            'a11y_tfe': 'true',
            'action': 'challenge-refresh',
            'old_ekey'  : self.captcha1['key'],
            'extraData': self.captcha1,
            'motionData': json.dumps(self.motiondata),
            'pdc':  {"s": round(datetime.now().timestamp() * 1000), "n":0, "p":0, "gcs":10},
            'n': loop.run_until_complete(hsw(self.captcha1['c']['req'], self.host, self.sitekey)),
            'c': json.dumps(self.captcha1['c']),
            'pst': False
        }
        if self.rqdata is not None: data['rqdata'] = self.rqdata

        getcaptcha2 = session.post(f"https://api.hcaptcha.com/getcaptcha/{self.sitekey}", data=data)
        return getcaptcha2.json()

    def text(self, task: dict) -> str:
        s, q = time(), task["datapoint_text"]["de"]    
        hashed_q = hashlib.sha1(q.encode()).hexdigest() 
        response = client.chat.completions.create(
            messages=[
                {"role": "user", 
                 "content": f"Srictly respond to the following question with only and only one single word, number, or phrase. Make sure its lowercase:  Question: {q} Response options: ja, nein"}
                 ],
                 model="llama3-8b-8192",
                 temperature=0.95,
                 max_tokens=128,
        )
    
        
        if response:
            response = response.choices[0].message.content
            self.answers[hashed_q] = response
            return task['task_key'], {'text': response}
        
        return "ja"

    def solve(self) -> str:
        s = time()
        try:
            cap = self.captcha2
            with ThreadPoolExecutor() as e: 
                results = list(e.map(self.text, cap['tasklist']))
            answers = {key: value for key, value in results}
            submit = session.post(
                f"https://api.hcaptcha.com/checkcaptcha/{self.sitekey}/{cap['key']}",
                json={
                    'answers': answers,
                    'c': json.dumps(cap['c']),
                    'job_mode': cap['request_type'],
                    'motionData': json.dumps(self.motion.check_captcha()),
                    'n': loop.run_until_complete(hsw(cap['c']['req'], self.host, self.sitekey)),
                    'serverdomain': self.host,
                    'sitekey': self.sitekey,
                    'v': version,
                })
            if 'UUID' in submit.text:
                logger.info(f"Solved hCaptcha {submit.json()['generated_pass_UUID'][:150]}..")
                return submit.json()['generated_pass_UUID']
            
            logger.critical(f"Failed To Solve hCaptcha")
            return None
        except Exception as e:
            line = inspect.currentframe().f_back.f_lineno
            logger.critical(f"Error at line {line}: {e}")

if __name__ == "__main__":
    rqdata = "Fw/JtA+U387VY6aPF7obxrL8yvKOWxu3KEUAIbRG4l+o98ypDBhBAtkbL1F5L+q0V8AKi0T8/4Z2BzcnpVlg+AsnDVcxKo+B9BnKsuhQJxNqJQop1ecdL2mivZVttgesKg36eiMCmPQxSOpXiJit/E4o/QiZBR2hlcIpdnPotwnANkU6Sl0yfjvQZa7eclM5kjmRbiFvXbxkhcruE53fQ8x7"
    solver = hcaptcha("a9b5fb07-92ff-493f-86fe-352a2803b3df", "discord.com", "http://127.0.0.1:9080", rqdata)
    token = solver.solve()
