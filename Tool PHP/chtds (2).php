<?php
system('clear');
date_default_timezone_set('Asia/Ho_Chi_Minh');
error_reporting(0);
function GET($host,$tsm)
{
$mr = curl_init();
curl_setopt_array($mr, array(
CURLOPT_URL => $host,
CURLOPT_HEADER => true,
CURLOPT_RETURNTRANSFER => true,
CURLOPT_HTTPHEADER => $tsm));
$mr2 = curl_exec($mr); curl_close($mr);
$json = json_decode($mr2,true);
return $mr2;
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
return $json;
}
function CAP($host,$head,$data)
{
$mr = curl_init();
curl_setopt_array($mr, array(
CURLOPT_URL => $host,
CURLOPT_POSTFIELDS => $data,
CURLOPT_RETURNTRANSFER => true,
CURLOPT_HTTPHEADER => $head));
$mr2 = curl_exec($mr); curl_close($mr);
$json = json_decode($mr2,true);
return $json;
}
function thanh(){
	echo "-------------------------------------------------\n";
}
$tg=date('H:i:s');
/////uu=readline("\033[1;32mEnter Để Tiếp Tục");


thanh();

$ck_tds="cf_clearance=TdF2rht_c2mmeJ6IpGWSzY_JwADEvJUyi3YGFkjdsVI-1658045081-0-150; PHPSESSID=483ca6d91ee276c501fdcfaf4b35e092";


echo "1 <> Facebook
2 <> Tiktok
3 <> Instagram
4 <> Youtube \n";
$chon=readline("Mời bạn chọn: ");
if($chon=="1"){
$view="cauhinh";
$chedo="add_uid";
}else if($chon=="2"){
$view="chtiktok";
$chedo="tiktok_add";
}else if($chon=="3"){
$view="chinstagram";
$chedo="instagram_add";
}else if($chon=="4"){
$view="chyoutube";
$chedo="youtube_add";
}else{
exit("nhập sai rồi");
}

thanh();

echo "File chứa acc cần thêm mỗi acc 1 dòng (vd: acc.txt)\n";
$file=readline("Nhập tên file: ");

thanh();
#$api=readline("Nhập api anycaptcha: ");

system('clear');

$tsm2 = [
"cookie:$ck_tds",
"user-agent:Mozilla/5.0 (Linux; Android 6.0.1; SM-G532G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.66 Mobile Safari/537.36",
];
$h=0;

$fp = fopen($file, "r");
 
while(! feof($fp)) {
$h+=1;
$user=trim(fgets($fp));
echo "$h <> Đang thêm acc <> $user <> vào cấu hình \n";




$tt=get("https://traodoisub.com/view/".$view."/",$tsm2);

$giai=file_get_contents("http://fireender.tk/captcha_v2.php?site_key=6LeGw7IZAAAAAECJDwOUXcriH8HNN7_rkJRZYF8a&web=https://traodoisub.com/view/".$view."/&key=atmtooldz-vl");
print_r($giai);

for($y=100;$y>-1;$y--){
	echo "Đang Giải Captcha $y     \r";
sleep(1);}



$add=post("https://traodoisub.com/scr/".$chedo.".php",$tsm2,"idfb=".$user."&g-recaptcha-response=".$capp."");

if($add['success']=="1"){
echo "Thêm thành công\n";
}else{
echo $add['error'];
echo "\n";
}



thanh();;

}
 
fclose($fp);

