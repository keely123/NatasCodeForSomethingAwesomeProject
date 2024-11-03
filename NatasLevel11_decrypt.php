<!DOCTYPE html>
<html>
<body>
 
<?php

$x = base64_decode('HmYkBwozJw4WNyAAFyB1VUcqOE1JZjUIBis7ABdmbU1GIjEJVCJlTRg');

function xor_encrypt($x) {
    $key = json_encode(array( "showpassword"=>"no", "bgcolor"=>"#ffffff"));
    $text = $x;
    $outText = '';

    // Iterate through each character
    for($i=0;$i<strlen($text);$i++) {
    $outText .= $text[$i] ^ $key[$i % strlen($key)];
    }

    return $outText;
}

$tempdata = json_encode(xor_encrypt($x, true));

print xor_encrypt($x);

?>



</body>
</html>