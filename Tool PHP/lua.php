<?php


$jobloi[1]=[];
$jobloi[2]=[];
$jobloi[3]=[];
$jobloi[4]=[];
$jobloi[5]=[];
$jobloi[6]=[];
$jobloi[7]=[];
$jobloi[8]=[];
$jobloi[9]=[];
$jobloi[10]=[];
$jobloi[11]=[];
$jobloi[12]=[];
$jobloi[13]=[];
$jobloi[14]=[];
$jobloi[15]=[];
$jobloi[16]=[];
$jobloi[17]=[];
$jobloi[18]=[];
$jobloi[19]=[];
$jobloi[20]=[];
$jobloi[21]=[];
$jobloi[22]=[];
$jobloi[23]=[];
$jobloi[24]=[];
$jobloi[25]=[];
$jobloi[26]=[];
$jobloi[27]=[];
$jobloi[28]=[];
$jobloi[29]=[];
$jobloi[30]=[];
$jobloi[31]=[];
$jobloi[32]=[];
$jobloi[33]=[];
$jobloi[34]=[];
$jobloi[35]=[];
$jobloi[36]=[];
$jobloi[37]=[];
$jobloi[38]=[];
$jobloi[39]=[];
$jobloi[40]=[];
$jobloi[41]=[];
$jobloi[42]=[];
$jobloi[43]=[];
$jobloi[44]=[];
$jobloi[45]=[];
$jobloi[46]=[];
$jobloi[47]=[];
$jobloi[48]=[];
$jobloi[49]=[];
$jobloi[50]=[];
$jobloi[51]=[];
$jobloi[52]=[];
$jobloi[53]=[];
$jobloi[54]=[];
$jobloi[55]=[];
$jobloi[56]=[];
$jobloi[57]=[];
$jobloi[58]=[];
$jobloi[59]=[];
$jobloi[60]=[];
$jobloi[61]=[];
$jobloi[62]=[];
$jobloi[63]=[];
$jobloi[64]=[];
$jobloi[65]=[];
$jobloi[66]=[];
$jobloi[67]=[];
$jobloi[68]=[];
$jobloi[69]=[];
$jobloi[70]=[];
$jobloi[71]=[];
$jobloi[72]=[];
$jobloi[73]=[];
$jobloi[74]=[];
$jobloi[75]=[];
$jobloi[76]=[];
$jobloi[77]=[];
$jobloi[78]=[];
$jobloi[79]=[];
$jobloi[80]=[];
$jobloi[81]=[];
$jobloi[82]=[];
$jobloi[83]=[];
$jobloi[84]=[];
$jobloi[85]=[];
$jobloi[86]=[];
$jobloi[87]=[];
$jobloi[88]=[];
$jobloi[89]=[];
$jobloi[90]=[];
$jobloi[91]=[];
$jobloi[92]=[];
$jobloi[93]=[];
$jobloi[94]=[];
$jobloi[95]=[];
$jobloi[96]=[];
$jobloi[97]=[];
$jobloi[98]=[];
$jobloi[99]=[];
$jobloi[100]=[];

$tkloi=[];



$red="\033[1;31m";
$green="\033[1;32m";
$yellow="\033[1;33m";
$blud="\033[1;34m";
$res="\033[1;35m";
$nau="\033[1;36m";
$trang="\033[1;37m";

error_reporting(0);
system('clear');


function FB($host,$tsm){
  $mr = curl_init();
  curl_setopt_array($mr, array(
  CURLOPT_HEADER => true,
  CURLOPT_PORT => "443",
  CURLOPT_URL => "$host",
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_CUSTOMREQUEST => "GET",
  CURLOPT_HTTPHEADER => $tsm));
  $mr2 = curl_exec($mr); curl_close($mr);
  return $mr2;}


function GL($host,$tsm){
  $mr = curl_init();
  curl_setopt_array($mr, array(
  CURLOPT_PORT => "443",
  CURLOPT_URL => "$host",
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_CUSTOMREQUEST => "GET",
  CURLOPT_HTTPHEADER => $tsm));
  $mr2 = curl_exec($mr); curl_close($mr);
  return $mr2;}

function GL1($host,$tsm,$data){
  $mr = curl_init();
  curl_setopt_array($mr, array(
  CURLOPT_PORT => "443",
  CURLOPT_URL => "$host",
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_SSL_VERIFYPEER => false,
  CURLOPT_TIMEOUT => 30,
  CURLOPT_CUSTOMREQUEST => "POST",
  CURLOPT_POSTFIELDS => $data,
  CURLOPT_HTTPHEADER => $tsm));
  $mr2 = curl_exec($mr); curl_close($mr);
  return $mr2;}




function cc($vanban){$str = strlen($vanban);
for($i=0;$i<=$str;$i++){echo $vanban[$i]; usleep(1000);}
return 1;}

