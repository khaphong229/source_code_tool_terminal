<?php

$check = "KPN-PASS".(date("d")*999*888*16)."END";

if(file_exists('key.txt')==true){
$f=fopen("key.txt","r");
$key=trim(fgets($f));
if($key!=$check){
unlink('key.txt');
}else{
echo "Key đúng \n";
}
fclose($f);
}

if(file_exists('key.txt')!=true){
while (true){
echo "Link lấy key xxxxxxxxxxxx\n";
echo "Nhập key: ";
$key=trim(fgets(STDIN));

if($key==$check){
$a = fopen('key.txt','a+');
fwrite($a, $key);
sleep(1);
echo "Key đúng \n";
fclose($a);
break;
}else{
echo "Key sai\n";
sleep(1);
}

}
}
