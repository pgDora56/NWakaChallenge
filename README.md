NWakaChallenge
====
Nわか(NWaka-1415)のbotを作ろうというエスワン(eS-1)の閃きから生まれた、K3史上最高にアホらしい開発プロジェクト D-side

## Description
とりあえず大前提としてこれはお遊びです。

そもそもこのプロジェクトは「#にわかの金で○○○」という煽りハッシュタグの発展として生まれました。（にわかの金で焼肉、にわかの金で寿司、にわかの金で人生を豊かにetc...）


こんだけあればbotに出来るんじゃない？の成れの果てです。K3の方はSlackに「にわかチャレンジ」チャンネルがありますので興味があれば是非どうぞ。

## Usage
まず、[Twiiter Apps](https://apps.twitter.com/)から各種トークンを取得する必要があります。

* Consumer Key
* Consumer Secret
* Access Token
* Access Token Secret

こいつらを取得してください。

そうしたら、ここに出ているファイル群と同じフォルダにconfig.pyを作り、

```python:config.py
CONSUMER_KEY = # Consumer Keyを書く
CONSUMER_SECRET = # Consumer Secretを書く  
ACCESS_TOKEN =  # Access Tokenを書く
ACCESS_TOKEN_SECRET =  # Access Token Secretを書く
```

と、API情報を記載し、実行するのみです。

## License
MIT License