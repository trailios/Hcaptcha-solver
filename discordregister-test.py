import requests, random, string
from solver import hcaptcha

def getCookies() -> list:
    headers = {
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.9',
        'Connection': 'keep-alive',
        'Referer': 'https://discord.com/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-GPC': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
        'X-Track': "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzExMy4wLjAuMCBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTEzLjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjk5OTksImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9",
    }

    response = requests.get('https://discord.com/api/v9/experiments', headers=headers)
    return response.cookies, response.json().get("fingerprint")


cookies, fingerprint = getCookies()

headers = {
    'accept': '*/*',
    'accept-language': 'de,de-DE;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'cache-control': 'no-cache',
    'content-type': 'application/json',
    # 'cookie': '__dcfduid=7973e1d0ff9d11ee8f0557d4a8d03702; __sdcfduid=7973e1d1ff9d11ee8f0557d4a8d03702a400c8d8e7b28421f00a934e8ec67374ab9e56bd043af28e4b153e7c92055d55; __stripe_mid=6b923cb4-a96e-4e3d-95a2-9024adb3b1f527e3ec; OptanonConsent=isIABGlobal=false&datestamp=Tue+Nov+19+2024+22%3A04%3A35+GMT%2B0100+(Mitteleurop%C3%A4ische+Normalzeit)&version=6.33.0&hosts=&landingPath=https%3A%2F%2Fdiscord.com%2F&groups=C0001%3A1%2CC0002%3A0%2CC0003%3A0; __cfruid=5d1be3d6f951e6c9326e2fd870e68cdac5f433d6-1733767934; _cfuvid=FFXtEFi_6Bfp92dxNuv6DU_u4oMLCBhq7nena9R9l04-1733767934159-0.0.1.1-604800000; locale=en-US; cf_clearance=KJdp1SuvW_f1AFIjaxXS4Qt9hOGjJjnY.0Oo52GC2ew-1733767935-1.2.1.1-MYPr9OYDQFBgtuzMPMG_fbpRZtFseP7pEDgJfuYH31Hw6kZhAQ5lt_Db3OLCiaPLNigrqgOj4bDQuUtN1d_JBH418jorrLZJOz5cSkueusk5mVTWNDVEv8FDV9FLlEMguNtB.XMgOSANmsvHEEvALYmdqTEWvi7MtDGCHPY02wgc4zR23A03yl0PosUSnpta6EhTEZ29vwTOTVqlFbtNoAEcK_o_4TiHKo_TYicdIBNIpJMIeD6Vu4SDqvtjaXldJyUVqakaI1.YG13MR2L7zPYkdKy.7BkmDvx1mgmDqRtAuBMNcF9D1H6h4EYFzAPmseA3EtXcFqMGBbxc49yCPlDGZbc.B3ePR2VgkoUkrnp3DqFkFRzn3GTT0_zG70HkvDSjrE8eRkJhAn1CaKHTMw',
    'origin': 'https://discord.com',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://discord.com/register?redirect_to=%2Fchannels%2F%40me',
    'sec-ch-ua': '"Microsoft Edge";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0',
    #'x-captcha-key': 'P1_eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.hadwYXNza2V5xQgU6h6MTE46e3juYyt6eg3oWO_z7W5WttOYkTQm9-U57QW0acYQ0N99LyQpj7SceYyTuLV7h2Wo8tAUOBHw3JInhWfrjDF3I3JrrLa2mPwlPNPrFmnVkbC4dOVnSg0wRZYwOeTU5Ochccue6TTrQw9XriULqNAIEpOEc2bGjkDcoCdno4afKASCruYsuDD1xPlMHwdLmNcHTby_H4ZFvsZjQbc8hfP5V2X4J50ul9C1Q8wFMCJXFNTq4aLyVeedi2JnN3K1VNExm7fNlRTx1SybTDoJCyg-k-_bnSsDGSRgtrmas1aumO4iKqDfnAOqdavVSUwIRvWzTU4p8GWtGbxaZYVcgUYgmrHBR7aqaPNU79YstpQx1sKmGeTadxYAi66lreA8fYkMBNLbwKRDrhOlBUJ4hbt00TrsduDrsbPEXZD5v-ueclMDbWf2-tvtwWWQR-RvKz7tFTzK5vWGpDe5URQQy0Hkwqgyl8M4KiGAMnbaBsLf8bBY-z9y1hrwILMY3M6xC2VsBSnGLCqI5KmjPV2HPMHqPZNor__VXmkp99wxlPA21j8M25s3fu72jkzDgSe7hXA2VUfhsMDyEgpbGRGIKRd7JODnLOKhcLPKfAaMnt31Kr4b5YFXk6ARhNhknSj1TCPI3o5j1jXB89psJ9hbf-sliXST5bAxbCq3Pgjjdm21cU-0BBQnRMyFyQeWV8MFGCzT83Kan4HKdUKhdrZIodf1CdeZrNtebx7qpDQCBoaXJTSPWKCVfrnSUSDat3o2t66q3UPqwCoFkQ120YYoX6K7wZRZUA9bFaiVs1JgCozAAR4pZ6TDrWOQxOnBqm-p6ibTWbD2oCsXaXpGXRAZqcRj501sdZymxQRSxUnxaiUTPFefkCWHUkkooMKjXGsV1P57GZAAAUVvXGYeXDzRdAWVBXCpIGe4-jP0JPLQKUpKU8fqvfcyqOMgBc70xlUORYBD4VpXB4fTuhupFDvb4jItJJh3Ibe__o3WC3uSLVjqJeX_nXKaj5GYKVwK0Qu5o09aeZ3VRciVnzpitLtI_4KtZuW0PqLez3Sw-Q-xzUNPAW9ziHXq7zMmvTRwx1q2m1tTsRaBXck-8QNQgU5tBq1Ysv1XkuhxajCObnioFeQ9Bw2rgEkn7rs8Qhau-W2zOSa0zuDFm0KzoPIkpeaCPHltRFhDiiecRkHdlAikxuiCRKz2wBZ5SqXxCsRwIaolyvmZoc_xVCpzW4uI4r6Js5vXeY3se_c4jYpy2-70_8De-sVccJNuNx4DQs131Zvybox555K2zKP8Kw4m-b7lI-0YceLs0vKoG75radHneTtWOyb29DuZVFHgGQYqA2XRS4uPtNvAvX-PD4_y0v5NcPlZh3-UgVVHqVOpv0vxI6l-Mb0DnCDDxlqEbnm4iHlKYQQWSLLfRHBo7r-xABcTba-QhiBxwZYT9WkZEwxhr58FchkNn_mM9J62Gk0XIQCmCWGLebl05A-Jyj58EoF5p5xTBpELNdNQpvsHYIFEqd1bAAdsXPuWqWAfHR1V9nA7DAyAPoTfbc-0-JCBLnUx39M7PwSVChmTviNQaDXBood5s2aD9AkTjYXOv2gO-22DQdWR6eL6oEhR-NRz3EVQqJuZQQ2Y6AeuSr2ejU4RCKigDbK-3V0lqcMVZhYLiBqe90eeN2uW2co6zs2sXIatxgjLGXdBxcxSHzQ_R2Cq5hEUXPBiSqoHvAIYgXulkBkuFcKmXzF_UGF0UY90-wGVLSA9SJuXAEiW0vy1vx3vmeBYgs-E3-N0TUqpp3bARIs-nruWK3bDdKjVGXCW16oi5fqcV0oS7IHDcIOIE-PIF1Jf5occRweJjryyIt3jWpBuT7znFTwWnq5BKQV4Zm0f6YIu_Wl1AwLdZ5VUqNETaTxTPlbLuEBeYAPpdZXTTe6kdd7BfrCN4VafFtwl44fEfOKeftZV9oMNryVgd_rqgLQafl_O7Odss5xa-lRpZhU4CgZacei090misXPVUDxmZ7ECtxQJ1c2TyK_Usz-wS3fuU9o7QQQcPaRlSbeiNDCkUvOnykth6ZSNXzL1BRcTfcHBV8NdzjwdMHKo2Mxg5J18yhNeb6SIhqN74-8aa_70QezELGXjEkK6rh73X-vBAuDfKlpcnFqmO4jfWHLsBJWf_flWxaaVann6y8VAQ8wzr6INCwH7vpbRPrBShh_CI322V3HdWf-uvsiXdGT0m3BapWGfk_Y0GF_apuZgHCIWbpYA5G03FZT62UyxbPdDhmmoAJwVuCIFBHYVq87w3nDt02w3GpX3CiL3j0uBCJLt5klVuc0PkZMdknT1rUBNZfcx3o41pkSb-mVtoglrWjVRwbueCqScV_9BZTjAY1SwHG7gxOINnKnb6ksSeHvQMNopNuxrQnju4YFEGp5By0emGrTSoTYWA8PpDL63VAxfjhF0-Rizz1-_9nPgUH0AdmtDL6e5njSpksQhftoottlYTO3QGu3czo8ClreAmA_KoMRv59bxqm-tMoNQx_UHaAXCty5FlT9o0DqBRTpZ3DD2pDNbEVsZz_c_E7fqTgDnumntY5GHuI5E_Zr15FTZYSfZTCd09qWvMq4MLndEP83_B_g6ypFWPG2PnFC6Ijp8mhI5Tm65jK4f6CupwssKH3d2Ca_I8daTpZ24Cqt6-SXvoKYlvvaIKhRCO0tmKP0ny8IfReNdYKzDtXQW-gEGM9EMCUQTeLXjaR7f_ASapwXtmYt0-3Ce0Rpxx3yj_LENQKNleHDOZ2YbIqhzaGFyZF9pZM4UPIQfomtyqDMzNzJiODlionBkAA.0My4FBCHTTn6YK8s_FWo6mrFk9Sf-FMX0vOhvz3yTb4',
    #'x-captcha-rqtoken': 'Iit0WTdKSExnM2RjbWdndFFIQldMcC8wQmxBTUdic095Uk5BMGtuemx2SmlPSFo5c1pZMDRpSDdsd0RlaituUS9DaEdJTWc9PVpzVFlrcStGVTBKOGQ2STci.Z2Yabg.Y21XDfgcESpyQLepefoPZ8FmvHY',
    'x-debug-options': 'bugReporterEnabled',
    'x-discord-locale': 'en-US',
    'x-discord-timezone': 'Europe/Berlin',
    'x-fingerprint': f'{fingerprint}',
    'x-kl-ajax-request': 'Ajax_Request',
    'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImRlIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEzMS4wLjAuMCBTYWZhcmkvNTM3LjM2IEVkZy8xMzEuMC4wLjAiLCJicm93c2VyX3ZlcnNpb24iOiIxMzEuMC4wLjAiLCJvc192ZXJzaW9uIjoiMTAiLCJyZWZlcnJlciI6IiIsInJlZmVycmluZ19kb21haW4iOiIiLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6MzUxMjQ3LCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ==',
}


