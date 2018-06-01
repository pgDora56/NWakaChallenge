import json, config, random
from words import *
from requests_oauthlib import OAuth1Session

CK = config.CONSUMER_KEY
CS = config.CONSUMER_SECRET
AT = config.ACCESS_TOKEN
ATS = config.ACCESS_TOKEN_SECRET
twitter = OAuth1Session(CK, CS, AT, ATS) #認証処理

url = "https://api.twitter.com/1.1/statuses/update.json" #タイムライン取得エンドポイント

noun = ["にわか","金","焼肉","人生","K3","中央線","遅延","山","回らない寿司"] # 名詞
particle = ["の","で","を","が","に","へ","と","、"] # (格)助詞
lst = ["食べたい","豊かに","欲しい","止まるんじゃねえぞ"] # 末文

nouns = [Nouns("にわか","person"),
        Nouns("金","other"),
        Nouns("焼肉","food"),
        Nouns("人生","other"),
        Nouns("K3","person"),
        Nouns("中央線","place"),
        Nouns("遅延","other"),
        Nouns("山","place"),
        Nouns("回らない寿司","food")]

tweet_content=[]
tweet_length = 10 # 初期値はハッシュタグ分
is_continue = True
nwaka_add = False
# for z in range(3):
    # x=random.choice(noun)
    # y=random.choice(particle)
    # tweet_content.append(x)
    # tweet_content.append(y)
"""
while is_continue:
    print(len(noun))
    noun_idx = random.randrange(0,len(noun)) # インデックスをランダムで決定
    noun_word = noun.pop(noun_idx) # 同じ名詞を使わないように
    part_word = random.choice(particle)

    tweet_content.append(noun_word)
    tweet_content.append(part_word)
    tweet_length += len(noun_word) + len(part_word)

    r = random.random()
    if r < (tweet_length / 200) or len(noun) == 0:
        is_continue = False

tweet_content.append(random.choice(lst))
"""

while is_continue:
    noun_idx = random.randrange(0, len(nouns))
    noun_word = nouns.pop(noun_idx)
    part_word = random.choice(noun_word.next_particle())

    tweet_content.append(noun_word.to_str())
    tweet_content.append(part_word)
    tweet_length += len(noun_word.to_str()) + len(part_word)
    if noun_word.to_str() == "にわか":
        nwaka_add = True
    if part_word == "が":
        tweet_content.append(random.choice(lst))
        break
    
    r = random.random()
    if r < (tweet_length / 100) and nwaka_add or len(nouns) == 0:
        is_continue = False


Nwaka = "#にわかちゃれんじ\n"
for l in tweet_content:
    Nwaka += l
print("{}".format(Nwaka))

yesno = ""
while not yesno in ["Y","n"]:
    yesno = input("OK? Y/n:")

if yesno == "Y":
    params = {"status" : Nwaka}

    res = twitter.post(url, params = params) #post送信

    if res.status_code == 200: #正常投稿出来た場合
        print("Success.")
    else:
        print("Failed : %d" % res.status_code)
