<?php

$check = "GC-COIN_".(date("d")*999*888*16).".END";
$long_url =urlencode('https://gccoinfaucetpay.000webhostapp.com/key.html?key=$check');
$api_token = '5796fc13d2c90adacd58c3ba2dcce768cd3e43b5';
$api_url = "https://tokoda.top/api?api={$api_token}&url={$long_url}";

$result = @json_decode(file_get_contents($api_url),TRUE);

if($result["status"] == 'error') {
echo $result["message"][0];
}else{
$linkkey=$result["shortenedUrl"];
}
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
echo "Link lấy key => $linkkey\n";
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
