<?php

function isPalindrome($x) {
    if ($x<0)
        return false;
    if ($x == 0)
        return true;
    $x = strval($x);
    $i = 0;
    $j = strlen($x)-1;

    while ($i < $j) {
        if ($x[$i] != $x[$j]) {
            return false;
        }
        $i += 1;
        $j -= 1;
    }
    return true;
        
}

print(isPalindrome(10));

?>