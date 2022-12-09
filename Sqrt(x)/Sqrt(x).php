<?php

function mySqrt($x) {
    $left = 0;
    $right = $x;
    
    while($left<=$right){
        $mid = (int)(($right + $left)/2);
        $sqr = $mid*$mid;
        
        if($sqr>$x){
            $right = $mid-1;
        }
        else if($sqr<$x){
            $left = $mid+1;
        }
        else{
            return $mid;
        }
    }
    return $right;       
}

print(mySqrt(9));

?>