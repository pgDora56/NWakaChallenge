import json, config, random
from words import *
from requests_oauthlib import OAuth1Session

CK = config.CONSUMER_KEY
CS = config.CONSUMER_SECRET
AT = config.ACCESS_TOKEN
ATS = config.ACCESS_TOKEN_SECRET
twitter = OAuth1Session(CK, CS, AT, ATS) #認証処理

url = "https://api.twitter.com/1.1/statuses/update.json" #タイムライン取得エンドポイント

part_lst = ["が食べたい","で豊かに","が欲しい","止まるんじゃねえぞ","は遅刻"] # 助詞＋末文
modi = ["美味しい","美しい", "可愛い", "金持ちの", "天使のような", "酷すぎる"] # 修飾語

yesno = ""
while not yesno in ["Y","n"]:
    yesno = ""
    nouns = [Nouns("にわか","person"),
            Nouns("にわな","person"),
            Nouns("にわかっぱ","person"),
            Nouns("金","other"),
            Nouns("焼肉","food"),
            Nouns("人生","other"),
            Nouns("K3","person"),
            Nouns("中央線","place"),
            Nouns("遅延","other"),
            Nouns("山","place"),
            Nouns("寿司","food")]

    noun_idx = random.randrange(0, len(nouns))
    noun_word = nouns.pop(noun_idx)
    part_word = noun_word.word_with_modifier(nouns, modi)

    Nwaka = "#にわかちゃれんじ\n" + part_word + random.choice(part_lst)

    print("{}".format(Nwaka))

    while not yesno in ["Y","n","c"]:
        yesno = input("Tweet OK? Y(es)/n(o)/c(ontinue):")

if yesno == "Y":
    params = {"status" : Nwaka}

    res = twitter.post(url, params = params) #post送信

    if res.status_code == 200: #正常投稿出来た場合
        print("Success.")
    else:
        print("Failed : %d" % res.status_code)
