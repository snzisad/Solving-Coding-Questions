<?php 
function longestCommonPrefix($strs) {
    $x = "";
    
    if(count($strs) <= 0){
        return $x;
    }
        
    $s = $strs[0];

    for($i=0; $i<strlen($s); $i++){
        $x = $x.$s[$i];

        for($j=1; $j<count($strs); $j++){
            if(!str_starts_with($strs[$j], $x)){
                return substr($x, 0, -1);
            }
        }
    }

    return $x;
}

print(longestCommonPrefix(["flower","flow","flight"]))

?>