$a1="Host:gomlua.com";
$a2="content-type:application/json";


$bok1="Host:mbasic.facebook.com";
$bok2="sec-ch-ua-mobile:?1";
$bok3="upgrade-insecure-requests:1";
$bok4="sec-fetch-site:same-origin";
$bok5="sec-fetch-mode:navigate";
$bok6="sec-fetch-user:?1";
$bok7="sec-fetch-dest:document";



while(true){


echo $trang."trua nhap tk va mk bam so 1\n";
echo $green."THem TAI KHOAN BAM SO 2 \n";
echo $nau."SUA COOKIE FACEBOOK BAM SO 3\n";
echo $res."CHON DE XOA GMAI VA COOKIE FACEBOOK BAM SO 4 \n";
echo $yellow."DA NHAP THONG TIN VA CHAY TOOL BAM SO 5 \n\n";



echo $nau."MOI BAN CHON : ";
$nhapthongtin=trim(fgets(STDIN));
system('clear');



//////////////////////////////////
if($nhapthongtin==1){
echo $res."ban co bn tk gl : ";
$nhaptk=trim(fgets(STDIN));
//////////////////////////////////
//////////////////////////////////
$k = fopen("cfg.php","a+");
fwrite($k, "<?php"."\n");
fwrite($k, "$"."stk = '$nhaptk';"."\n");
while(true){$n1++;
if($n1==$nhaptk or $n1<$nhaptk){
echo $res."gmai TK SO [$n1] : ";
$gmail=trim(fgets(STDIN));
echo $res."mat khau TK SO [$n1] : ";
$mkm=trim(fgets(STDIN));
fwrite($k, "$"."gmail[$n1] = '$gmail';"."\n");
fwrite($k, "$"."mkm[$n1] = '$mkm';"."\n");
continue;}else{
fwrite($k, "?>");
fclose($k);break;;}}
//////////////////////////////////
while(true){$n2++;
if($n2==$nhaptk or $n2<$nhaptk){
$k = fopen("cokifb.php".$n2."","a+");
fwrite($k, "<?php"."\n");
echo $res."NHAP COOKIE FB  [SO $n2] : ";
$cookie=trim(fgets(STDIN));
fwrite($k, "$"."cookie[$n2] = '$cookie';"."\n");
fwrite($k, "?>");
fclose($k);
///////////////////////////////////
continue;}else{exit;}}}


if($nhapthongtin==2){
include("cfg.php");
if($stk==true){


while(true){$trum++;
include("cfg.php");
$bao=$stk+$trum;
include("cfg.php".$bao."");

if($mtk[$bao]==true){continue;}
if($mtk[$bao]==false){break;}

}


if($mtk[$bao]==false){
$k = fopen("cfg.php".$bao."","a+");
fwrite($k, "<?php"."\n");
fwrite($k, "$"."mtk[$bao] = '$bao';"."\n");
fwrite($k, "$"."stk = '$bao';"."\n");
//////////////////////////////////////////
echo $res."gmai TK SO $bao : ";
$gmail=trim(fgets(STDIN));
echo $res."mat khau TK SO $bao : ";
$mkm=trim(fgets(STDIN));
fwrite($k, "$"."gmail[$bao] = '$gmail';"."\n");
fwrite($k, "$"."mkm[$bao] = '$mkm';"."\n");
fwrite($k, "?>");
fclose($k);
//////////////////////////////////////////
$k = fopen("cokifb.php".$bao."","a+");
fwrite($k, "<?php"."\n");
echo $trang."cookie TK SO $bao : ";
$cookie=trim(fgets(STDIN));
fwrite($k, "$"."cookie[$bao] = '$cookie';"."\n");
fwrite($k, "?>");
fclose($k);
exit;}
} //stk
elseif($stk==false){
echo "TRUA NHAP THONG TIN NHA BAN\n";exit;}
} /// thong tin 2













if($nhapthongtin==3){
echo $res."BAN MUON SUA COOKIE FACEBOOK TK SO MAY : ";
$somay=trim(fgets(STDIN));
system("rm cokifb.php".$somay."");
///////////////////////////////////////
$k = fopen("cokifb.php".$somay."","a+");
fwrite($k, "<?php"."\n");
echo $trang."NHAP LAI COOKIE FACEBOOK TK SO [$somay] : ";
$cookie=trim(fgets(STDIN));
fwrite($k, "$"."cookie[$somay] = '$cookie';"."\n");
fwrite($k, "?>");
fclose($k);
exit;}

if($nhapthongtin==4){
echo $red."XOA HET GMAI VA MAT KHAU VA COOKIE BAM SO 1 \n";
echo $trang."CHI XOA HET COOKIE FACEBOOK BAM SO 2 \n\n";

echo $res."CHON DI BAN : ";
$conso=trim(fgets(STDIN));

if($conso==1){
system("rm cfg.php");

while(true){
$xoahet++;
if($xoahet==105){break;}
system("rm cfg.php".$xoahet."");
system("rm cokifb.php".$xoahet."");
system('clear');continue;}}

if($conso==2){
while(true){
$xoahet++;
if($xoahet==105){break;}
system("rm cokifb.php".$xoahet."");
continue;}}
continue;}
if($nhapthongtin==5){break;}else{continue;}}










