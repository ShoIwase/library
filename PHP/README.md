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