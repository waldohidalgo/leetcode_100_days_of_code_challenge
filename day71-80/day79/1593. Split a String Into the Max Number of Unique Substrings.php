<?php

class Solution {
    private $maxLength = 1;
    private function backtrack($i, $s, &$seen) {
        if ($i == strlen($s)) {
            $this->maxLength = max($this->maxLength, count($seen));
            return;
        }
        for ($j = $i + 1; $j <= strlen($s); $j++) {
            $substring = substr($s, $i, $j - $i);
            if (in_array($substring, $seen)) {
                continue;
            }
            $seen[] = $substring;
            $this->backtrack($j, $s, $seen);
            array_pop($seen);
        }
    }

    public function maxUniqueSplit($s) {
        $seen = array();  
        $this->backtrack(0, $s, $seen);  
        return $this->maxLength;  
    }
}


$solution = new Solution();
echo $solution->maxUniqueSplit("ababccc");  