$a3="user-agent:Mozilla/5.0 (Linux; Android 10; Active 3 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36";
$tsm=array($a1,$a2,$a3);


while(true){$vi++;
include("cfg.php");
include("cfg.php".$vi."");
if($vi>$stk){break;}
$datalua='{"email":"'.$gmail[$vi].'","password":"'.$mkm[$vi].'"}';
$dn=gl1("https://gomlua.com/user/loginV2?os=web",$tsm,$datalua);
$dn=json_decode($dn,true);
$token[$vi]=$dn['data']['app_token'];

if($token[$vi]==false){echo "TK SO $vi loi \n";continue;}
echo "$token[$vi] \n";
continue;}
system('clear');


while(true){$ci++;sleep(1);
include("cfg.php");
include("cfg.php".$ci."");
if($ci>$stk){break;}
if($token[$ci]==false){continue;}
$a4="app_token: $token[$ci]";
$tsm1=array($a1,$a2,$a3,$a4);
$tk=gl("https://gomlua.com/user/info?os=web",$tsm1);
$tk=json_decode($tk,true);
$name[$ci]=$tk['data']['username'];
$lua1[$ci]=$tk['data']['current_paddy'];
echo $trang."TEN : $name[$ci] | LUA : $lua1[$ci] \n";
}


date_default_timezone_set("Asia/Ho_Chi_Minh");
$datetime = new DateTime();
$thu = array("CN", "T2", "T3", "T4", "T5", "T6", "T7");
$may = (int)$datetime->format('w');
$thumay = $thu[$may];

echo"\n";










