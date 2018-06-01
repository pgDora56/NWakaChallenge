import json, config, random
from requests_oauthlib import OAuth1Session

CK = config.CONSUMER_KEY
CS = config.CONSUMER_SECRET
AT = config.ACCESS_TOKEN
ATS = config.ACCESS_TOKEN_SECRET
twitter = OAuth1Session(CK, CS, AT, ATS) #認証処理

url = "https://api.twitter.com/1.1/statuses/update.json" #タイムライン取得エンドポイント

noun = ["にわか","金","焼肉","人生","K3","中央線","遅延"] # 名詞
particle = ["の","で","を","が","に","へ","と","から","より","で","や"] # (格)助詞
lst = ["食べたい","豊かに","欲しい"] # 末文

tweet_content=[]
tweet_length = 10 # 初期値はハッシュタグ分
is_continue = True

# for z in range(3):
    # x=random.choice(noun)
    # y=random.choice(particle)
    # tweet_content.append(x)
    # tweet_content.append(y)

while is_continue:
    print(len(noun))
    noun_idx = random.randrange(0,len(noun)) # インデックスをランダムで決定
    noun_word = noun.pop(noun_idx) # 同じ名詞を使わないように
    part_word = random.choice(particle)

    tweet_content.append(noun_word)
    tweet_content.append(part_word)
    tweet_length += len(noun_word) + len(part_word)

    r = random.random()
    if r < tweet_length / 200 or len(noun) == 0:
        is_continue = False    

tweet_content.append(random.choice(lst))

Nwaka = "#にわかちゃれんじ\n"
for l in tweet_content:
    Nwaka += l
print("{}".format(Nwaka))
print(noun)

params = {"status" : Nwaka}

res = twitter.post(url, params = params) #post送信

if res.status_code == 200: #正常投稿出来た場合
    print("Success.")
else:
    print("Failed : %d" % res.status_code)
