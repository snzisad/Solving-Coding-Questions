<?php

function climbStairs($n) {
    $cur = 1;
    $pre = 1;
    $temp = 0;

    for ($i = 1; $i<$n; $i++){
        $temp = $cur;
        $cur += $pre;
        $pre = $temp;
    }
        
    return $cur;
}

print(climbStairs(3));

?>