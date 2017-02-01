<?php
//今日の日付を定義（Y年m月d日---H時i分s秒）
//タイムゾーン設定を忘れるとグリニッジ標準時(UTC)となる
date_default_timezone_set('Asia/Tokyo');
$date = date("Y-m-d");

//今日のデータ取得SQL
$sql = 'SELECT * FROM table WHERE date = DATE(NOW())';

//曜日の日本語表示（日=0から土=6）を利用する
//Ex.)（水）
$weekday = array( "日", "月", "火", "水", "木", "金", "土" );
print '（'.$weekday[date("w")].'）';
?>