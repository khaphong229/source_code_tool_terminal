<?php
error_reporting(0);
date_default_timezone_set("Asia/Ho_Chi_Minh");
$reset="\033[0m";
$red="\033[0;31m";
$white= "\033[0;37m";
$whiteb= "\033[0;37m";
$BBlack="\033[1;30m";      
$BRed="\033[1;31m";
$BGreen="\033[1;32m";
$BYellow="\033[1;33m";
$BBlue="\033[1;34m";
$BPurple="\033[1;35m";
$BCyan="\033[1;36m";
$BWhite="\033[1;37m";
$Blue="\033[1;34m";
$redb="\033[1;31m";
$green="\033[0;32m";
$yellow="\033[1;33m";
$cam="\033[0;33m";
$test="\033[1;33m";
$greenb="\033[1;32m";
$blue="\033[0;34m";
$lam="\033[1;34m";
$tmi="\033[1;34m";
$hong="\033[1;35m";
$imt="\033[1;35m";
$cyan= "\e[1;36m";
$syan="\033[1;36m";
$xnhac= "\033[1;96m";
$den="\033[1;90m";
$do="\033[1;91m";
$luc="\033[1;92m";
$vang="\033[1;93m";
$xduong="\033[1;94m";
$hong="\033[1;95m";
$trang="\033[1;97m";
$vang="\033[1;93m";
$do="\033[1;91m";
$luc="\033[1;92m";
system("cls");
system('clear');
echo($hong."
     __     __        _____            _   _      _   
     \ \   / /       |  __ \          | \ | |    | |  
      \ \_/ /__ _ __ | |__) | __ ___  |  \| | ___| |_ 
       \   / _ \ '_ \|  ___/ '__/ _ \ | . ` |/ _ \ __|
        | |  __/ | | | |   | | | (_) || |\  |  __/ |_ 
        |_|\___|_| |_|_|   |_|  \___(_)_| \_|\___|\__|

           ".$white."Creator:".$vang." Mr. YLV {$do}● {$white}Donate Momo: {$vang}0865924512\n");
echo $vang."    ==========================================================\n";
$list_token = [];
$list_idgr = [];
if (!file_exists('noidung.txt')){
	echo $luc."Nhập nội dung comment: $vang";
	$token_tds = trim(fgets(STDIN));
	file_put_contents('noidung.txt', $token_tds);
}
$messs = file_get_contents("noidung.txt");
$mess = $messs.'
===========================
Time: '.date("H:i:s");
echo $do."[".$luc."●".$do."] ".$trang."=> ".$luc."Nhập số token: {$vang}";
$sltk = trim(fgets(STDIN));
for($tk=1;$tk<=$sltk;$tk++){
  echo $do."[".$luc."●".$do."] ".$trang."=> ".$luc."Nhập token thứ {$do}{$tk}{$luc}: {$vang}";
  $valua_token = trim(fgets(STDIN));
  array_push($list_token,$valua_token);
}
echo $white."Note!!!!! Hãy nhập những group nào mà tất cả nick facebook phía trên đã tham gia nếu chưa tham gia tool sẽ lỗi!!!!\n$reset";
echo $do."[".$luc."●".$do."] ".$trang."=> ".$luc."Nhập số group facebook: {$vang}";
$sltk = trim(fgets(STDIN));
for($gr=1;$gr<=$sltk;$gr++){
  echo $do."[".$luc."●".$do."] ".$trang."=> ".$luc."Nhập ID group thứ {$do}{$gr}{$luc}: {$vang}";
  $valua_idgr = trim(fgets(STDIN));
  array_push($list_idgr,$valua_idgr);
}
echo "{$green}Bạn có thể up ảnh và nhận link tại: {$blue}https://yenla.ga/tien-ich/upload-imgur.php {$green}hoặc {$blue}https://api.yenpro.net/upload/migur/ \n{$reset}";
echo $green."Nhập {$do}no {$green}Hoặc {$do}[Enter] {$luc}để bỏ qua ảnh\n";
echo $do."[".$luc."●".$do."] ".$trang."=> ".$luc."Nhập link ảnh: {$vang}";
$anh = trim(fgets(STDIN));
echo $do."[".$luc."●".$do."] ".$trang."=> ".$luc."Nhập delay: {$vang}";
$timer = trim(fgets(STDIN));
$dem = 0;
echo $vang."    ==========================================================\n";
while(true){
  foreach ($list_idgr as $idgr){
    echo $do."[".$luc."●".$do."] ".$trang."=> ".$luc."Run Group ID: {$vang}{$idgr}\n{$reset}";
    foreach ($list_token as $token){
      $check = check($access_token=$token);
      if($check == "die"){
        echo $do."[".$luc."●".$do."] ".$trang."=> ".$do."Token lỗi hoặc die rồi!! bỏ qua token {$vang}{$token} {$do}nhé!!! \n{$reset}";
        unset($list_token["{$token}"]);
        break;
      }else{
        $name = $check["name"];
        $idfb = $check["id"];
        echo $do."[".$luc."●".$do."] ".$trang."=> ".$green."Run Nick: {$cyan}{$name} {$reset}| {$green}ID: {$cyan}{$idfb}\n";
      }
      $getjob = get_job($token,$idgr);
      if($getjob == "die"){
        unset($list_token["{$token}"]);
        break;
      }else{
        $data_job = $getjob["data"];
      }
      foreach ($data_job as $job){
        $link_job = $job["actions"][0]["link"];
        $id_job = $idgr."_".explode("posts/",$link_job)[1];
       echo $do."[".$luc."●".$do."] ".$trang."=> ".$luc."ID bài viết: $vang {$id_job}\n";
       $bytes = random_bytes(5);
       $messe = $mess.'
       [Captcha] => '.bin2hex($bytes);
       $check_cmt = auto_cmt($token,$id_job,$messe,$anh);
       if($check_cmt["status"] == "die"){
         echo $check_cmt["msg"]."\n";
         echo $do."[".$luc."●".$do."] ".$trang."=> ".$do."Token lỗi hoặc die rồi!! bỏ qua nick {$vang}{$name} {$do}nhé!!! \n{$reset}";
         unset($list_token["{$token}"]);
         break;
       }else{
         $dem = $dem+1;
         $uid = $check_cmt["id"];
         $t=$vang."©©".$vang."[Mr. YLV]".$do." ● ".$vang."[".$vang.$dem.$vang."]".$do." ● ".$xnhac.date("H:i")."".$do." ●".$vang." Comment thành công!".$do." ● ".$vang.$uid."\n";
			  for($i=11;$i<(strlen($t)+1);$i++){
			    echo $t[$i];
			    usleep(3000);
			  }
			  delay_time($timer);
       }
      }
    }
  }
}
function auto_cmt($access_token,$idpost,$mess,$img){
  $url = "https://graph.facebook.com/{$idpost}/comments";
  if($img == "no" or $img == "" or $img == " "){
    $data = array(
      "access_token" => $access_token,
      "message" => $mess
    );
  }else{
    $data = array(
        "access_token" => $access_token,
        "message" => $mess,
        "attachment_url" => $img
      );
  }
  $ch = curl_init();
  curl_setopt($ch, CURLOPT_URL,$url);
  curl_setopt($ch, CURLOPT_POST, 1);
  curl_setopt($ch, CURLOPT_FOLLOWLOCATION, true);
  curl_setopt($ch, CURLOPT_POSTFIELDS,$data);
  curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, 0);
  curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
  $res = curl_exec($ch);
  $result = json_decode($res,true);
  curl_close ($ch);
  if(array_key_exists("error",$result)){
    $kq = $result["error"]["message"];
    $msg = json_encode(["status"=>"die","msg"=>$kq]);
    return json_decode($msg,true);
  }else{
    return $result;
  }
}
function check($access_token){
  $url = "https://graph.facebook.com/me/?fields=id,name&access_token={$access_token}";
  $ch = curl_init();
  curl_setopt($ch, CURLOPT_URL,$url);
  curl_setopt($ch, CURLOPT_POST, 1);
  curl_setopt($ch, CURLOPT_FOLLOWLOCATION, true);
  curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, 0);
  curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
  $res = curl_exec($ch);
  $result = json_decode($res,true);
  curl_close ($ch);
  if(array_key_exists("error",$result)){
    return "die";
  }else{
    return $result;
  }
}
function get_job($access_token,$idgr){
  $url = "https://graph.facebook.com/{$idgr}/feed?access_token={$access_token}";
  $ch = curl_init();
  curl_setopt($ch, CURLOPT_URL,$url);
  curl_setopt($ch, CURLOPT_FOLLOWLOCATION, true);
  curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, 0);
  curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
  $res = curl_exec($ch);
  $result = json_decode($res,true);
  curl_close ($ch);
  if(array_key_exists("error",$result)){
    return "die";
  }else{
    return $result;
  }
}
function delay_time($delay) {
    for ($time = $delay; $time > -1; $time--) {
        echo "\r\033[1;93m   ┗(•°_°•)\033[1;91m ~>       \033[1;92m L      \033[1;91m |\033[1;93m $time\033[1;91m | ";
        usleep(150000);

        echo "\r\033[1;91m   ┗(•°_°•)\033[0;33m   ~>     \033[0;37m LO     \033[0;31m |\033[0;33m $time\033[0;31m | ";
        usleep(150000);
        echo "\r\033[1;92m   ┗(•°_°•)\033[0;33m     ~>   \033[0;37m LOA    \033[0;31m |\033[0;33m $time\033[0;31m | ";
        usleep(150000);
        echo "\r\033[1;94m   ┗(•°_°•)\033[0;33m       ~> \033[0;37m LOAD   \033[0;31m |\033[0;33m $time\033[0;31m | ";
        usleep(150000);
        echo "\r\033[1;95m   ┗(•°_°•)\033[0;33m        ~>\033[0;37m LOAD.  \033[0;31m |\033[0;33m $time\033[0;31m | ";
        usleep(150000);
        echo "\r\033[1;95m   ┗(•°_°•)\033[0;33m        ~>\033[0;37m LOAD.. \033[0;31m |\033[0;33m $time\033[0;31m | ";
        usleep(150000);
        echo "\r\033[1;95m   ┗(•°_°•)\033[0;33m        ~>\033[0;37m LOAD...\033[0;31m |\033[0;33m $time\033[0;31m | ";
        usleep(100000);
        echo "\r                                          \r";
    }}
    
?>