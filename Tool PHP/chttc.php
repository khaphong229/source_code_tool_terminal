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
function P($host,$tsm1,$data)
{
$mr = curl_init();
curl_setopt_array($mr, array(
CURLOPT_URL => $host,
CURLOPT_HEADER => true,
CURLOPT_RETURNTRANSFER => true,
CURLOPT_POSTFIELDS => $data,
CURLOPT_HTTPHEADER => $tsm1));
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


$api=readline("Nhập api ttc: ");


thanh();

$tc = p("https://tuongtaccheo.com/logintoken.php",$tsm=["user-agent:Mozilla/5.0 (Linux; Android 6.0.1; SM-G532G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.66 Mobile Safari/537.36"],$data="access_token=".$api."");

$ck_tds=explode('; path=/',explode('set-cookie: ',$tc)[1])[0];


$ten=explode('"',explode('"user":"',$tc)[1])[0];

if (explode('"',explode('{"status":"', $tc)[1])[0]=="success"){
	echo "\033[1;37mđăng nhập thành công <> $ten\n";
}else{exit('đăng nhập thất bại');}

thanh();

echo "1 <> Facebook
2 <> Tiktok
3 <> Youtube \n";
$chon=readline("Mời bạn chọn: ");
if($chon=="1"){
$view="facebook";
$chedo="facebook";
}else if($chon=="2"){
$view="tiktok";
$chedo="tiktok";
}else if($chon=="3"){
$view="youtube";
$chedo="youtube";
}else{
exit("nhập sai rồi");
}

thanh();

echo "File chứa acc cần thêm mỗi acc 1 dòng (vd: acc.txt)\n";
$file=readline("Nhập tên file: ");

thanh();
$api=readline("Nhập api anycaptcha: ");

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



$head=array("Host: api.anycaptcha.com","Content-Type: application/json",);


$tt=get("https://tuongtaccheo.com/cauhinh/".$view.".php",$tsm2);
	////print_r($tt);
$data_gui='{	"clientKey": "'.$api.'",	"task": {		"type": "RecaptchaV2TaskProxyless",		"websiteURL": "https://tuongtaccheo.com/cauhinh/'.$view.'.php",		"websiteKey": "6Lcp7hcUAAAAAJafojnrzQU-DliPkgIiNSGFnVej",		"isInvisible": false	}}';
$gui=cap("https://api.anycaptcha.com/createTask",$head,$data_gui);
$id=$gui['taskId'];

for($y=100;$y>-1;$y--){
	echo "Đang Giải Captcha $y     \r";
sleep(1);}

$data_giai='{	"clientKey": "'.$api.'",	"taskId": '.$id.'}';
$giai=cap("https://api.anycaptcha.com/getTaskResult",$head,$data_giai);

$tb=$giai['status'];
$capp=$giai['solution']['gRecaptchaResponse'];

if($tb=="ready"){echo "Giải Captcha Thành Công <> ";


$add=post("https://tuongtaccheo.com/cauhinh/nhapnick.php",$tsm2,"link=".$user."&loainick=".$chedo."&recaptcha=".$capp."");
#print_r($add);
if($add=="1"){
echo "Thêm thành công\n";
}else{
echo $add;
echo "\n";
}


}else{
echo "Giải captcha thất bại \n";
}

thanh();;

}
 
fclose($fp);

