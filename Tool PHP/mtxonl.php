<?php
system('clear');
error_reporting(0);
function GET($host,$tsm)
{
$mr = curl_init();
curl_setopt_array($mr, array(
CURLOPT_URL => $host,
CURLOPT_RETURNTRANSFER => true,
CURLOPT_HTTPHEADER => $tsm));
$mr2 = curl_exec($mr); curl_close($mr);
$json = json_decode($mr2,true);
return $mr2;
}
function G($host,$tsm)
{
$mr = curl_init();
curl_setopt_array($mr, array(
CURLOPT_URL => $host,
CURLOPT_RETURNTRANSFER => true,
CURLOPT_HTTPHEADER => $tsm));
$mr2 = curl_exec($mr); curl_close($mr);
$json = json_decode($mr2,true);
return $json;
}
function POST($host,$tsm1,$data)
{
$mr = curl_init();
curl_setopt_array($mr, array(
CURLOPT_URL => $host,
CURLOPT_RETURNTRANSFER => true,
CURLOPT_POSTFIELDS => $data,
CURLOPT_HTTPHEADER => $tsm1));
$mr2 = curl_exec($mr); curl_close($mr);
$json = json_decode($mr2,true);
return $mr2;
}

$ua="Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36";
$ck=readline('nhap cookie ');

$nghi=readline('sau bao nhieu job thi nghi ');
$baolau=readline('nghi bao lau ');
system('clear');
$tsm = array(
"Host:mtxgame.online",
"user-agent:$ua",
"cookie:$ck",);
$tsm2 = array(
"mtxgame.online",
"user-agent:$ua",
);
$tsm1 = array(
"Host:mtxgame.online",
"90",
"application/x-www-form-urlencoded",
"user-agent:$ua",
"cookie:$ck",);

$tsm3 = array(
"Host:mtxgame.online",
"content-length: 71",
"application/x-www-form-urlencoded",
"user-agent:$ua",
"cookie:$ck",);

