<?php

function plusOne($digits) {
    $new_digits = [];
    $additional = 1;
    for($i=count($digits)-1; $i>=0; $i--){
        $val_sum = $digits[$i]+$additional;
        if($val_sum>9){
            array_unshift($new_digits, 0);
            $additional = 1;
        }
        else{
            array_unshift($new_digits, $val_sum);
            $additional = 0;
        }
    }
    if($additional>0){
        array_unshift($new_digits, $additional);
    }

    return $new_digits;  
}

print(plusOne([1, 2, 3]));
?>