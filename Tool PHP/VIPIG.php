<?php
error_reporting(0); 
session_start();
echo "\e[38;5;208m ------- Support VIPIG -------\e[38;5;208m \n";
$xuong = "\n";
 $do="\033[1;91m";
 $maufulldo= "\e[1;47;31m"; 
$maunenhong= "\033[1;41;33m"; 
$white= "\033[1;37m";
$red="\033[1;31m";
$pink="\e[1;35m"; 
$green="\e[1;32m"; 
$yellow="\e[1;33m";
$white= "\033[0;37m"; 
$cyan= "\e[1;36m"; 
$blue="\e[1;34m"; 
$cam= "\e[38;5;208m";
$TIME='date "+%H:%M"';date_default_timezone_set("Asia/Ho_Chi_Minh");
$useragent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36";
$_SESSION['fck'] = file_exists("VIPIG.txt");
if ($_SESSION['fck'] == '1'){
  unlink("VIPIG.txt");
}
$_SESSION['check'] = file_exists("logVIPIG.txt");
$_SESSION['checklistcc'] = file_exists("ListccVIPIG.txt");
$nhaplaicc = false;
if ($_SESSION['check'] =='1'){
  luachon:
  echo "\n";
echo$white." Nhập$cam Enter$white để vào tool! $xuong Nhập$red No$white để đăng nhập lại VIPIG : ";
$_SESSION['nhap'] = trim(fgets(STDIN));
if ($_SESSION['nhap'] !='no' and $_SESSION['nhap'] != 'No' and $_SESSION['nhap'] !=''){
echo $red."Sai Định Dạng\n";
GOTO luachon;
}
if ($_SESSION['nhap'] =='no' or $_SESSION['nhap'] =='No'){
$my = fopen("logVIPIG.txt", "w+");
echo $white." ⏩ ".$green."Tài khoản VIPIG: ";
$username =trim(fgets(STDIN));
echo $white." ⏩ ".$green."Mật Khẩu VIPIG : ";
$password =trim(fgets(STDIN));
$arr = array("username"=> $username, "password"=> $password);
fwrite($my,json_encode($arr));
    $my = file("logVIPIG.txt");
$bb = file_get_contents('logVIPIG.txt');
$cc =json_decode($bb);
$_SESSION['username']= $cc->{"username"};
$_SESSION['password']= $cc->{"password"};
}
if ($_SESSION['nhap'] == ''){
$bb = file_get_contents("logVIPIG.txt");
$cc =json_decode($bb);
$_SESSION['username']= $cc->{"username"};
$_SESSION['password']= $cc->{"password"};
}
} else {
  login:
$my = fopen("logVIPIG.txt","w+");
echo "\n";
echo $white." ⏩ ".$green."Tài khoản VIPIG : ";
$_SESSION["username"]=trim(fgets(STDIN));
echo $white." ⏩ ".$green."Mật Khẩu VIPIG : ";
$_SESSION['password']=trim(fgets(STDIN));
$arr = array("username"=> $_SESSION["username"], "password"=> $_SESSION['password']);
fwrite($my,json_encode($arr));
}
$user = $_SESSION['username'];
$pass = $_SESSION['password'];
$source = getcookieVIPIG($user,$pass,$useragent);
$sou= strlen($source);
if ($sou < 10 ){
  echo $white." ✅ ".$green."Đăng nhập VIPIG thành công\n";
  // get xu
  $url = "https://vipig.net/home.php";
  $curl = curl_init();
  curl_setopt_array($curl, array(
  CURLOPT_PORT => "443",
  CURLOPT_URL => "$url",
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => "",
  CURLOPT_SSL_VERIFYPEER => true,
  CURLOPT_CUSTOMREQUEST => "GET",
  CURLOPT_COOKIEFILE => "VIPIG.txt"
  ));
  $data = curl_exec($curl);
  curl_close($curl);
  preg_match('#id="soduchinh">(.+?)<#is', $data, $sd);
  $xu = $sd["1"];
  $_SESSION['xu'] = $xu;
}else{
	echo $red." ❌ ".$red."Sai Username hoặc Password\n";
	 GOTO login;
}

  choosetr:
  echo "\n";
