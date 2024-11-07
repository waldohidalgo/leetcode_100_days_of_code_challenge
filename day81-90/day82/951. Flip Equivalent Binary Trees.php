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

    public function printTree($root) {
        if (!$root) {
            return "Empty Tree";
        }

        $queue = new SplQueue();
        $queue->enqueue($root);
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



class Solution{
    /**
     * @param TreeNode $root1
     * @param TreeNode $root2
     * @return Boolean
     */
    function flipEquiv($root1, $root2) {
        if (!$root1 && !$root2) {
            return true;
        }
        if (!$root1 || !$root2) {
            return false;
        }
        if ($root1->val != $root2->val) {
            return false;
        }
        return (
            $this->flipEquiv($root1->left, $root2->right) && $this->flipEquiv($root1->right, $root2->left) 
            || 
            $this->flipEquiv($root1->left, $root2->left) && $this->flipEquiv($root1->right, $root2->right));
    }
}

$binaryTree=new BinaryTree();
$root1=$binaryTree->buildTree([1,2,3,4,5,6,null,null,null,7,8]);
$root2=$binaryTree->buildTree([1,3,2,null,6,4,5,null,null,null,null,8,7]);
$solution=new Solution();
print($solution->flipEquiv($root1,$root2));