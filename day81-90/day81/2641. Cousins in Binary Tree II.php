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

class BinaryTree {
    public $root;

    public function __construct($arr) {
        $this->root = $this->buildTree($arr);
    }

    public function buildTree($arr) {
        if (empty($arr)) {
            return null;
        }

        $root = new TreeNode($arr[0]);
        $queue = new SplQueue();
        $queue->enqueue($root);
        $index = 1;

        while (!$queue->isEmpty() && $index < count($arr)) {
            $node = $queue->dequeue();

            
            if ($arr[$index] !== null) {
                $node->left = new TreeNode($arr[$index]);
                $queue->enqueue($node->left);
            }
            $index++;

            if ($index >= count($arr)) {
                break;
            }

            
            if ($arr[$index] !== null) {
                $node->right = new TreeNode($arr[$index]);
                $queue->enqueue($node->right);
            }
            $index++;
        }

        return $root;
    }

    public function printTree() {
        if (!$this->root) {
            return "Empty Tree";
        }

        $queue = new SplQueue();
        $queue->enqueue($this->root);
        $result = [];

        while (!$queue->isEmpty()) {
            $node = $queue->dequeue();
            if ($node) {
                $result[] = $node->val;
                $queue->enqueue($node->left);
                $queue->enqueue($node->right);
            } else {
                $result[] = null;
            }
        }

        
        while (!empty($result) && end($result) === null) {
            array_pop($result);
        }

        return $result;
    }
}

class Solution {
    public function replaceValueInTree($root) {
        if (!$root) {
            return null;
        }

        $queue = new SplQueue();
        $queue->enqueue($root);
        $root->val = 0;  

        while (!$queue->isEmpty()) {
            $levelSum = 0;
            $siblingsMap = [];

            
            $levelSize = $queue->count();
            for ($i = 0; $i < $levelSize; $i++) {
                $node = $queue->dequeue();
                $siblingsMap[] = [$node->left, $node->right];  

                if ($node->left) {
                    $levelSum += $node->left->val;
                    $queue->enqueue($node->left);
                }
                if ($node->right) {
                    $levelSum += $node->right->val;
                    $queue->enqueue($node->right);
                }
            }

            
            foreach ($siblingsMap as [$left, $right]) {
                $siblingSum = 0;
                if ($left) {
                    $siblingSum += $left->val;
                }
                if ($right) {
                    $siblingSum += $right->val;
                }

                if ($left) {
                    $left->val = $levelSum - $siblingSum;  
                }
                if ($right) {
                    $right->val = $levelSum - $siblingSum;  
                }
            }
        }

        return $root;
    }
}


$binaryTree = new BinaryTree([5,4,9,1,10,null,7]);
#$binaryTree->printTree();
$sol=new Solution();
$sol->replaceValueInTree($binaryTree->root);
print_r($binaryTree->printTree());