if($_SESSION['checklistcc'] =='1'){
  echo$white." Nhập$cam Enter$white để dùng list cookies đã lưu! $xuong Nhập$red 1$white để nhập lại list cookie : ";
$_SESSION['nhapcc'] = trim(fgets(STDIN));
if ($_SESSION['nhapcc'] !='1' and $_SESSION['nhapcc'] !=''){
echo $red."Sai lựa chọn\n";
GOTO choosetr;
}else if($_SESSION['nhapcc'] ==''){
	$mangcookie =[];
	$listccdaluu = explode("\n",file_get_contents("ListccVIPIG.txt"));
	for($i=0;$i<count($listccdaluu); $i++){
		$access = cookie($listccdaluu[$i],$useragent);
		$configdata = json_decode(trim(explode('}}}',explode('["XIGSharedData",[],', $access)[1])[0].'}}}'),true);
		if ($configdata !== null && $configdata['raw'] !== null)
		{
				array_push($mangcookie,$listccdaluu[$i]);

		}
	}
	$luong = count($mangcookie);
}else if($_SESSION['nhapcc'] =='1'){
	$nhaplaicc = true;
}
}else{
	$nhaplaicc = true;
}
if($nhaplaicc == true){
unlink("ListccVIPIG.txt");
choose:
echo $white." ✏ ".$blue."Nhập số ních INSTA muốn chạy: ";
$luong=trim(fgets(STDIN));
if ($luong<1 || $luong >2000){
  echo $red."\033[1;37m~\033[1;31m Ít nhất là 1 và nhiều nhất là 2000 má ưiii !!!\n";
  GOTO choose;
  }
$c=1;$thu=1;
$mangcookie =[];
for($b=1;$b<=$luong;$b++){
    echo $white." + ".$green."Nhập Cookie Thứ ".$thu.":$white ";
    $cooki[$c]=trim(fgets(STDIN));
    // $ch=curl_init();
    $cookie=$cooki[$c];
$access = cookie($cookie,$useragent);
$configdata = json_decode(trim(explode('}}}',explode('["XIGSharedData",[],', $access)[1])[0].'}}}'),true);
if ($configdata !== null && $configdata['raw'] !== null)
{
        array_push($mangcookie,$cookie);
		file_put_contents("ListccVIPIG.txt",$cookie."\n",FILE_APPEND);
	             $c++;
	            $thu++;
}else{echo $white." ⛔ ".$red."Cookie die rồi, thử lại đi \n";$b--;}
}
}

if($luong==1){
  echo $white." ⏩ ".$blue."Hết nhiệm vụ hoặc lỗi thì dừng bao lâu? : $white ";
  $dl=trim(fgets(STDIN));
  $doi = 99999;
}else{
	nhiemvu:
$dl = 150;
echo $white." ⏩ ".$blue."Sau bao nhiêu nhiệm vụ thì đổi cấu hình : $white ";
$doi=trim(fgets(STDIN));
if ($doi<1){
  echo $red."\033[1;37m~\033[1;31m Lựa chọn không hợp lệ !\n";
  GOTO nhiemvu;
}
}



$listnv = [];
  Job:
  echo $yellow." ⏩ ".$blue."Chế độ Follow$pink (on/off): $white";
  $chon1=trim(fgets(STDIN));
  if ($chon1 == 'on' or $chon1 == 'On' or $chon1 == 'ON'){
    array_push($listnv,'sub');
	Time_nv:
  echo $yellow." ⏩ ".$blue."Delay Nhiệm Vụ Follow (lớn hơn 20): $white";
  $timedelay=trim(fgets(STDIN));
  if($timedelay < 20)
    {
      echo $red."\033[1;37m~\033[1;31m Delay Follow không hợp lệ, tối thiểu 20 !\n";
      GOTO Time_nv;
    }
  }
  echo $yellow." ⏩ ".$blue."Chế độ Tym$pink (on/off): $white";
  $chon1=trim(fgets(STDIN));
  if ($chon1 == 'on' or $chon1 == 'On' or $chon1 == 'ON'){
    array_push($listnv,'tym');
	Time_nvtym:
	echo $yellow." ⏩ ".$blue."Delay Nhiệm Vụ Tym (lớn hơn 10): $white";
  $timedelaytym=trim(fgets(STDIN));
  
	if($timedelaytym < 10)
    {
      echo $red."\033[1;37m~\033[1;31m Delay Tym không hợp lệ, tối thiểu 10 !\n";
      GOTO Time_nvtym;
    }
  }
  if (count($listnv) == 0){
    echo $red."Chọn tối thiểu 1 loại Job !\n";
    GOTO Job;
  }
  
  
