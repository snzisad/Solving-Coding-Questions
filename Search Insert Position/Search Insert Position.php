<?php
    function searchInsert($nums, $target) {
        if($nums[0]>=$target){
            return 0;
        }
        else if(end($nums)<$target){
            return count($nums);
        }

        $start = 0;
        $end = count($nums);

        while(1){
            $mid_pos = (int)(($start+$end)/2);
            if($nums[$mid_pos-1]<$target && $nums[$mid_pos]>=$target){
                return $mid_pos;
            }
            else if($nums[$mid_pos]<$target){
                $start = $mid_pos+1;
            } 
            else {
                $end = $mid_pos - 1;
            }
        }
    }

?>