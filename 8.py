'''
26 08 2019
This problem was asked by Google.

A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.

Given the root to a binary tree, count the number of unival subtrees.

For example, the following tree has 5 unival subtrees:

   0
  / \
 1   0
    / \
   1   0
  / \
 1   1
'''
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val=val
        self.left=left
        self.right=right

def getTreesUtil(root):
    if root is None:
        return (0,None)
    elif root.left is None and root.right is None:
        #print("Found one : ", root.val)
        return (1, root.val)
    else:
        leftStree, lval = getTreesUtil(root.left)
        rightStree, rval = getTreesUtil(root.right)
        if lval == root.val and rval == root.val:
            #print("Found here one : ", root.val, leftStree, lval, rightStree, rval)
            return 1 + leftStree + rightStree, lval
        else:
            return (leftStree+rightStree, None)

def getTrees(root):
    if root is None:
        return 0
    elif root.left is None and root.right is None:
        #print("Found one : ", root.val)
        return 1
    else:
        ans,_ = getTreesUtil(root)
        return ans

def main():
    root = TreeNode(0, TreeNode(1, TreeNode(0, TreeNode(1, TreeNode(1), TreeNode(1)), TreeNode(0))), TreeNode(0, TreeNode(1, TreeNode(1), TreeNode(1)), TreeNode(0)))
    ans = getTrees(root)
    print(ans)

if __name__=="__main__":
    main()