usleep(200000);

echo $white."             \n";
for($v=0;$v<= 12;$v++){
    echo "\033[1;37m- ";usleep(15000);
    echo "\033[1;33m- ";usleep(15000);
}
echo "\033[1;37m- ";usleep(15000);
echo "\033[1;33m-";usleep(15000);
echo"\n";
echo $cyan." ✅ ".$cam."Username: $white".$user."\n";
echo $cyan." ✅ ".$cam."Account number :$white $luong\n";
echo $cyan." ✅ ".$cam."Coin :$white $xu\n";
echo $cyan." ✅ ".$cam."ID tool :$white T001\n";
echo $cyan." ✅ ".$cam."Verison :$white V.2\n";
echo $cyan." ✅ ".$cam."Follow 6 lần sẽ nhận xu TẤT CẢ 1 lượt\n";
for($v=0;$v<= 12;$v++){
    echo "\033[1;37m- ";usleep(15000);
    echo "\033[1;33m- ";usleep(15000);
}
echo "\033[1;37m- ";usleep(15000);
echo "\033[1;33m-";usleep(15000);
echo"\n";
$q=1;
while (0<1){
for($l=0;$l<count($mangcookie);$l++){
$cookie = $mangcookie[$l];
$access = cookie($cookie,$useragent);
$configdata = json_decode(trim(explode('}}}',explode('["XIGSharedData",[],', $access)[1])[0].'}}}'),true);
if ($configdata !== null && $configdata['raw'] !== null)
{
	$dataa = json_decode($configdata['raw'],true);
  $idfb =  $dataa['config']['viewerId'];
  $tenfb =  $dataa['config']['viewer']['username'];
  $h = datnick($idfb,$useragent);
}else{
  echo "                                     \r";
  echo $white." ⛔ ".$red."Cookie Die - ĐANG ĐỔI NICK\n";
  array_splice($mangcookie,$l,1);
}

if ($h == '1'){
echo "                                                    \r";
echo $white." Supports VIPIG - ".$green."Account: $cam".$tenfb."\n";
        $i=1;
        $max=0;
 $rand = $listnv[array_rand($listnv,1)];

  if ($rand == 'sub'){
    $loai = 'sub';
    $list = getnv($loai,$useragent);
    $check = count($list);
    if($check <5){
      echo "                                                      \r";
     echo $white." ❌ ".$red."Ko đủ 5 Nhiệm Vụ Follow\r";
	 if(count($mangcookie)==1){
          echo "                                                      \r";
           for($j = $dl;$j> 0;$j--){
             echo $green."Đang Chờ Delay Tránh Block$yellow $j Giây";
             sleep(1);
             echo "\r";
           }
        }
    }else{
	$churk_list = array_chunk($list,6);
	if(count($churk_list[count($churk_list) - 1]) <5){
	$rmd = array_pop($churk_list);
	}
	foreach ($churk_list  as $listid) {
	$idnhanxu ='';
	$coloigiuachung = false;
    foreach ($listid  as $id) {

    $id = $id[("soID")];
	$idnhanxu .= $id.",";
	$csf = explode(';',explode('csrftoken=', $cookie)[1])[0];
	$chayfl = follow($id,$cookie,$csf);
	$max=$max+1;
    $g = json_decode($chayfl,true);
    if($g == null || $g['status'] !== 'ok'){
	echo "\r";
    echo "                                              \r";
	echo $red." ●$red FOLLOW LỖI$red ● $white";	
	echo "\n";
	
	$ck = hoanthanhsub(rtrim($idnhanxu,","));
	if($ck !== null){
		if(isset($ck['mess'])){
			echo "\r";
		  echo "                                              \r";

		  echo date("H:i");
		  echo $green." ⏩ ".$green.$ck['mess']."\n";
		}else if(isset($ck['error'])){
			echo "\r";
		  echo "                                              \r";

		  echo date("H:i");
		  echo $red." ⏩ ".$red.$ck['error']."\n";
		}
	}
	$xu = getxu();
      echo "\r";
      echo "                                              \r";

      echo date("H:i");
      echo $white." ⏩ ".$blue."Số dư : $white ";
      echo $xu."\n";
	
	$coloigiuachung = true;
	if(count($mangcookie)==1){
          echo "                                                      \r";
           for($j = $dl;$j> 0;$j--){
             echo $green."Đang Chờ Delay Tránh Block$yellow $j Giây";
             sleep(1);
             echo "\r";
           }
		   break 1;
    }else if(count($mangcookie) > 1){
		echo "\r";
    echo "                                              \r";
	echo $blue." ⏩$blue ĐANG ĐỔI NICK$blue ● $white";	
	echo "\n";
		 break 2;
	}
	}else{
    echo "\r";
    echo "                                              \r";
	echo $green." ●$green FOLLOW THÀNH CÔNG$green ● $white";
	echo "\n";
	}
	loadtime($timedelay);
	
    } // foreach
	if($coloigiuachung == false){
	$ck = hoanthanhsub(rtrim($idnhanxu,","));
	if($ck !== null){
		if(isset($ck['mess'])){
			echo "\r";
		  echo "                                              \r";

		  echo date("H:i");
		  echo $green." ⏩ ".$green.$ck['mess']."\n";
		}else if(isset($ck['error'])){
			echo "\r";
		  echo "                                              \r";

		  echo date("H:i");
		  echo $red." ⏩ ".$red.$ck['error']."\n";
		}
	}
	$xu = getxu();
      echo "\r";
      echo "                                              \r";

      echo date("H:i");
      echo $white." ⏩ ".$blue."Số dư : $white ";
      echo $xu."\n";
	}
	  if ($max >= $doi){
           $max=0;
           break;
          }
	}
  }
  }
  if ($rand == 'tym'){
    //$loai = 'sub';
    $list = getnv("tym",$useragent);
    $check = count($list);
    if($check <0){
      echo "                                                      \r";
     echo $white." ❌ ".$red."Hết nhiệm vụ tym rồi\r";
	 if(count($mangcookie)==1){
          echo "                                                      \r";
           for($j = $dl;$j> 0;$j--){
             echo $green."Đang Chờ Delay Tránh Block$yellow $j Giây";
             sleep(1);
             echo "\r";
           }
        }
    }else{

	foreach ($list  as $listid) {
	$soloitym = 0;

    $id = $listid['idpost'];
	
	$csf = explode(';',explode('csrftoken=', $cookie)[1])[0];
	$chayfl = tym($id,$cookie,$csf);
	 //echo $id."-".$chayfl."\n";
	$max=$max+1;
    $g = json_decode($chayfl,true);
    if($g == null || $g['status'] !== 'ok'){
	echo "\r";
    echo "                                              \r";
	echo $red." ●$red TYM LỖI$red ● $white";	
	echo "\n";
	$soloitym ++;
	}else{
    echo "\r";
    echo "                                              \r";
	echo $green." ●$green TYM THÀNH CÔNG$green ● $white";
	echo "\n";
	$ck = hoanthanhtym($id);
	if($ck !== null){
		if(isset($ck['mess'])){
			$soloitym = 0;
			echo "\r";
		  echo "                                              \r";

		  echo date("H:i");
		  echo $green." ⏩ ".$green.$ck['mess']."\n";
		  $_SESSION['xu'] = $_SESSION['xu']+300;
		}else if(isset($ck['error'])){
			echo "\r";
		  echo "                                              \r";

		  echo date("H:i");
		  echo $red." ⏩ ".$red.$ck['error']."\n";
		  
		  // echo $id."\n";
		}
	}
	$xu = $_SESSION['xu'];
      echo "\r";
      echo "                                              \r";

      echo date("H:i");
      echo $white." ⏩ ".$blue."Số dư : $white ";
      echo $xu."\n";
	}
	loadtime($timedelaytym);
	
	if($soloitym >4){
		if(count($mangcookie)==1){
          echo "                                                      \r";
           for($j = $dl;$j> 0;$j--){
             echo $green."Đang Chờ Delay Tránh Block$yellow $j Giây";
             sleep(1);
             echo "\r";
           }
		   //break 1;
    }else if(count($mangcookie) > 1){
		echo "\r";
    echo "                                              \r";
	echo $blue." ⏩$blue ĐANG ĐỔI NICK$blue ● $white";	
	echo "\n";
		 break 1;
	}
	}
	
  if ($max >= $doi){
	   $max=0;
	   break;
	  }
	}
  }
  }


}else if($h == '2'){
	echo "\r";
      echo "                                              \r";

      echo date("H:i");
      echo $white." ⏩ ".$red."Cần thêm nick : $white".$tenfb.$red." vào trước khi chạy";
      echo $xu."\n";
}else{
	echo "\r";
      echo "                                              \r";

      echo date("H:i");
      echo $white." ⏩ ".$red."LỖI, ĐANG ĐỔI NICK";
      echo $xu."\n";
}
}
}
if (count($mangcookie)==1 && empty($dl)){
  echo $pink." ⏩ ".$blue."Dừng Thời Gian: ";
  $dl=trim(fgets(STDIN));
}
if (count($mangcookie)==0){
unlink("ListccVIPIG.txt");
echo $pink." ⛔ ".$red."Tất Cả Cookie Đều Die\n";
echo $pink." ⏩ ".$red."Ctrl+C và chạy lại tool\n";


}
// }