json_data = {
    'fingerprint': f'{fingerprint}',
    'email': 'opsurge.2.orsgss@gmail.com',
    'username': 'ztailsaosss',
    'global_name': 'trailiisgay',
    'password': '1122qqww**?',
    'invite': "zUevfhuh",
    'consent': True,
    'date_of_birth': '2002-11-05',
    'gift_code_sku_id': None,
}

proxies = {'http': 'http://127.0.0.1:9080', 'https': 'http://127.0.0.1:9080'}

def register():
    response = requests.post('https://discord.com/api/v9/auth/register', cookies=cookies, headers=headers, json=json_data, proxies=proxies)
    return response.json()

def hcap(captcha_data):
    solver = hcaptcha("a9b5fb07-92ff-493f-86fe-352a2803b3df", "discord.com", "http://127.0.0.1:9080", captcha_data)
    token = solver.solve()
    return token

def main():

    randommail = ''.join(random.choices(string.ascii_letters + string.digits, k=5))
    password = ''.join(random.choices(string.ascii_letters + string.digits, k=15))

    json_data["username"] = f"trail.hcap{randommail}"

    json_data["email"] = f"mak2idx{randommail}@gmail.com"
    json_data["password"] = password

    r = register()
    captcha_token = r["captcha_rqtoken"]
    captcha_data = r["captcha_rqdata"]

    token = hcap(captcha_data)

    if token:
        headers["x-captcha-key"] = token
        headers["x-captcha-rqtoken"] = captcha_token

        r = register()
        if "token" in r:
            print(f"Email: {json_data['email']}")
            print(f"Password: {password}")
            print(f"Token: {r['token']}")
        elif "captcha" in r:
            print(f"Failed to solve captcha: {r}")
        else:
            print(f"Error: {r}")
    else:
        print("Error: Failed to solve captcha")

main()
