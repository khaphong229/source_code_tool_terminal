<?php
error_reporting(0);
include('datatube.php');

$do="\033[1;31m";
$xl="\033[1;32m";
$vang="\033[1;33m";
$xn="\033[1;34m";
$res="\033[1;35m";
$nau="\033[1;36m";
$trang="\033[1;97m";
$nenden = "\033[40m";
$nendo  = "\033[41m";
$nenxanhla = "\033[42m";
$nencam = "\033[43m";
$nenxanhduong = "\033[44m";
$nentim = "\033[45m";
$nenxanhduongnhat = "\033[46m";

function GET($host,$tsm)
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
  CURLOPT_CUSTOMREQUEST => "PUT",
  CURLOPT_POSTFIELDS => $data,
  CURLOPT_HTTPHEADER => $tsm1));
  $mr2 = curl_exec($mr); curl_close($mr);
  $json = json_decode($mr2,true);
  return $json;
}
function P($host,$tsm8,$data)
{
  $mr = curl_init();
  curl_setopt_array($mr, array(
  CURLOPT_URL => $host,
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_CUSTOMREQUEST => "POST",
  CURLOPT_POSTFIELDS => $data,
  CURLOPT_HTTPHEADER => $tsm8));
  $mr2 = curl_exec($mr); curl_close($mr);
  $json = json_decode($mr2,true);
  return $json;
}
home:
@system('clear');
if(file_exists('datatube.php')!=true){
	echo "
\033[1;36m   ██╗  ██╗██████╗ ███╗   ██╗
\033[1;35m   ██║ ██╔╝██╔══██╗████╗  ██║
\033[1;34m   █████╔╝ ██████╔╝██╔██╗ ██║
\033[1;33m   ██╔═██╗ ██╔═══╝ ██║╚██╗██║
\033[1;32m   ██║  ██╗██║     ██║ ╚████║
\033[1;31m   ╚═╝  ╚═╝╚═╝     ╚═╝  ╚═══╝

\n";
echo "\033[1;31m TOOL BẢN QUYỀN CỦA KPNTOOL 
\033[1;34m
\n";
	$tk=readline('Nhập token: ');
	$devicetk=readline('Nhập device token: ');
	$device=readline('Nhập device: ');
	$versioncode=readline('Nhập versioncode: ');
	$a = fopen('datatube.php','a+');
fwrite($a, "<?php
$");
fwrite($a, "tk= '$tk';
$");
fwrite($a, "devicetk= '$devicetk';
$");
fwrite($a, "device= '$device';
$");
fwrite($a, "versioncode = '$versioncode';
?>");
fclose($a);
}
$tsm8=array(
"Host:tuberocket.app:3000",
"token:$tk",
"versionCode:$versioncode",
"device:$device",
"deviceToken:$devicetk",);
	

system('clear');
///////

echo "
\033[1;36m   ██╗  ██╗██████╗ ███╗   ██╗
\033[1;35m   ██║ ██╔╝██╔══██╗████╗  ██║
\033[1;34m   █████╔╝ ██████╔╝██╔██╗ ██║
\033[1;33m   ██╔═██╗ ██╔═══╝ ██║╚██╗██║
\033[1;32m   ██║  ██╗██║     ██║ ╚████║
\033[1;31m   ╚═╝  ╚═╝╚═╝     ╚═╝  ╚═══╝

\n";
echo "\033[1;31m TOOL ĐƯỢC VIẾT BỞI KPNTOOL 

\n";

while(true){

ho:

$tc_sign=p("http://tuberocket.app:3000/api/signIn",$tsm8,"");

$token=$tc_sign['result']['token'];

#$token="441f9300590211ed942c6d0a3d87625e";

if(empty($token)){exit("Die token rồi vui lòng thay token mới\n");unlink('datatube.php');goto home;}
$tsm = array(
"Host:tuberocket.app:3000",
"token:$token",
);
$tsm1 = array(
"Host:tuberocket.app:3000",
"token:$token",
"Content-Length:71",
"Content-Type:application/json; charset=UTF-8",
);
	
$in=get("http://tuberocket.app:3000/api/member",$tsm);

$mail=$in['result']['email'];
$coin=$in['result']['coin'];
echo "\033[1;32mEmail: $mail \033[1;36m• $coin coins\n";
echo "\033[1;30m------------------------------------------------\n";
while(1){



$tc_b = get("http://tuberocket.app:3000/api/video",$tsm);

$id = $tc_b['result']['videoId'];

if(empty($id)){echo "Die token rồi vui lòng thay token mới\n";goto ho;}

$time = $tc_b['result']['playSecond'];

for($i = $time;$i>-1;$i--){
        $dom=rand(0,7);
        echo "\033[1;3".$dom."mĐợi [ $i ] giây    \r";
        sleep(1);
        }
        
//////
$a++;
$nhan = post("http://tuberocket.app:3000/api/video",$tsm1,'{"id":"'.$id.'","playCount":0,"playSecond":0,"boost":0,"status":""}');

$xu1 = $nhan['result']['coin'];

echo "\033[1;32m$a • \033[1;33mId video: $id \033[1;35m• Cập nhật có: $xu1 coins\n";


}

}




