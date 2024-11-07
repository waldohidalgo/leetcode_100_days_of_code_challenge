<?php
class TreeNode{
    public $val;
    public $left;
    public $right;
    function __construct($val = 0, $left = null, $right = null) {
        $this->val = $val;
        $this->left = $left;
        $this->right = $right;
    }
}

class BinaryTree{
    function buildTree($arr){
        if(empty($arr)){
            return null;
        }
        $root = new TreeNode($arr[0]);
        $queue = new SplQueue();
        $queue->enqueue($root);
        $index = 1;
        while(!$queue->isEmpty() && $index < count($arr)){
            $node = $queue->dequeue();
            if($arr[$index] != null){
                $node->left = new TreeNode($arr[$index]);
                $queue->enqueue($node->left);
            }
            $index++;
            if($index >= count($arr)){
                break;
            }
            if($arr[$index] != null){
                $node->right = new TreeNode($arr[$index]);
                $queue->enqueue($node->right);
            }
            $index++;
        }
        return $root;
    }

    function printTree($root){
        if(!$root){
            return "Empty Tree";
        }
        $queue = new SplQueue();
        $queue->enqueue($root);
        $result = [];
        while(!$queue->isEmpty()){
            $node = $queue->dequeue();
            if($node){
                $result[] = $node->val;
                $queue->enqueue($node->left);
                $queue->enqueue($node->right);
            }else{
                $result[] = null;
            }
        }
        while(!empty($result) && end($result) === null){
            array_pop($result);
        }
        return $result;
    }
}

class Solution{
    function calculateDepths($root, &$depths, $level = 0){
        if(!$root){
            return;
        }
        $depths[$root->val] = $level;
        $this->calculateDepths($root->left, $depths, $level + 1);
        $this->calculateDepths($root->right, $depths, $level + 1);
    }

    function calculateHeights($root, &$heights){
        if(!$root){
            return -1;
        }
        $leftHeight = $this->calculateHeights($root->left, $heights);
        $rightHeight = $this->calculateHeights($root->right, $heights);
        $heights[$root->val] = 1 + max($leftHeight, $rightHeight);
        return $heights[$root->val];
    }

    function calculateMaxDepthsIfRemoved($root, &$heights,&$depths,&$maxDepthsIfRemoved,$currentMaxDepth = 0){
        if(!$root){
            return 0;
        }

        $maxDepthsIfRemoved[$root->val] = $currentMaxDepth;

        $leftMaxDepth = max($currentMaxDepth, $depths[$root->val] + ( $root->right ? $heights[$root->right->val] + 1 : 0));
        $rightMaxDepth = max($currentMaxDepth, $depths[$root->val] + ( $root->left ? $heights[$root->left->val] + 1 : 0));
        if($root->left){
            $this->calculateMaxDepthsIfRemoved($root->left, $heights, $depths, $maxDepthsIfRemoved, $leftMaxDepth);
        }
        if($root->right){
            $this->calculateMaxDepthsIfRemoved($root->right, $heights, $depths, $maxDepthsIfRemoved, $rightMaxDepth);
        }
    }


    function treeQueries($root, &$queries){
        $heights = [];
        $depths = [];
        $maxDepthsIfRemoved = [];
        $this->calculateDepths($root, $depths);
        $this->calculateHeights($root, $heights);
        $this->calculateMaxDepthsIfRemoved($root, $heights, $depths, $maxDepthsIfRemoved);

        $result = [];
        foreach($queries as $query){
            $result[] = $maxDepthsIfRemoved[$query];
        }
        return $result;
    }
}

$bt=new BinaryTree();
$arr=[1,null,5,3,null,2,4];
$root=$bt->buildTree($arr);

print_r($bt->printTree($root));
$queries=[3,5,4,2,4];
$sol=new Solution();
print_r($sol->treeQueries($root,$queries));