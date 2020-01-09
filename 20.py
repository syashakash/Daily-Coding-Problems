'''
This problem was asked by Google.

Given two singly linked lists that intersect at some point, find the intersecting node. The lists are non-cyclical.

For example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10, return the node with value 8.

In this example, assume nodes with the same value are the exact same node objects.

Do this in O(M + N) time (where M and N are the lengths of the lists) and constant space.
'''
class ListNode:
    def __init__(self, val):
        self.next=None
        self.val=val

def insert(root, val):
    newNode = ListNode(val)
    newNode.next = root
    return newNode

def getIntersection(A, B):
    if A is None or B is None:
        return None
    n, m = 0, 0
    temp = A
    while temp is not None:
        temp = temp.next
        n+=1
    temp = B
    while temp is not None:
        temp = temp.next
        m+=1
    if n < m:
        A, B = B, A
        n, m = m, n
    tempA = A
    tempB = B
    while n > m:
        tempA = tempA.next
        n-=1
    while tempA is not None and tempB is not None and tempA.val != tempB.val:
        tempA = tempA.next
        tempB = tempB.next
    if (tempA is None or tempB is None) or (tempA.val != tempB.val):
        return -1
    else:
        return tempA.val
        
    
def main():
    t = int(input())
    while t > 0:
        root1 = None
        arr = [int(i) for i in input().split()]
        for a in arr:
            root1=insert(root1, a)
        root2 = None
        arr = [int(i) for i in input().split()]
        for a in arr:
            root2 = insert(root2, a)
        ans = getIntersection(root1, root2)
        print(ans)
        t-=1

if __name__ == "__main__":
    main()