function cookie($cookie,$useragent){
$ch = curl_init();
  curl_setopt($ch, CURLOPT_URL, 'https://www.instagram.com/');
$head[] = "Connection: keep-alive";
$head[] = "Keep-Alive: 300";
$head[] = "authority: www.instagram.com";
$head[] = "ccept-Charset: ISO-8859-1,utf-8;q=0.7,*;q=0.7";
$head[] = "accept-language: vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5";
$head[] = "cache-control: max-age=0";
$head[] = "upgrade-insecure-requests: 1";
$head[] = "accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9";
$head[] = "sec-fetch-site: none";
$head[] = "sec-fetch-mode: navigate";
$head[] = "sec-fetch-user: ?1";
$head[] = "sec-fetch-dest: document";
curl_setopt($ch, CURLOPT_USERAGENT,$useragent );
curl_setopt($ch, CURLOPT_ENCODING, '');
curl_setopt($ch, CURLOPT_COOKIE, $cookie);
curl_setopt($ch, CURLOPT_HTTPHEADER, $head);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, FALSE);
curl_setopt($ch, CURLOPT_TIMEOUT, 60);
curl_setopt($ch, CURLOPT_CONNECTTIMEOUT, 60);
curl_setopt($ch, CURLOPT_FOLLOWLOCATION, TRUE);
curl_setopt($ch, CURLOPT_HTTPHEADER, array('Expect:'));
$access = curl_exec($ch);
curl_close($ch);

