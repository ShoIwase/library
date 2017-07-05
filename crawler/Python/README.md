# すくれいぴんぐについての覚え書き場所（Python編）

## 導入作業

### Python3.xのインストール
```
sudo apt-get install -y python3 python3.4-venv
```

### 仮想環境(venv)
仮想環境(Virtual Environment)を利用する。
```
python3 -m venv scraping
. scraping/bin/activate
```

### ライブラリの活用
```
pip install requests
sudo apt-get install -y libxml2-dev libxslt-dev libpython3-dev zlib1g-dev
pip install lxml
pip install cssselect
```

## 応用覚え書き

### title.py
ブログタイトルを最新から順に任意のページまで出力し続ける。  
box-ttl内のaリンクの文字のみを出力することで実現。

### refresh.py
ブログタイトルを監視し更新があったらツイートする。  
比較対象はtitle.txtである。  
更新がない場合は`true 日時`を返し，更新があった場合は`false`を返す。  
crontabでの監視が適切。
