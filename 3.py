'''
21 08 2019
This problem was asked by Google.

Given the root to a binary tree, implement serialize(root), 
which serializes the tree into a string, and deserialize(s), 
which deserializes the string back into the tree.

For example, given the following Node class

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
The following test should pass:

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
'''

class Node:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def serialize(root):
    vals = []
    def encode(node):
        if node:
            vals.append(str(node.val))
            encode(node.left)
            encode(node.right)
        else:
            vals.append('#')
    encode(root)  
    return ' '.join(vals)

def deserialize(data):
    def decode(vals):
        val = next(vals)
        if val == '#':
            return None
        node = Node(int(val))
        node.left = decode(vals)
        node.right = decode(vals)
        return node
    vals = iter(data.split())
    return decode(vals)

def predorder(root):
    ans = []
    stack = []
    stack.append(root)
    while len(stack) > 0:
        node = stack[-1]
        stack.pop()
        ans.append(node.val)
        if node.right is not None:
            stack.append(node.right)
        if node.left is not None:
            stack.append(node.left)
    return ans

#root = Node('root', Node('left', Node('left.left')), Node('right'))
root = Node(1, Node(2, Node(4), Node(5)), Node(3,None,Node(6)))
string = serialize(root)
print(string)
root = deserialize(string)
print(predorder(root))