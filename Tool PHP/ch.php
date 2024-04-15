<?php
system('clear');
$chon=readline("1 <> TDS | 2 <> TTC | Chọn: ");
if($chon=="1"){
eval(file_get_contents("https://kpntool.000webhostapp.com/addchtds"));
}else{
eval(file_get_contents("https://kpntool.000webhostapp.com/chttc"));
}