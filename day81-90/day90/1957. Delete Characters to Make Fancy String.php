<?php
class Solution {

/**
 * @param String $s
 * @return String
 */
function makeFancyString($s) {
    $length = strlen($s);
    $stack=[];
    for($i=0;$i<$length;$i++){
        $stack_length=count($stack);
        if(
            $stack_length>=2 
                &&
            $stack[$stack_length-2]==$stack[$stack_length-1] 
            &&
            $stack[$stack_length-1]==$s[$i]
            ){
            continue;
        }
        $stack[] = $s[$i];
    }
    return implode('',$stack); 
}
}

$sol=new Solution();
echo ($sol->makeFancyString("aaabaaaaaab"));