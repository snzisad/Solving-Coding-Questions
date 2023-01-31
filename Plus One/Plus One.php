<?php

function plusOne($digits) {
    $new_digits = [];
    $carry = 1;
    for($i=count($digits)-1; $i>=0; $i--){
        $val_sum = $digits[$i]+$carry;
        if($val_sum>9){
            array_unshift($new_digits, 0);
            $carry = 1;
        }
        else{
            array_unshift($new_digits, $val_sum);
            $carry = 0;
        }
    }
    if($carry>0){
        array_unshift($new_digits, $carry);
    }

    return $new_digits;  
}

print(plusOne([1, 2, 3]));
?>