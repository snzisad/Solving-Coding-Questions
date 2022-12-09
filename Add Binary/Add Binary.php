<?php


function addBinary($a, $b) {
    $sums = "";
    $carry = 0;

    while($a != "" && $b != ""){
        [$sum1, $carry] = binary_sum((int)$a[-1], (int)$b[-1], $carry);
        $sums = strval($sum1).$sums;
        $a = substr($a, 0, -1);
        $b = substr($b, 0, -1);
    }
    while($a != ""){
        [$sum1, $carry] = binary_sum((int)$a[-1], 0, $carry);
        $sums = strval($sum1).$sums;
        $a = substr($a, 0, -1);
    }
    while($b != ""){
        [$sum1, $carry] = binary_sum(0, (int)$b[-1], $carry);
        $sums = strval($sum1).$sums;
        $b = substr($b, 0, -1);
    }

    if($carry == 1){
        $sums = strval($carry) . $sums;
    }

    return $sums;
}


function binary_sum($a, $b, $carry){
    $sum1 = ($a+$b+$carry);
    if($sum1 <= 1){
        $carry = 0;
    }
    else if($sum1 == 2){
        $sum1 = 0;
        $carry = 1;
    } 
    else if ($sum1 == 3) {
        $sum1 = 1;
        $carry = 1;
    }

    return [$sum1, $carry];
}

print(addBinary("1010", "1011"));
?>