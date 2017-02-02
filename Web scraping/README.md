# すくれいぴんぐについての覚え書き場所

## curl xpath awkを用いたスクレイピング

### 準備
導入しランさせておく  
`sudo apt-get install libxml2-utils`  
`alias xpath="xmllint --html --xpath 2>/dev/null"`

### おおまかな手順
1.  `curl -0 URL > example`で対象URLをローカルに保存
1.  `xpath "xpathの内容"  example > Xexample`
1.  `gawk -f data.awk Xexample > awk_data`  

awk内は随時更新（正規表現を使用する）

## Rubyを用いたスクレイピング

### nokogiriの導入
nokogiriをそのまま導入しようとするとエラーが発生するため，以下の通り進める。
```
sudo add-apt-repository -y ppa:brightbox/ruby-ng
sudo apt-get update
sudo apt-get -y install ruby2.1 ruby2.1-dev zlib1g-dev
sudo gem install nokogiri
sudo gem install anemone

```