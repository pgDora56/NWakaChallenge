import json, config, random
from requests_oauthlib import OAuth1Session

CK = config.CONSUMER_KEY
CS = config.CONSUMER_SECRET
AT = config.ACCESS_TOKEN
ATS = config.ACCESS_TOKEN_SECRET
twitter = OAuth1Session(CK, CS, AT, ATS) #認証処理

url = "https://api.twitter.com/1.1/statuses/update.json" #タイムライン取得エンドポイント

a="にわか"
b="金"
c="焼肉"
d="人生"
e="の"
f="で"
g="を"
h="が"
i="食べたい"
j="豊かに"
k="K3"
list1=[a,b,c,d,k]
list2=[e,f,g,h]
list3=[i,j]
list4=[]

for z in range(3):
    x=random.choice(list1)
    y=random.choice(list2)
    list4.append(x)
    list4.append(y)
list4.append(random.choice(list3))
Nwaka = "#にわかちゃれんじ\n"+list4[0]+list4[1]+list4[2]+list4[3]+list4[4]+list4[5]+list4[6]
print("{}".format(Nwaka))

params = {"status" : Nwaka}
res = twitter.post(url, params = params) #post送信

if res.status_code == 200: #正常投稿出来た場合
        print("Success.")
else:
        print("Failed : %d" % res.status_code)
