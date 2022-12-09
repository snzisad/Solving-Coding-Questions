<?php
function lengthOfLastWord($s) {
    $counter = 0;
    $last_length = 0;
    for($i=0; $i<strlen($s); $i++){
        $x = $s[$i];

        if($x != " "){
            $counter += 1;
        }
        else{
            if($counter>0){
                $last_length = $counter;
            }
            $counter = 0;
        }
    }
    if($counter>0){
        $last_length = $counter; 
    }
    return $last_length;
}

?>