<?php
$cookie = "YSC=OhqGbOzQ26M;VISITOR_INFO1_LIVE=3Il3j7ITR0o;PREF=f4=4000000;HSID=A_xGgCIFHDocOSbkc;SSID=AjaTFCjlbbvRRRQHJ;APISID=cRwpnffswF6bkYhy/AHBQKauFqrcR6uQCc;SAPISID=FFMeGf5SOnvVZp5E/AVI1mvX2ADyb_SoR4;__Secure-1PAPISID=FFMeGf5SOnvVZp5E/AVI1mvX2ADyb_SoR4;__Secure-3PAPISID=FFMeGf5SOnvVZp5E/AVI1mvX2ADyb_SoR4;SID=MAgo0wkledvBS5puh6rxi-n9fqcLGfMeSaFD8_JNLaZF0TlBv-A5quDwGV_DFv6NQrULVg.;__Secure-1PSID=MAgo0wkledvBS5puh6rxi-n9fqcLGfMeSaFD8_JNLaZF0TlBEio6YQIcWUMcNISKD-45sA.;__Secure-3PSID=MAgo0wkledvBS5puh6rxi-n9fqcLGfMeSaFD8_JNLaZF0TlBiWBN_U3GHcMlFRbtf8szvw.;LOGIN_INFO=AFmmF2swRQIhAMgIpi63HnWydd57kIdkKYwT03fv9kW9qVurHsk84UAvAiBgAX5xo3zVi4frvf0lsKa7mCig7WNw79jA0jTnot1rWg:QUQ3MjNmejd4NG1UUl92OGNNemUwdDRMUmd5NmVieDIyc09sNUdVb08xQ01TYXZnZUpEcFM5OXctdklTMkoxUW9LaE4zUURPWG5RakNLcWhiUDdZdEx5MTBsODJ4OUpEc0ZaUEhqTzRvMkl0TU5TZkZLaW5vd21XdjRtMmdhcXBRblowdXIxRk1xY1NyZVhxREpSdVBDc3RqTmRkaEZoMW93;SIDCC=AJi4QfEQOIOlxW8pKiYJRHiLbTGM-VnSZ0G-UtfVuBbeCKmBrcltsDk15QmfwN-wyBQ69TkG;__Secure-1PSIDCC=AJi4QfGiqIqQQ_-XlwwhGp2Eute5ibU33bXVG5T7ACruNZJ8v9ogTEQcBZew1YQa4joamP3D;__Secure-3PSIDCC=AJi4QfF6N-8tXJJdFT23sHjbhT0B9BQNOMqWuS8yYX_hOi8o7ASQZRNkvBAcoSkeaTRkB0Ac3w";
$authorization = 'SAPISIDHASH 1657339663_e5e960c92dd15b66063270b13971ef67577e1b1b';
    $head_g = ["user-agent:Mozilla/5.0 (Linux; Android 9; RMX1811) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Mobile Safari/537.36", "cookie: " . $cookie];
 while(true){
    $ch = curl_init();
    curl_setopt_array($ch, array(
        CURLOPT_URL => "https://m.youtube.com/feed/channels",
        CURLOPT_FOLLOWLOCATION => false,
        CURLOPT_RETURNTRANSFER => 1,
        CURLOPT_POST => 1,
        CURLOPT_HTTPGET => true,
        CURLOPT_SSL_VERIFYPEER => 0,
        CURLOPT_HTTPHEADER => $head_g,
        CURLOPT_ENCODING => true
    ));
    $dlg = curl_exec($ch);
    curl_close($ch);

#$idcn = explode('\x22,\x22webPageType\x',explode('x22url\x22:\x22\/channel\/',$dlg)[1])[0];
$idcn = explode('\x22',explode('\x22channelId\x22:\x22',$dlg)[1])[0];

$url = 'https://m.youtube.com/channel/'.$idcn;
if (!$idcn){
die("đã hủy hết kênh \n");
}
print_r("id: ". $idcn."\n");
  $dpl =  unsubscribe($url, $cookie, $authorization);
if ($dpl['kpb-status']){
print_r("msg: ".$dpl["SUBSCRIBE"]."\n");
 } else {
 print_r("msg: error \n");
 }
 sleep(02);
 }
    
    
    
    
    
    
    
    function unsubscribe($url, $cookie, $authorization)
{
    $ch = curl_init();
    curl_setopt_array($ch, array(
        CURLOPT_URL => "https://api.kpb-fia.com/api/Youtubes.php",
        CURLOPT_FOLLOWLOCATION => false,
        CURLOPT_RETURNTRANSFER => 1,
        CURLOPT_POST => 1,
        CURLOPT_HTTPGET => true,
        CURLOPT_SSL_VERIFYPEER => 0,
        CURLOPT_CUSTOMREQUEST => "POST",
        CURLOPT_POSTFIELDS => [
"TYPE" => "UNSUBSCRIBEJWKEJDKSHS",
"LINK-CHANNEL" => "$url",
"COOKIE" => "$cookie",
"AUTHORIZATION" => "$authorization"
],
        CURLOPT_HTTPHEADER => ['Host:api.kpb-fia.com',
        'User-Agent:Mozilla/5.0 (Linux; Android 9; RMX1811) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36',
        'Accept:image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8'],
        CURLOPT_ENCODING => true
    ));
    $BA = curl_exec($ch);
    return json_decode($BA,true);
}
    
    
    