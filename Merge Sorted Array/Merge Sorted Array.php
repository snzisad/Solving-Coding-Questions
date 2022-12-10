<?php

function merge(&$nums1, $m, $nums2, $n) {
    $j = 0;
    $i = 0;
    $num_inserted = 0;
    while($j<$n){
        if($nums1[$i]>=$nums2[$j]){
            $nums1 = array_merge(array_slice($nums1, 0, $i), array($nums2[$j]), array_slice($nums1, $i));
            $j += 1;
            $num_inserted += 1;
        }
        else if($i>=($m+$num_inserted) && $nums1[$i] == 0){
            $nums1[$i] = $nums2[$j];
            $j += 1;
        }
        $i += 1;
    }
    $nums1 = array_slice($nums1, 0, ($m+$n));
}


$nums1 = [4, 0, 0, 0, 0, 0];
$m = 1;
$nums2 = [1,2,3,5,6];
$n = 5;
print(merge($nums1, $m, $nums2, $n))

?>