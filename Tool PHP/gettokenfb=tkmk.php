<?php
$tk="";
$mk="";
$curl = curl_init();
    curl_setopt_array($curl, array(
    CURLOPT_URL => 'https://graph.facebook.com/auth/login',
    CURLOPT_RETURNTRANSFER => true,
    CURLOPT_ENCODING => '',
    CURLOPT_MAXREDIRS => 10,
    CURLOPT_TIMEOUT => 0,
    CURLOPT_FOLLOWLOCATION => true,
    CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
    CURLOPT_CUSTOMREQUEST => 'POST',
    CURLOPT_POSTFIELDS =>'{"locale":"vi_VN","format":"json","email":"'.$tk.'","password":"'.$mk.'","access_token":"350685531728|62f8ce9f74b12f84c123cc23437a4a32","generate_session_cookies":true}',
    CURLOPT_HTTPHEADER => array(
    'User-Agent: Dalvik/2.1.0 (Linux; U; Android 12; M2101K7BG Build/SP1A.210812.016) [FBAN/MobileAdsManagerAndroid;FBAV/303.0.0.28.104;FBBV/413414122;FBRV/0;FBLC/vi_VN;FBMF/Xiaomi;FBBD/Redmi;FBDV/M2101K7BG;FBSV/12;FBCA/arm64-v8a:armeabi-v7a:armeabi;FBDM/{density=2.75,width=1080,height=2263};FB_FW/1;]',
    'Content-Type: application/json'
    ),
    ));  
    $response = curl_exec($curl);
    curl_close($curl);
    print_r($response);