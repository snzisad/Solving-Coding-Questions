<?php
    function removeDuplicates(&$nums) {
        $k = 0;
        for($i=0; $i<count($nums); $i++){
            if($nums[$i] != $nums[$k]){
                $k += 1;
                $nums[$k] = $nums[$i];
            }
        }
        return $k+1;
    }

?>