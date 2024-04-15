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

#https://www.subpals.com/
$cka="_ga=GA1.2.1165813625.1672394043; shopmagic_visitor_84938ff465a7a5148a30ef3d43f9bfff=%7B%22meta%22%3A%5B%5D%2C%22hash%22%3A%22d80115171dfbf6f5f65237646cdc26bf%22%7D; cookieaccepted=1; _pbjs_userid_consent_data=3524755945110770; _pubcid=daebc5b0-8e26-4b6e-8d4b-b6d60dc1496c; __gads=ID=d70900e4856500e1:T=1672394625:S=ALNI_MZWMAEcvW9LyN-5wIPQ9kZgPA4Y6Q; _cc_id=1bdac2ef333313dc81c0afb6b1be4285; _gid=GA1.2.328068940.1678233248; __cf_bm=EySaCXJjEqxfvnpRCc3_u5T0_sMnpa0kP72hQmQNPP4-1678428487-0-Aet5quMYwl4XWTepXWnYkbfUfSYf4Cek17U7DeAW9c2V19oLrHJZO94IY2IGlyjypVcfYnxL34eUqzb36qCCA40=; PHPSESSID=qiglrvr0452hbjc44a59a53egh; __gpi=UID=00000b9a89a7f8c6:T=1672394625:RT=1678428507:S=ALNI_MYMdSDQyPhk6ehvyNJggk24CRQd9Q; panoramaId_expiry=1678514907975; panoramaId=ea30ba100e316a62e96ebc139d4ea9fb927af16bcbed906d9d8bc98c18b40630; panoramaIdType=panoDevice; cto_bundle=m3nixl94SHRxUkVTemdseUdweXNYckxvM2xGSXpGSWF4MkExc2o0amtOVURlVnI2MEVmZlVBJTJGYjMyJTJCTldWQmc0eDJBMDJ0TzdMM2pmMG5LZGx0TUluSnZhZ2VkNnRjNjNpOTM3RiUyQllUOGpBaFlKNSUyQmVUczRlRzdPRzdjaVFnWUFRUzE2Z1M0N0hXbUJLVTZlZzhaUW9uamd0dyUzRCUzRA; _gat=1; _gat_gtag_UA_18712495_28=1; __atuvc=4%7C6%2C9%7C7%2C0%7C8%2C0%7C9%2C57%7C10; __atuvs=640ac9474d1b4827006; useragent=TW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEwOS4wLjAuMCBTYWZhcmkvNTM3LjM2; _uafec=Mozilla%2F5.0%20(Windows%20NT%2010.0%3B%20Win64%3B%20x64)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F109.0.0.0%20Safari%2F537.36; ";

#https://www.ytpals.com/login/
$ckb="_ga=GA1.2.1653116204.1672467888; hblid=bcPlO1teRmQsHj9c276LI0Ib8zB0zr25; cookieaccepted=1; olfsk=olfsk7656692775789862; _gid=GA1.2.1467463214.1678235765; PHPSESSID=1e1033304513a8fcb9d4b8b9e7d0753a; _gat_gtag_UA_18712495_34=1; wcsid=KnxSKqLi0RSqdtxs276LI0I60SAbBaAo; _okdetect=%7B%22token%22%3A%2216784285290620%22%2C%22proto%22%3A%22about%3A%22%2C%22host%22%3A%22%22%7D; _okbk=cd4%3Dtrue%2Cvi5%3D0%2Cvi4%3D1678428530031%2Cvi3%3Dactive%2Cvi2%3Dfalse%2Cvi1%3Dfalse%2Ccd8%3Dchat%2Ccd6%3D0%2Ccd5%3Daway%2Ccd3%3Dfalse%2Ccd2%3D0%2Ccd1%3D0%2C; _ok=1441-802-10-6072; __atuvc=3%7C6%2C4%7C7%2C0%7C8%2C0%7C9%2C32%7C10; __atuvs=640ac96ffd4a241a003; _oklv=1678428539630%2CKnxSKqLi0RSqdtxs276LI0I60SAbBaAo; useragent=TW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEwOS4wLjAuMCBTYWZhcmkvNTM3LjM2; _uafec=Mozilla%2F5.0%20(Windows%20NT%2010.0%3B%20Win64%3B%20x64)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F109.0.0.0%20Safari%2F537.36; ";

#https://www.sonuker.com/
$ckc="_ga=GA1.2.1569672957.1672478432; shopmagic_visitor_68b2373c8d69e044f700781a2b74fbdc=%7B%22meta%22%3A%5B%5D%2C%22hash%22%3A%220cd8a5ee3f27f4c6a0137cde7088a340%22%7D; cookieaccepted=1; _gid=GA1.2.861368689.1678428556; _gat_gtag_UA_18712495_27=1; PHPSESSID=ff5aed9dbd551ec3a674a8beb456548c; __atuvc=3%7C6%2C4%7C7%2C0%7C8%2C0%7C9%2C22%7C10; __atuvs=640ac98d122737b5003; useragent=TW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEwOS4wLjAuMCBTYWZhcmkvNTM3LjM2; _uafec=Mozilla%2F5.0%20(Windows%20NT%2010.0%3B%20Win64%3B%20x64)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F109.0.0.0%20Safari%2F537.36; ";

function chay($loai,$ck){

$tsm=[
"Host:www.".$loai.".com",
"user-agent:Mozilla/5.0 (Linux; Android 10; Active 3 Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5359.128 Mobile Safari/537.36",
"cookie:$ck",
];

while(1){

$check=get("https://www.".$loai.".com/members-area/",$tsm);
$plan=explode('</a>',explode('<a class="btn btn-unavailable btn-pt" role="button" href="javascript: void(0);">',$check)[1])[0];

#$substring="No Plan Activated";
#if(strpos($check, $substring)==true){echo "Chưa có buff\n";
if($plan=="Activated"){
	echo "$loai | Bạn đã buff trước đó rồi!!!\n";
	break;
}

$h=0;

$active=get("https://www.".$loai.".com/members-area/activate/",$tsm);

$value=explode('";',explode('var subscribers  = "',$active)[1])[0];
$channel=explode('";',explode('var channel      = "',$active)[1])[0];
$id=explode('";',explode('var videoId      = "',$active)[1])[0];

$link=explode('",',explode('url: "',$active)[1])[0];


if($value=="" or $channel=="" or $id=="" or $link==""){exit("cookie die");}

#echo "$value | $id | $channel | $link\n";

$tsm1=[
"Host:www.".$loai.".com",
"content-length:74",
"application/x-www-form-urlencoded; charset=UTF-8",
"Mozilla/5.0 (Linux; Android 10; Active 3 Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5359.128 Mobile Safari/537.36",
"cookie:$ck",
];

for($i=20;$i>-1;$i--){$mau=rand(0,7);echo "\033[1;3".$mau."mĐợi $i giây      \r"; sleep(1);}

$data="subscribers=$value&channel=$channel&videoId=$id";

$nhan=post($link,$tsm1,$data);

$h++;

if($nhan['status']=="success"){
echo "$h | $loai | $id | $channel \n";
}
if($nhan['status']=="activated"){
echo "Đã hết lượt rồi\n";
break;}

}

}



chay("subpals",$cka);

echo "----------------------------\n";

chay("ytpals",$ckb);

echo "----------------------------\n";

chay("sonuker",$ckc);

echo "----------------------------\n";


for($i=43300;$i>-1;$i--){$mau=rand(0,7);echo "\033[1;3".$mau."mĐợi $i giây      \r"; sleep(1);}