while(1){
	$a++;
$nv= get("https://mtxgame.online/play/qrumruynkk4sm02g",$tsm);

$substring="Không tìm thấy từ khóa, vui lòng thử lại sau";
if(strpos($nv, $substring)==true){exit("Không tìm thấy từ khóa, vui lòng thử lại sau \n");}

preg_match("#Tên:(.*?)</td>(.*?)<td>(.*?)</td>(.*?)tại:(.*?)<td>(.*?)-#is",$nv,$regex);
if(empty(trim($regex[3]))){exit(" cookie die \n");}
echo "\033[1;31mTk ".trim($regex[3])." • \033[1;32m".trim($regex[6])." Điểm • \033[1;33m$a Job\n";

$luot=explode(' lượt',explode('<strong>Từ khóa của bạn trong ngày hôm nay (bạn còn ',$nv)[1])[0];
if($luot=="1/300") {exit("Hẹn gặp lại \n");}
$e = explode("<td>",$nv);

echo "\033[1;34mWeb ".trim(explode("<ul",$e[2])[0])." • \033[1;35m$luot Lượt\n";
$id=explode('" />',explode('<input type="hidden" name="assignment_id" value="',$nv)[1])[0];
$token=explode('" />',explode('<input type="hidden" name="_token" value="',$nv)[1])[0];
$token_skip=explode('" />',explode('<input type="hidden" name="_token" value="',$nv)[2])[0];
$tukhoa=explode('</',explode('<span id="linkRef">',$nv)[1])[0];
echo "\033[1;36mTừ khoá $tukhoa \n";

if(trim(explode("<ul",$e[2])[0])=="Website: Minh Đức"){
$url="wirvddwca1op";}
if(trim(explode("<ul",$e[2])[0])=="Website: Hưng Phát"){
$url="brp05vlbqdns";}
if(trim(explode("<ul",$e[2])[0])=="Website: Trí Bảo"){
$url="mpjglqkh21m8";}
if(trim(explode("<ul",$e[2])[0])=="Website Bảo Phát"){
$url="mi22rp64jo0n";}
if(trim(explode("<ul",$e[2])[0])=="Website: Đại Phát"){
$url="uui74sqrnsgc";}
if(trim(explode("<ul",$e[2])[0])=="Website: Hòa Phát"){
$url="v9i5kj09f32g";}
if(trim(explode("<ul",$e[2])[0])=="Website: Phát Đạt"){
$url="whbhtyt9rh4y";}
if(trim(explode("<ul",$e[2])[0])=="Website: Cường Phát"){
$url="xg9jtq5rh446";}
if(trim(explode("<ul",$e[2])[0])=="Website: Thịnh Phát"){
$url="z84hxssxviu3";}
if(trim(explode("<ul",$e[2])[0])=="Website: Đức Bảo"){
$url="dy2jz01a2okp";}
if(trim(explode("<ul",$e[2])[0])=="Website: Quang phát"){
$url="4e96vjjkw4e4";}
if(trim(explode("<ul",$e[2])[0])=="Website: Tiến Phát"){
$url="ubozic5r64xk";}
if(trim(explode("<ul",$e[2])[0])=="Website: Toàn Phát"){
$url="lw1k5uxzmqt2";}
if(trim(explode("<ul",$e[2])[0])=="Website: Vĩnh Phát"){
$url="3xbzsgg5y4ft";}
if(trim(explode("<ul",$e[2])[0])=="Website: Thịnh Đạt"){
$url="oykz4jpgr8ge";}
if(trim(explode("<ul",$e[2])[0])=="Website: Bảo Minh"){
$url="ynv2uno6rkfy";}
if(trim(explode("<ul",$e[2])[0])=="Website: Quang Minh"){
$url="apb2n8dj9ct8";}
if(trim(explode("<ul",$e[2])[0])=="Website: Tiến Minh"){
$url="gitvfz5b69hw";}
if(trim(explode("<ul",$e[2])[0])=="Website: Phát Đạt Chấm info"){
$url="whbhtyt9rh4y";}
if(trim(explode("<ul",$e[2])[0])=="Website: Bảo Phát"){
$url="mi22rp64jo0n";}
if(trim(explode("<ul",$e[2])[0])=="Website: Vạn Phát"){
$url="5e05faiygzdn";}
else{
$skip=post("https://mtxgame.online/skip_code",$tsm3,"assignment_id=".$id."&_token=".$token_skip."");
}
#if(trim(explode("<ul",$e[2])[0])=="xxx"){
#$url="xxx";}
#if(trim(explode("<ul",$e[2])[0])=="xxx"){
#$url="xxx";}
#if(trim(explode("<ul",$e[2])[0])=="xxx"){
#$url="xxx";}
#if(trim(explode("<ul",$e[2])[0])=="xxx"){
#$url="xxx";}

	
if(empty($url)){exit("Bye \n");}
	
$delay=rand(70,90);
for($i=$delay;$i>-1;$i--){$mau=rand(0,7);echo "\033[1;3".$mau."mĐợi $i giây      \r"; sleep(1);}
if(!empty($url)){
$check=g("https://mtxgame.online/getcode?key=".$url."",$tsm2);
$code=$check['code'];
}else{
exit("Bye \n");
#$skip=post("https://mtxgame.online/skip_code",$tsm3,"assignment_id=".$id."&_token=".$token_skip."");
}

echo "\033[1;31mCode $code \n";

#for($i=10;$i>-1;$i--){$mau=rand(0,7);echo "\033[1;3".$mau."mĐợi $i giây để nhập code   \r"; sleep(1);}

//////////////////

$nhan=post("https://mtxgame.online/submit_code",$tsm1,"code=".$code."&assignment_id=".$id."&_token=".$token."");
###print_r($nhan);
echo "\033[1;30m--------------------------------------------- \n";


if($a%$nghi==0){for($i=$baolau;$i>-1;$i--){$mau=rand(0,7);echo "\033[1;3".$mau."mĐợi $i giây      \r"; sleep(1);}}
	
}


