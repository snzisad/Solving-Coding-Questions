<?php
function isValid($s) {
    if(strlen($s) == 0)
        return true;
    else if(strlen($s)%2 == 1)
        return false;

    $brac = ['(', '{', '['];
    $brac_closed =[ ')', '}', ']'];

    $a = [];

    for($i=0; $i<strlen($s); $i++){
        $x = $s[$i];

        if(in_array($x, $brac)){    
            array_push($a, array_search($x, $brac));
        }
        else if(count($a)>0 && end($a) == array_search($x, $brac_closed)){
            $a = array_slice($a, 0, -1);
        }
        else{
            return false;
        }
    }
    if(count($a)>0){
        return false;
    }
    return true;
}

print(isValid("()[]{}"));

?>