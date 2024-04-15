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

$ua="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36";

$ck=readline('nhap cookie ');
#$ck="PHPSESSID=278dd6c3623fa7caaf87cf002d6948ef";
$nghi=readline('sau bao nhieu job thi nghi ');
$baolau=readline('nghi bao lau ');
system('clear');
$tsm = array(
"Host:mtxgames.info",
"user-agent:$ua",
"cookie:$ck",);
$tsm2 = array(
"giaycaonam4vietnam.com",
"user-agent:$ua",
);
$tsm1 = array(
"Host:mtxgames.info",
"90",
"application/x-www-form-urlencoded",
"user-agent:$ua",
"cookie:$ck",);

$tsm3 = array(
"Host:mtxgames.info",
"content-length: 72",
"application/x-www-form-urlencoded",
"user-agent:$ua",
"cookie:$ck",);

while(1){
	$a++;
$nv= get("https://mtxgames.info/play/51t7wrh0n4rkrco3",$tsm);

$substring="Không tìm thấy từ khóa, vui lòng thử lại sau";
if(strpos($nv, $substring)==true){exit("Không tìm thấy từ khóa, vui lòng thử lại sau \n");}

preg_match("#Tên:(.*?)</td>(.*?)<td>(.*?)</td>(.*?)tại:(.*?)<td>(.*?)-#is",$nv,$regex);
if(empty(trim($regex[3]))){exit(" cookie die \n");}
echo "\033[1;31mTk ".trim($regex[3])." • \033[1;32m".trim($regex[6])." Điểm • \033[1;33m$a Job\n";

$luot=explode(' lượt',explode('<strong>Từ khóa của bạn trong ngày hôm nay (bạn còn ',$nv)[1])[0];
if($luot=="1/200") {exit("Hẹn gặp lại \n");}
$e = explode("<td>",$nv);

echo "\033[1;34mWeb ".trim(explode("<ul",$e[2])[0])." • \033[1;35m$luot Lượt\n";
$id=explode('" />',explode('<input type="hidden" name="assignment_id" value="',$nv)[1])[0];
$token=explode('" />',explode('<input type="hidden" name="_token" value="',$nv)[1])[0];
$token_skip=explode('" />',explode('<input type="hidden" name="_token" value="',$nv)[2])[0];
$tukhoa=explode('</',explode('<span id="linkRef">',$nv)[1])[0];
echo "\033[1;36mTừ khoá $tukhoa \n";

if(trim(explode("<ul",$e[2])[0])==""){exit("Hẹn gặp lại \n");}

if(trim(explode("<ul",$e[2])[0])=="152"){
$url="ynv2uno6rkfy";}
if(trim(explode("<ul",$e[2])[0])=="Website: Minh Đức"){
$url="wirvddwca1op";}
if(trim(explode("<ul",$e[2])[0])=="Website: Hưng Phát"){
$url="brp05vlbqdns";}
if(trim(explode("<ul",$e[2])[0])=="526"){
$url="gitvfz5b69hw";}
if(trim(explode("<ul",$e[2])[0])=="182"){
$url="mpjglqkh21m8ere534534";}
if(trim(explode("<ul",$e[2])[0])=="vạn phát"){
$url="6zz6oacwema3";}
if(trim(explode("<ul",$e[2])[0])=="29"){
$url="mi22rp64jo0n";}
if(trim(explode("<ul",$e[2])[0])=="Tiến Minh"){
$url="gitvfz5b69hw";}
if(trim(explode("<ul",$e[2])[0])=="Tiến phát"){
$url="ubozic5r64xk";}
if(trim(explode("<ul",$e[2])[0])=="113"){
$url="dyovua8rkfz4";}
if(trim(explode("<ul",$e[2])[0])=="106"){
$url="t59pd0ss6joh";}
if(trim(explode("<ul",$e[2])[0])=="48"){
$url="uui74sqrnsgc";}
if(trim(explode("<ul",$e[2])[0])=="52"){
$url="rtmpunauqphk";}
if(trim(explode("<ul",$e[2])[0])=="15"){
$url="4e96vjjkw4e4";}
if(trim(explode("<ul",$e[2])[0])=="412"){
$url="dy2jz01a2okp345345";}
if(trim(explode("<ul",$e[2])[0])=="452"){
$url="whbhtyt9rh4y";}
if(trim(explode("<ul",$e[2])[0])=="62"){
$url="3xbzsgg5y4ft";}
if(trim(explode("<ul",$e[2])[0])=="Nhà phố"){
$url="y684if8iatnd";}
if(trim(explode("<ul",$e[2])[0])=="Kế toán"){
$url="w5gqrvc35tkd";}
if(trim(explode("<ul",$e[2])[0])=="118"){
$url="xg9jtq5rh446";}
if(trim(explode("<ul",$e[2])[0])=="thongboncaunghet.com"){
$url="w09xdwgyjpx4";}
if(trim(explode("<ul",$e[2])[0])=="Thịnh phát"){
$url="y53drdra6kcs";}
if(trim(explode("<ul",$e[2])[0])=="Website: Trí Bảo"){
$url="mpjglqkh21m8";}
if(trim(explode("<ul",$e[2])[0])=="kubet88-&gt;Tìmởtrang9"){
$url="6d7fvcswje17";}
if(trim(explode("<ul",$e[2])[0])=="trangchủfb88"){
$url="dmuk0uq0lebw";}
if(trim(explode("<ul",$e[2])[0])=="linkdangky88.com"){
$url="dmuk0uq0lebw";}
if(trim(explode("<ul",$e[2])[0])=="kubet379.net-&gt;Tìmởtrang2"){
$url="aup83dggt5vb";}
if(trim(explode("<ul",$e[2])[0])=="kucasino.pro-&gt;Tìmởtrang2"){
$url="2iays7z7ha1j";}
if(trim(explode("<ul",$e[2])[0])=="ku777.tv"){
$url="pl1yll410hly";}
if(trim(explode("<ul",$e[2])[0])=="fintechaz"){
$url="9pfah68acj0b";}
if(trim(explode("<ul",$e[2])[0])=="kubet88.us-&gt;Tìmởtrang8"){
$url="6d7fvcswje17";}
if(trim(explode("<ul",$e[2])[0])=="188kubet"){
$url="y8obaz4j4465";}
if(trim(explode("<ul",$e[2])[0])=="188kubet.com"){
$url="y8obaz4j4465";}
if(trim(explode("<ul",$e[2])[0])=="phuquybds.com"){
$url="jh0zkiny1evd";}
if(trim(explode("<ul",$e[2])[0])=="Website Bảo Phát"){
$url="mi22rp64jo0n";}
if(trim(explode("<ul",$e[2])[0])=="tcn quận 9"){
$url="1jjhrml784lw";}
if(trim(explode("<ul",$e[2])[0])=="trắc nghiệm"){
$url="2ratnskde1b5";}
if(trim(explode("<ul",$e[2])[0])=="Website: Quang Hồng"){
$url="yjujvr475e7y";}
if(trim(explode("<ul",$e[2])[0])=="Website: Mạnh Hùng"){
$url="tpuwrs6znawe";}
if(trim(explode("<ul",$e[2])[0])=="Website: Quốc Tuấn"){
$url="ltomjjcmi3cz";}
if(trim(explode("<ul",$e[2])[0])=="Website: Hưng Thịnh"){
$url="zdr4t2g8upb4";}
if(trim(explode("<ul",$e[2])[0])=="Website: Long Phát"){
$url="18ba4qrhjnmb";}
if(trim(explode("<ul",$e[2])[0])=="Website:Đại Nghĩa"){
$url="b5d4r0nq811a";}
if(trim(explode("<ul",$e[2])[0])=="Website: Thuận An"){
$url="geec9kssl7ci";}
if(trim(explode("<ul",$e[2])[0])=="Website: Quang Hồng"){
$url="b5d4r0nq811a";}
if(trim(explode("<ul",$e[2])[0])=="Website: Quốc Tuấn"){
$url="ltomjjcmi3cz";}
if(trim(explode("<ul",$e[2])[0])=="Website: Trí Phát"){
$url="vmfp2bz4qfyt";}
if(trim(explode("<ul",$e[2])[0])=="Website: Đức Bảo"){
$url="dy2jz01a2okp345345";}
if(trim(explode("<ul",$e[2])[0])=="Bùn vi sinh Hưng Phát"){
$url="brp05vlbqdns";}
if(trim(explode("<ul",$e[2])[0])=="Website: Quang Hồng"){
$skip=post("https://mtxgames.info/skip_code",$tsm3,"assignment_id=".$id."&_token=".$token_skip."");
#$url="b5d4r0nq811a";
}
if(trim(explode("<ul",$e[2])[0])=="Quận 9 Trí Phát"){
$url="1jjhrml784lw";}
if(trim(explode("<ul",$e[2])[0])=="Website: Long Phát"){
$url="9ky3r4yzetwo";}
if(trim(explode("<ul",$e[2])[0])==""){
$skip=post("https://mtxgames.info/skip_code",$tsm3,"assignment_id=".$id."&_token=".$token_skip."");
}
	
if(empty($url)){exit("Bye \n");}
	
$delay=rand(60,90);
for($i=$delay;$i>-1;$i--){$mau=rand(0,7);echo "\033[1;3".$mau."mĐợi $i giây      \r"; sleep(1);}
if(!empty($url)){
$check=g("https://giaycaonam4vietnam.com/getcode?key=".$url."",$tsm2);
$code=$check['code'];
if($check['status']=="true"){
echo "\033[1;31mCode $code \n";
}else{
$skip=post("https://mtxgames.info/skip_code",$tsm3,"assignment_id=".$id."&_token=".$token_skip."");
}
}else{$skip=post("https://mtxgames.info/skip_code",$tsm3,"assignment_id=".$id."&_token=".$token_skip."");
}



#for($i=10;$i>-1;$i--){$mau=rand(0,7);echo "\033[1;3".$mau."mĐợi $i giây để nhập code   \r"; sleep(1);}

//////////////////

$nhan=post("https://mtxgames.info/submit_code",$tsm1,"code=".$code."&assignment_id=".$id."&_token=".$token."");
###print_r($nhan);
echo "\033[1;30m--------------------------------------------- \n";


if($a%$nghi==0){for($i=$baolau;$i>-1;$i--){$mau=rand(0,7);echo "\033[1;3".$mau."mĐợi $i giây      \r"; sleep(1);}}
	
}