return $access;
}
function follow($id,$cookie,$csrftoken = null){
	$ch=curl_init();
	curl_setopt($ch, CURLOPT_URL, 'https://www.instagram.com/web/friendships/'.$id.'/follow/');
	$headers = [
    'x-requested-with: XMLHttpRequest',
    'x-ig-www-claim: hmac.AR2KtRYzNVfelijR0GD6-VLJU3G-vRVGUezuXpjzaQ5m4MmZ',
    'x-ig-app-id: 936619743392459',
    'x-csrftoken: '.$csrftoken.'',
    'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36',
    'x-instagram-ajax: bd344c4b4f36',
    'referer: https://www.instagram.com/'
];
	curl_setopt($ch, CURLOPT_USERAGENT, 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36');
	curl_setopt($ch, CURLOPT_ENCODING, '');
	curl_setopt($ch, CURLOPT_COOKIE, $cookie);
	curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);
	curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
	curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, FALSE);
	curl_setopt($ch, CURLOPT_TIMEOUT, 60);
	curl_setopt($ch, CURLOPT_CONNECTTIMEOUT, 60);
	curl_setopt($ch, CURLOPT_FOLLOWLOCATION, TRUE);
	//curl_setopt($ch, CURLOPT_HTTPHEADER, array('Expect:'));
	curl_setopt($ch, CURLOPT_POST,true);
	curl_setopt($ch, CURLOPT_POSTFIELDS,array());
	$access = curl_exec($ch);
	curl_close($ch);
	return $access;
}
function shortcode_to_mediaid($shortcode,$cookie){

    $mediaid = false;

    $ch = curl_init();
  curl_setopt($ch, CURLOPT_URL, 'https://www.instagram.com/p/'.$shortcode);
$head[] = "Connection: keep-alive";
$head[] = "Keep-Alive: 300";
$head[] = "authority: www.instagram.com";
$head[] = "ccept-Charset: ISO-8859-1,utf-8;q=0.7,*;q=0.7";
$head[] = "accept-language: vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5";
$head[] = "cache-control: max-age=0";
$head[] = "upgrade-insecure-requests: 1";
$head[] = "accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9";
$head[] = "sec-fetch-site: none";
$head[] = "sec-fetch-mode: navigate";
$head[] = "sec-fetch-user: ?1";
$head[] = "sec-fetch-dest: document";
curl_setopt($ch, CURLOPT_USERAGENT, 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36');
curl_setopt($ch, CURLOPT_ENCODING, '');
curl_setopt($ch, CURLOPT_COOKIE, $cookie);
curl_setopt($ch, CURLOPT_HTTPHEADER, $head);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, FALSE);
curl_setopt($ch, CURLOPT_TIMEOUT, 60);
curl_setopt($ch, CURLOPT_CONNECTTIMEOUT, 60);
curl_setopt($ch, CURLOPT_FOLLOWLOCATION, TRUE);
$access = curl_exec($ch);
curl_close($ch);
if(strpos($access,'"media_id":"') !== false){
	$mediaid = explode('"',explode('"media_id":"',$access)[1])[0];
}
return $mediaid;

}
function tym($id,$cookie,$csrftoken = null){
	$mediaid = shortcode_to_mediaid($id,$cookie);
	if($mediaid !==false){
	$ch=curl_init();
	curl_setopt($ch, CURLOPT_URL, 'https://www.instagram.com/web/likes/'.$mediaid.'/like/');
	$headers = [
    'x-requested-with: XMLHttpRequest',
    'content-length: 0',
    'content-type: application/x-www-form-urlencoded',
    'x-ig-www-claim: hmac.AR2KtRYzNVfelijR0GD6-VLJU3G-vRVGUezuXpjzaQ5m4MmZ',
    'x-ig-app-id: 936619743392459',
    'x-csrftoken: '.$csrftoken.'',
    'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
    'x-instagram-ajax: 1005633491',
    'referer: https://www.instagram.com/p/'.$id.'/'
];
	curl_setopt($ch, CURLOPT_USERAGENT, 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36');
	curl_setopt($ch, CURLOPT_ENCODING, '');
	curl_setopt($ch, CURLOPT_COOKIE, $cookie);
	curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);
	curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
	curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, FALSE);
	curl_setopt($ch, CURLOPT_TIMEOUT, 60);
	curl_setopt($ch, CURLOPT_CONNECTTIMEOUT, 60);
	curl_setopt($ch, CURLOPT_FOLLOWLOCATION, TRUE);
	//curl_setopt($ch, CURLOPT_HTTPHEADER, array('Expect:'));
	curl_setopt($ch, CURLOPT_POST,true);
	curl_setopt($ch, CURLOPT_POSTFIELDS,array());
	$access = curl_exec($ch);
	curl_close($ch);
	
	return $access;
	}else{
		return '';
	}
}
function loadtime($time){
        for ( $x = $time; $x--; $x ) {
echo "                                                      \r";
echo "\e[1;32m🇻🇳 Vui Lòng Chờ \e[1;37m \e[1;31m- \e[1;32m- \e[1;33m- \e[1;34m- \e[1;35m- \e[1;37m ".$x."\033[1;37m \e[1;33mGiây";
usleep(170000);
echo "\r";
echo "                                                      \r";
echo "\e[1;36m🇻🇳 Vui Lòng Chờ \e[1;37m \e[1;33m- \e[1;34m- \e[1;35m- \e[1;36m- \e[1;31m- \e[1;37m ".$x."\033[1;37m \e[1;34m Giây";
       usleep(170000);
       echo "\r";
       echo "                                                      \r";
       echo "\e[1;34m🇻🇳 Vui Lòng Chờ \e[1;37m \e[1;34m- \e[1;35m- \e[1;36m- \e[1;31m- \e[1;33m- \e[1;37m ".$x."\033[1;37m \e[1;31m Giây";
       usleep(170000);
       echo "\r";
       echo "                                                      \r";
       echo "\e[1;33m🇻🇳 Vui Lòng Chờ \e[1;37m \e[1;35m- \e[1;36m- \e[1;31m- \e[1;33m- \e[1;34m- \e[1;37m ".$x."\033[1;37m \e[1;32m Giây";
       usleep(170000);
       echo "\r";
       echo "                                                      \r";
       echo "\e[1;31m🇻🇳 Vui Lòng Chờ \e[1;37m \e[1;33m- \e[1;32m- \e[1;31m- \e[1;35m- \e[1;36m-\e[1;37m ".$x."\033[1;37m \e[1;36m Giây";
       usleep(170000);
       echo "\r";
}
}

