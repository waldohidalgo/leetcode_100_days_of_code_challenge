<?php

class Solution {

    /**
     * @param Integer[][] $grid
     * @return Integer
     */
    function maxMoves($grid) {
        $m = count($grid);
        $n = count($grid[0]);
        
        $memo = array_fill(0, $m, array_fill(0, $n, -1));
        $directions = [[-1, 1], [0, 1], [1, 1]];
        $dfs = function($i, $j) use (&$grid,$directions, $m, $n, &$memo, &$dfs) {
            if ($memo[$i][$j] != -1) {
                return $memo[$i][$j];
            }
            
            $max_moves = 0;
            foreach ($directions as $direction) {
                $ni = $i + $direction[0];
                $nj = $j + $direction[1];
                
                if ($ni >= 0 && $ni < $m && $nj < $n && $grid[$ni][$nj] > $grid[$i][$j]) {
                    $max_moves = max($max_moves, 1 + $dfs($ni, $nj));
                }
            }
            
            return $memo[$i][$j] = $max_moves;
        };
        
        return max(array_map(function($i) use ($dfs) {
            return $dfs($i, 0);
        }, range(0, $m - 1)));
    }
}


$sol=new Solution();
$grid = [[2,4,3,5],[5,4,9,3],[3,4,2,11],[10,9,13,15]];

print_r($sol->maxMoves($grid));