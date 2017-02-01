<?php
//データベース接続設定
$dbServer = 'IP Adress';
$dbName = 'DB Name';
$dsn = "mysql:host={$dbServer};dbname={$dbName};charset=utf8";
$dbUser = 'Username';
$dbPass = 'password';
//データベースへの接続
$db = new PDO($dsn, $dbUser, $dbPass);
?>