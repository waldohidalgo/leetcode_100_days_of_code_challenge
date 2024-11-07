<?php

class TreeNode {
    public $val;
    public $left;
    public $right;

    public function __construct($val = 0, $left = null, $right = null) {
        $this->val = $val;
        $this->left = $left;
        $this->right = $right;
    }
}

class MinHeap extends SplPriorityQueue {
    public function compare(mixed $a, mixed $b): int {
        return $b - $a; 
    }
}
class Solution {
    public function kthLargestLevelSum($root, $k) {
        if ($root === null) {
            return -1; 
        }

        $queue = new SplQueue();
        $queue->enqueue($root);

        $minHeap = new SplPriorityQueue();

        while (!$queue->isEmpty()) {
            $levelSum = 0;
            $size = $queue->count(); 

            for ($i = 0; $i < $size; $i++) {
                $node = $queue->dequeue(); 
                $levelSum += $node->val;   
 
                if ($node->left !== null) {
                    $queue->enqueue($node->left);
                }
                if ($node->right !== null) {
                    $queue->enqueue($node->right);
                }
            }
  
            if ($minHeap->count() < $k) {
                $minHeap->insert($levelSum, $levelSum);
            }  
            else if ($levelSum > $minHeap->top()) {
                $minHeap->extract(); 
                $minHeap->insert($levelSum, $levelSum); 
            }
        }
        return $minHeap->count() < $k ? -1 : $minHeap->top();
    }
}


$root = new TreeNode(1, new TreeNode(2), new TreeNode(3));
$solution = new Solution();
echo $solution->kthLargestLevelSum($root, 2);
