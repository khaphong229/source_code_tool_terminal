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

$cka="_ga=GA1.1.1361896543.1692621197; PHPSESSID=5k6psci1e7pjvub0mlcl7q2k41; _pbjs_userid_consent_data=3524755945110770; _pubcid=7c406963-ff05-4e4d-8cfb-ce77d44555fa; _lr_env_src_ats=false; Neustar-Fabrick ID=%7B%22fabrickId%22%3A%22E1%3AAEu4xAgve0OkcEfV-X0UmhsHo4cTF23jxI6ARwN3cJ87boIG_aBYFlORd7a29OsNPhzOL53ROazZ850zaBo5BvAK4l_4khy1iVPgpl1SQFT4GspA_O_NYDI3_gGDbJGZ%22%7D; __cf_bm=JOzcs1ovEtJMOtX8nPss4ss05DMrx1VG80wenYSf8ZE-1692625566-0-AW/gzteyvMSoiog2j4/u72urELDqpQaXHtooNGmhkfmH8zzNHb9SzDDfuV4XvOHJDfQuu3IwuQ1A5aQmw1z/AfE=; __gads=ID=2aaa64bc2b62abd7:T=1692625583:RT=1692625583:S=ALNI_MYOYakKYBDMf0U7tyYsU1LtJrhjhg; __gpi=UID=00000c3057864c87:T=1692625583:RT=1692625583:S=ALNI_MYPmRSuNzKTO2yeDWCNFz4RpwOY4Q; _lr_retry_request=true; cto_bundle=6OO3q18wbm1EZEVHJTJGSVFvVGlNQjJIeU9lU084YVNGbmtEaXNGZXNPSTRuRE9kdGJwUGxPMkVObTl4QUVkd3phYzZaZkV3NzhKSDZob1RRcXpZeiUyQjZ2RWplQnliSHhsOUpZckl1WEhaYXM3M0x4dm83ZjZNelFZa1Y4RGZ6MDZWQ2RVOFJCVFpaR2lnU3dYY3kxbnY4aHl1M3RnJTNEJTNE; cto_bidid=PhTSpF9SYU5JNzIlMkYlMkJYVlNLbmh4Qmt0bEZGVE00a2dwd0J6U2dLWW1hYW56YWg3dkUlMkIyTmdaVjJTM2pHQzB1dGYzNTlyRzhMRkR4QXY4R0EwZ0NvZzltVjZCeFZieFVjMFhOeVJWOUtmZm44RE1CNCUzRA; cto_dna_bundle=x6NDDF8wbm1EZEVHJTJGSVFvVGlNQjJIeU9lU0cxeWNLS2RUNHZTZkJrS3lCblVmQkJLQmY0czUlMkJvMG1LblBJbjR2Y1pzMU9RUE10MVVIREZybVFXV3REQ21Fb3clM0QlM0Q; _ga_6WTH13ELBM=GS1.1.1692625571.2.1.1692625953.0.0.0; useragent=TW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzExNS4wLjAuMCBTYWZhcmkvNTM3LjM2IEVkZy8xMTUuMC4xOTAxLjIwMw%3D%3D; ";

$ckb="PHPSESSID=19t3r3iu952h4qf4usgd2cbjlb; _ga=GA1.1.1955567299.1692621323; hblid=J3feeXgn14LLHoaD276LI0IkaCFbjrB3; _okdetect=%7B%22token%22%3A%2216926213233490%22%2C%22proto%22%3A%22about%3A%22%2C%22host%22%3A%22%22%7D; olfsk=olfsk9989476632891796; _ok=1441-802-10-6072; __cf_bm=JxZNQdwwaX.0_XnydOtV9aGwJ_Tc5zJjB7CS8eIKYAU-1692625854-0-Aahs4Wn0ZBv1VzJSrJzy+mbPvh3iE9kOLCn6mp1z+Ssn6RcLC6a6pa2F7Qc5V/V1jCpTfzEx3p4KI4PIObuVMLo=; paddos_HJxyy=1; wcsid=R3y3E0G1huTp5DVo276LI0I0AoB3Czjr; _okbk=cd4%3Dtrue%2Cvi5%3D0%2Cvi4%3D1692625857159%2Cvi3%3Dactive%2Cvi2%3Dfalse%2Cvi1%3Dfalse%2Ccd8%3Dchat%2Ccd6%3D0%2Ccd5%3Daway%2Ccd3%3Dfalse%2Ccd2%3D0%2Ccd1%3D0%2C; _ga_VWXD5PXED8=GS1.1.1692625856.2.1.1692625888.0.0.0; _oklv=1692625889276%2CR3y3E0G1huTp5DVo276LI0I0AoB3Czjr; useragent=TW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzExNS4wLjAuMCBTYWZhcmkvNTM3LjM2IEVkZy8xMTUuMC4xOTAxLjIwMw%3D%3D; ";
$ckc="_ga=GA1.1.1688622782.1692620808; PHPSESSID=nf6kr71bl2g8ik21ffn4r2ieve; __cf_bm=Wh3gNlYxPf00X_uYv5_.XlUfqfc8fp1C.NbZY2Xt_Kg-1692625911-0-Aa3HJm/nLM8QVEB1wUWb2wm2V7RwPAyprZpn8H+MipsMi8VRVtodUtmsxfXofE6ZAQuH7Cz48CVNXUiOoDsGItU=; _ga_PYT4DLL427=GS1.1.1692625912.2.1.1692625919.0.0.0; useragent=TW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzExNS4wLjAuMCBTYWZhcmkvNTM3LjM2IEVkZy8xMTUuMC4xOTAxLjIwMw%3D%3D; ";

function chay($loai,$ck){
$head=[
"Host:www.$loai.com",
"user-agent:Mozilla/5.0 (Linux; Android 9; SM-S906N Build/PQ3B.190801.08041932) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Mobile Safari/537.36",
"cookie:$ck",
];

while (1){
    $a++;
    $active=get("https://www.$loai.com/members-area/activate/",$head);
    $channel=explode('";',explode('var channel      = "',$active)[1])[0];
    $id=explode('";',explode('var videoId      = "',$active)[1])[0];

    echo "$channel và $id";


    $head_p=[
		"Host:www.$loai.com",
		"content-length:52",
		"content-type:application/x-www-form-urlencoded; charset=UTF-8",
		"user-agent:Mozilla/5.0 (Linux; Android 10; Active 3 Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5359.128 Mobile Safari/537.36",
		"cookie:$ck",
    ];

    for($i=20;$i>-1;$i--){$mau=rand(0,7);echo "\033[1;3".$mau."mĐợi $i giây      \r"; sleep(1);}

    $nhan=post("https://www.$loai.com/members-area/sub-completed-v4.php",$head_p,"channel=$channel&videoId=$id");
    if ($nhan['status']=="success"){
        echo "$h | SUCCESS | $id | $channel \n";
    }
    if($nhan['status']=="activated"){
        echo "Đã hết lượt rồi              \n";
        break;
    }
}
}

while (1){
    chay("subpals",$cka);

	chay("ytpals",$ckb);

	chay("sonuker",$ckc);
}