function getcookieVIPIG($user,$pass,$useragent){
  $ch=curl_init();
curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
curl_setopt($ch, CURLOPT_URL, 'https://vipig.net/login.php');
curl_setopt($ch, CURLOPT_COOKIEJAR, "VIPIG.txt");
curl_setopt($ch, CURLOPT_USERAGENT,$useragent);
$login =array('username' => $user,'password' => $pass,'submit' => 'ĐĂNG NHẬP');
curl_setopt($ch, CURLOPT_POST,count($login));
curl_setopt($ch, CURLOPT_POSTFIELDS,$login);
curl_setopt($ch, CURLOPT_COOKIEFILE, "VIPIG.txt");
$source=curl_exec($ch);
curl_close($ch);
return $source;
}
function datnick($idfb,$useragent){
$dat=http_build_query(array('iddat[]'=> $idfb));
$ch=curl_init();
	curl_setopt($ch, CURLOPT_URL,'https://vipig.net/cauhinh/datnick.php');
	$head[]='Host: vipig.net';
	$head[]='content-length: '.strlen($dat);
	$head[]='accept: */*';
	$head[]='origin: https://vipig.net';
	$head[]='x-requested-with: XMLHttpRequest';
	$head[]='save-data: on';
	$head[]='content-type: application/x-www-form-urlencoded; charset=UTF-8';
	$head[]='referer: https://vipig.net/cauhinh/index.php';
	$head[]='accept-language: vi-VN, vi;q=0.9,fr-FR;q=0.8,fr;q=0.7, en-US;q=0.6,en;q=0.5,zh-CN;q=0.4.zh;q=0.3';
	$head[]='cookie: TawkConnectionTime=0';
  curl_setopt($ch, CURLOPT_USERAGENT, $useragent);
	curl_setopt($ch,CURLOPT_FOLLOWLOCATION,TRUE);
  curl_setopt($ch,CURLOPT_RETURNTRANSFER, 1);
  curl_setopt($ch,CURLOPT_POST, 1);
  curl_setopt($ch,CURLOPT_POSTFIELDS,$dat);
  curl_setopt($ch,CURLOPT_SSL_VERIFYPEER,0);
  curl_setopt($ch,CURLOPT_HTTPHEADER, $head);
  curl_setopt($ch,CURLOPT_ENCODING, TRUE);
  curl_setopt($ch,CURLOPT_COOKIEFILE,"VIPIG.txt");
	$h = curl_exec($ch);
	curl_close($ch);
	return $h;
}

