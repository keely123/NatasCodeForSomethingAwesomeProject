<!DOCTYPE html>
<html>
<body>
 
<?php

$x = array( "showpassword"=>"yes", "bgcolor"=>"#ffffff");

function xor_encrypt($x) {
    $key = 'eDWo';
    $text = $x;
    $outText = '';

    // Iterate through each character
    for($i=0;$i<strlen($text);$i++) {
    $outText .= $text[$i] ^ $key[$i % strlen($key)];
    }

    return $outText;
}


print base64_encode(xor_encrypt(json_encode($x)));
?>



</body>
</html>