while(true){
$zao=0;while($zao<12345678889){$zao++;
include("cfg.php");
include("cfg.php".$zao."");
include("cokifb.php".$zao."");


if($zao>$stk){break;}





$eror1=in_array($zao,$tkloi);
if($eror1==true){
echo "DA CHAN TK $name[$zao] .................\r";
continue;}




$tokena=$token[$zao];
$a5="app_token: $tokena";
$tsm2=array($a1,$a2,$a3,$a5);
$job=gl("https://gomlua.com/cpi/listCampaignFacebook?os=web&type=like_post",$tsm2);




$xi=0;while($xi<123456){$xi++;
if($xi==11){break;}
$linkid[$xi]=explode(',',explode('link_id":',$job)[$xi])[0];



$eror=in_array($linkid[$xi],$jobloi[$zao]);
if($eror==true){continue;}
if($linkid[$xi]==false){break;}
$lua3=explode(',',explode('current_paddy":',$job)[1])[0];
$lua2=explode(',',explode('amount":',$job)[1])[0];
$ty=explode('"',explode('react_type":"',$job)[$xi])[0];
$uid=explode('"',explode('campaign_id":"',$job)[$xi])[0];
$luot=explode('}',explode('size":',$job)[1])[0];
////////////////////////////////////////////////////////////
$html = "htmlspecialchars_decode";

$hq="htpp$uid";
$q=explode('_',explode('htpp',$hq)[1])[0];
$q1=explode(' ',explode('_',$uid)[1])[0];


$boki=$cookie[$zao];
$bok8="cookie:$boki";
$tsm50=array($bok1,$bok2,$bok3,$bok4,$bok5,$bok6,$bok7,$a3,$bok8);
$mbasic=fb("https://mbasic.facebook.com/".$q."/posts/".$q1."",$tsm50);
if(strpos($mbasic,'828281030927956')==true){echo "CHECKPOI :828281030927956\n";$tkloi[]=$zao;break;}
if(strpos($mbasic,'1501092823525282')==true){echo "CHECKPOI :1501092823525282\n";$tkloi[]=$zao;break;}
if(strpos($mbasic,'Tham gia Facebook hoặc đăng nhập để tiếp tục.')==true){echo "COOKIE DIE \n";$tkloi[]=$zao;break;}
if(strpos($mbasic,'Đăng nhập Facebook để xem bài viết này.')==true){echo "COOKIE DIE\n";$tkloi[]=$zao;break;}
if(strpos($mbasic,'Đăng nhập tài khoản của bạn')==true){echo "COOKIE DIE \n";$tkloi[]=$zao;break;}


$loai=explode('"',explode('/reactions/picker/?',$mbasic)[1])[0];
$malen[$xi]=$loai;

//echo "===$malen[$xi] \n";

if($loai==true){}elseif($loai==false){
echo "fb.............[$luot].............loi \r";
$jobloi[$zao][]=$linkid[$xi];
continue;
}






if($ty=="LIKE"){$cx="1";}
if($ty=="LOVE" or $ty=="Thả tim"){$cx="2";}
if($ty=="CARE"){$cx="3";}
if($ty=="HAHA"){$cx="4";}
if($ty=="wow"){$cx="5";}
if($ty=="SAD"){$cx="6";}
if($ty=="ANGRY"){$cx="7";}
$mbasic1=fb("https://mbasic.facebook.com/reactions/picker/?".$html($loai),$tsm50);
$loai1=explode('"',explode('ufi/reaction/?',$mbasic1)[$cx])[0];
if($loai1==true){
for($time=5;$time>-1;$time--){echo $yellow."$name[$zao] bat dau $ty id $linkid[$xi] $time ".$green."[ nhiem vu con lai $luot ] \r";sleep(1);}
}elseif($loai1==false){echo $nau."JOB BI LOI [TK SO $zao] ...................\r";$jobloi[$zao][]=$linkid[$xi];continue;}


$mbasic2=fb("https://mbasic.facebook.com/ufi/reaction/?".$html($loai1),$tsm50);
if(strpos($mbasic2,'Tài khoản của bạn hiện bị hạn chế')==true){echo "$name[$zao] (bi chan tuong tac)\n";$tkloi[]=$zao;break;}
if(strpos($mbasic2,'Bạn hiện không thể bày tỏ cảm xúc')==true){echo "$name[$zai] (bi chan tuong tac)\n";$tkloi[]=$zao;break;}
if(strpos($mbasic2,'Giờ bạn chưa dùng được tính năng này')==true){echo "$name[$zao] (chan tuong tac)\n";$tkloi[]=$zao;break;}
//////////////////////////////////////////////////////
if($check00 = explode('rdr',explode('location: ',$mbasic2)[1])[0]){
////////////////////////////////////////////////
//$kolo=$yellow."$name[$zao] BẮT ĐẦU ĐẦU NHẬN TIỀN ".$trang."[ ID $green$linkid[$xi] ".$trang."]...................\r";
$kolo=$green."DA $ty $linkid[$xi] [$xi job ] ...................\r";
$hkll = explode(' ',explode('https://mbasic.facebook.com/',$check00)[1])[0];
if($hkll == "?_"){
echo $red."chan tuong tac.............\n";
$tkloi[]=$zao;}
else{cc($kolo);}}


continue;}



echo $red."=============================================================\n";
echo $yellow."BAT DAU NHAN TIEN TAT CA JOB [TK $name[$zao] .................\n";
echo $red."=============================================================\n";




$go=0;while($go<123456){$go++;sleep(1);
if($go==$xi){break;}
//////////////////////////////////////////////////////////////
if($linkid[$go]<599999){
$nhantien="https://gomlua.com/likeToken/likeSuccess?os=web&link_id=$linkid[$go]&like_count=1";} 
elseif($linkid[$go]>599999){
$nhantien="https://gomlua.com/cpi/likeSuccess?os=web&link_id=$linkid[$go]&like_old=1";}

if($malen[$go]==false){
echo $trang."DA CHAN JOB $linkid[$go] [job so $go loi]............\r";
continue;}

echo $nau."BAT DAU NHAN TIEN  JOB $linkid[$go] [job so $go ]...\r";


$tay=0;while($tay<123){$tay++;
if($tay==3){break;}
$nhan=gl($nhantien,$tsm2);
$nhan=json_decode($nhan,true);
$code=$nhan['code'];

if($code==2){
for($v=10;$v>-1;$v--){echo"............. $v ............\r";sleep(1);}
continue;}

if($code==406 or $code==504 or $code==554){
echo "DANH NHAN LAI [$tay] .............\r";
}else{break;}}


$solua=$nhan['data']['current_paddy'];
if($solua>$lua3){
$ngay=date("H:i:s");$noe++;
$uu=$res."[$ngay] ".$yellow."DA $blud$ty ".$green."+ $lua2 => $nau$solua [$yellow$noe] ".$red."TK => $trang$name[$zao] ".$blud."[ $yellow$zao ".$blud."]\n";cc($uu);
for($v=60;$v>-1;$v--){echo"............. $v ............\r";sleep(1);}continue;}



elseif($solua<$lua3 or $solua==$lua3){
echo "loi $code ...........................................\r";
$jobloi[$zao][]=$linkid[$go];sleep(3);}


continue;}






//} //xi

} /// zao




}




