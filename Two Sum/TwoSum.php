<?php

function twoSum($nums, $target) {
    $collection = array();

    foreach($nums as $key => $num) {
        $subtracted = $target - $num;

        if (count($collection)>0 && array_key_exists($subtracted, $collection)) {
            return array($collection[$subtracted], $key);  
        } else {
            $collection[$num] = $key;
        }
    }
}

$nums = [2,7,11,15];
$target = 9;

var_dump (twoSum($nums, $target));

?>