function getnv($loai,$useragent){
 $ch=curl_init();
 if($loai == 'tym'){
	curl_setopt($ch, CURLOPT_URL,'https://vipig.net/kiemtien/getpost.php');
	$head[]='referer: https://vipig.net/kiemtien/';
 }else{
 curl_setopt($ch, CURLOPT_URL,'https://vipig.net/kiemtien/'.$loai.'cheo/getpost.php');
 $head[]='referer: https://vipig.net/kiemtien/'.$loai.'cheo';
 }
 $head[]='Host: vipig.net';
 $head[]='accept: application/json, text/javascript, *'.'/'.'*; q=0.01';
 $head[]='x-requested-with: XMLHttpRequest';
 $head[]='user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36';
 
 curl_setopt($ch, CURLOPT_USERAGENT, $useragent);
 curl_setopt($ch,CURLOPT_FOLLOWLOCATION, TRUE);
 curl_setopt($ch,CURLOPT_RETURNTRANSFER,1);
 curl_setopt($ch,CURLOPT_POST,1);
 curl_setopt($ch,CURLOPT_HTTPGET, true);
 curl_setopt($ch,CURLOPT_SSL_VERIFYPEER, 0);
 curl_setopt($ch,CURLOPT_HTTPHEADER, $head);
 curl_setopt($ch,CURLOPT_ENCODING, TRUE);
 curl_setopt($ch,CURLOPT_COOKIEFILE, "VIPIG.txt");
 return json_decode(curl_exec($ch),true);
 curl_close($ch);
}

