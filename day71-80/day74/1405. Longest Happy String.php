<?php
class Solution {
    /**
     * @param Integer $a
     * @param Integer $b
     * @param Integer $c
     * @return String
     */
    function longestDiverseString($a, $b, $c) {
        $heap = new SplPriorityQueue();

        if ($a > 0) {
            $heap->insert(['char' => 'a', 'freq' => $a], $a);
        }
        if ($b > 0) {
            $heap->insert(['char' => 'b', 'freq' => $b], $b);
        }
        if ($c > 0) {
            $heap->insert(['char' => 'c', 'freq' => $c], $c);
        }

        $result = "";

        while (!$heap->isEmpty()) {
            $current = $heap->extract();  
            $char1 = $current['char'];
            $freq1 = $current['freq'];

            if (strlen($result) >= 2 && $result[-1] == $result[-2] && $result[-1] == $char1) {
                if ($heap->isEmpty()) {
                    break;
                }
                
                $next = $heap->extract();
                $char2 = $next['char'];
                $freq2 = $next['freq'];
                
                $result .= $char2;
 
                if ($freq2 > 1) {
                    $heap->insert(['char' => $char2, 'freq' => $freq2 - 1], $freq2 - 1);
                }
                
                $heap->insert(['char' => $char1, 'freq' => $freq1], $freq1);
            } else {
                
                $result .= $char1;

                if ($freq1 > 1) {
                    $heap->insert(['char' => $char1, 'freq' => $freq1 - 1], $freq1 - 1);
                }
            }
        }
        return $result;
    }
}

$solution = new Solution();
echo $solution->longestDiverseString(7, 1, 0);  

