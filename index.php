<?php

$filename = "test.txt";
if(!file_exists($filename)){
	die('文件不存在');
}

$pics = [];
$fs = fopen($filename, "r");
while(!feof($fs)){
	$line=trim(fgets($fs));
	if($line!=''){
		array_push($pics, $line);
	}
}

$pic = $pics[array_rand($pics)];

$type=$_GET['type'];
switch($type){

case 'json':
	header('Content-type:text/json');
	die(json_encode(['pic'=>$pic));

default:
	die(header("Location: $pic"));
}
