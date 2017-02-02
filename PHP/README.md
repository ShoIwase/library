# PHPについての覚え書き場所

## 一般的なこと

### MySQLへの接続
```
//接続情報
$dbServer = 'IP Adress';
$dbName = 'DB Name';
$dsn = "mysql:host={$dbServer};dbname={$dbName};charset=utf8";
$dbUser = 'Username';
$dbPass = 'password';

//接続
$db = new PDO($dsn, $dbUser, $dbPass);
```

### 構文エラーの非表示
```
ini_set('display_errors', 0);
```

### SQL文の定義とクエリ実行，出力
```
$sql = 'SELECT * FROM table';
$result = $db->query($sql);

while($value = $result->fetch()){
$example = $value['example'];

echo $example;
}
```

### DB新規挿入・更新
新規挿入
```
$example = $_POST['example'];

$insert = 'INSERT INTO table (example) VALUES (:example)';

$stmt = $db->prepare($insert);
$stmt->bindParam(':example', $example);
$stmt->execute();
```

更新
```
$example = $_POST['example'];

$update = 'UPDATE table SET example = :example';

$prepare = $db->prepare($update);
$prepare->bindValue(':example',$example);
$prepare->execute();
```

## 細かいこと

### 日時
今日の日付を定義（Y年m月d日---H時i分s秒）  
タイムゾーン設定を忘れるとグリニッジ標準時(UTC)となる
```
date_default_timezone_set('Asia/Tokyo');
$date = date("Y-m-d");
```

今日のデータ取得SQL
```
$sql = 'SELECT * FROM table WHERE date = DATE(NOW())';
```

曜日の日本語表示（日=0から土=6）を利用する
```
$weekday = array( "日", "月", "火", "水", "木", "金", "土" );
print '（'.$weekday[date("w")].'）';
```

### 配列

新規配列の定義
```
$data = array();
```

変数(id)を配列に追加
```
$data[] = $id;
```

配列内の変数をカウント
```
$number = count($data);
```

配列内の全変数を出力
```
print_r($data);
```

配列内のn番目の変数を出力
```
echo $data[n];
```

### inputと$_POST
nameに変数を代入する方法と，valueの値を変数にするには以下を使用する。
```<input type = "number" name = "example'.$a.'" value="'.$example.'">```

$_POSTにて定義する際は「'」と「"」に気をつけて使用する。
```$_POST['example'.$n.'']```

### DB更新後の処理
DB更新後にリフレッシュされない場合はPHP内でJavaScriptを用いたリフレッシュを行う（暫定的な方法で原因は明らかではない）
```
echo <<<EOM <script type="text/javascript">location.href = "リフレッシュ先のURL";</script> EOM;
```

### 変数の一部を取得
dataのa番目からb桁をNewdataとして定義
```
$Newdata = substr($data,a,b);
```