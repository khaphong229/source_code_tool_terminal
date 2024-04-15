<?php 

////////////

//@system("clear");
error_reporting(1);

/////////////
function GET($host,$tsm)
{
$mr = curl_init();
curl_setopt_array($mr, array(
CURLOPT_URL => $host,
///CURLOPT_HEADER => true,
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

/////////////
$ck="cf_clearance=lnP_63kO9l.o1JYCI708YliWfMIfO5BIcp9.zJ7ys1w-1693118382-0-1-9ce20b05.6bf8d98f.4acfd085-0.2.1693118382; apikey=W86YkuVMYyzvyAtdGyEuXerASCgx2HQ9TPhnCml1GuxofEaEcHVIeqYsh; username=3743405055244215559; money=50; __gads=ID=e77c97b09d7906cb-22a7d27cb6e3007e:T=1693118381:RT=1693118880:S=ALNI_Mb-qSKPiUh6kPIBKNYlDPDEia3eLw; __gpi=UID=00000c3437a7a335:T=1693118381:RT=1693118880:S=ALNI_MZ7E9zSefS_MxDeGejYbc3FBA4WrQ; urlsdt=/momo; XSRF-TOKEN=eyJpdiI6IjkzcGpIa0wySVFUR3B5OGJla3d1QUE9PSIsInZhbHVlIjoiczlLWGd4dVpvcHFNZ25VS3lWSlVmelpwSFNHRDYyR3RIK1A3TndKaU4xN1pTNXhnSmJnNGNtMHllbkZFQUxxTUFOaFBKTnBPcTUxaUV3cnUyNEtxN2tTZG9tY0NzR01LcWRvYkpreXB3SDRDWFhuVmdRL2tjRnNPQVNYdzVlZFEiLCJtYWMiOiIzODRhMTdhNzRkMDljYWZlNjQ1ZjYxZmM0YTZiNzYxMzA2MDJkNDM5ODlmYTA4ZWJkY2YyZmUwY2I1OTQ5MWY2IiwidGFnIjoiIn0%3D; laravel_session=eyJpdiI6IkZIcVE0TnBsZGZrRVI3emNXeFp1Y3c9PSIsInZhbHVlIjoiSkJOSng3MCtXYXRMNUFvNUdiWktxRmljWHNNTnp0bHRYSkF5emxqZ3hqbXU4OGprUTAxcGZ3TWNEUWFQRUI4OENvQmYvZ3VQaHJHOHBpWlhPN0xUdG50V0VsNE0wNU51ell5a0FTbk5YK0xIUVpsUDMxT3hIUmU1WFB6TVlzVnEiLCJtYWMiOiIyYzFlOGYwZjAxMjQ1NGZjOGU5OTg1YzVmZmY4NDg2Y2E2NzQ2ODIxNTJhMjk1MTUyNTA1ODM2ZDBlM2U4MDdmIiwidGFnIjoiIn0%3D";

///////////////////
$tsm=array(
"vip.hust.media",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.62",
"cookie:$ck",
);


////////////////

$in4=get("https://vip.hust.media/profile?=key=",$tsm);

print_r($in4);