function getxu(){
  $url = "https://vipig.net/home.php";
  $curl = curl_init();
  curl_setopt_array($curl, array(
  CURLOPT_PORT => "443",
  CURLOPT_URL => "$url",
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => "",
  CURLOPT_SSL_VERIFYPEER => true,
  CURLOPT_CUSTOMREQUEST => "GET",
  CURLOPT_COOKIEFILE => "VIPIG.txt"
  ));
  $data = curl_exec($curl);
  curl_close($curl);
  preg_match('#id="soduchinh">(.+?)<#is', $data, $sd);
  $xu = $sd["1"];
  return $xu;
  $_SESSION['xu'] = $xu;
}

function hoanthanhsub($id)
{
    $url  = "https://vipig.net/kiemtien/subcheo/nhantien2.php";
    $data= ('id=').$id;
    $head = array(
        "Host: vipig.net",
        "content-length: " . strlen($data),
        "x-requested-with: XMLHttpRequest",
        "user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36",
        "content-type: application/x-www-form-urlencoded; charset=UTF-8",
        "origin: https://vipig.net",
        "referer: https://vipig.net/kiemtien/subcheo/"
    );
    $ch   = curl_init();
    curl_setopt_array($ch, array(
        CURLOPT_URL => $url,
        CURLOPT_FOLLOWLOCATION => TRUE,
        CURLOPT_RETURNTRANSFER => 1,
        CURLOPT_POST => 1,
        CURLOPT_POSTFIELDS => $data,
        CURLOPT_SSL_VERIFYPEER => 0,
        CURLOPT_COOKIEFILE => "VIPIG.txt",
        CURLOPT_HTTPHEADER => $head,
        CURLOPT_ENCODING => TRUE
    ));
    $a = json_decode(curl_exec($ch), true);
    return $a;
}
function hoanthanhtym($id)
{
    $url  = "https://vipig.net/kiemtien/nhantien.php";
    $data= ('id=').$id;
    $head = array(
        "Host: vipig.net",
        "content-length: " . strlen($data),
        "x-requested-with: XMLHttpRequest",
        "user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36",
        "content-type: application/x-www-form-urlencoded; charset=UTF-8",
        "origin: https://vipig.net",
        "referer: https://vipig.net/kiemtien/"
    );
    $ch   = curl_init();
    curl_setopt_array($ch, array(
        CURLOPT_URL => $url,
        CURLOPT_FOLLOWLOCATION => TRUE,
        CURLOPT_RETURNTRANSFER => 1,
        CURLOPT_POST => 1,
        CURLOPT_POSTFIELDS => $data,
        CURLOPT_SSL_VERIFYPEER => 0,
        CURLOPT_COOKIEFILE => "VIPIG.txt",
        CURLOPT_HTTPHEADER => $head,
        CURLOPT_ENCODING => TRUE
    ));
    $a = json_decode(curl_exec($ch), true);
    return $a;
}
?>