<?php
function romanToInt($s) {  
    $r = ['I', 'V', 'X', 'L', 'C', 'D', 'M'];
    $m = [1, 5, 10, 50, 100, 500, 1000];

    $y = 0;
    $i = 0;

    while ($i<strlen($s)){
        $x = $s[$i];
        $pos = array_search($s[$i], $r);

        if($i == strlen($s)-1){
            $y = $y+$m[$pos];
            break;
        }
        else{
            $pos2 = array_search($s[$i + 1], $r);
            

            if(($pos == 0 && ($pos2 == 1 || $pos2 == 2)) || ($pos == 2 && ($pos2 == 3 || $pos2 == 4)) || ($pos == 4 && ($pos2 == 5 || $pos2 == 6))){
                $y = $y + ($m[$pos2] - $m[$pos]);
                $i = $i+2;
            }
            else{
                $y = $y + $m[$pos]; 
                $i = $i+1;
            }
        }

    }
    return $y;
}

print(romanToInt("LVIII"))

?>