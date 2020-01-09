'''
This problem was asked by Google.

Given an array of integers and a number k, where 1 <= k <= length of the array, compute the maximum values of each subarray of length k.

For example, given array = [10, 5, 2, 7, 8, 7] and k = 3, we should get: [10, 7, 8, 8], since:

10 = max(10, 5, 2)
7 = max(5, 2, 7)
8 = max(2, 7, 8)
8 = max(7, 8, 7)
Do this in O(n) time and O(k) space. 
You can modify the input array in-place and you do not need to store the results.
You can simply print them out as you compute them.
'''

import heapq

def maxHeapify(aList, i, n):
    left = 2 * i + 1
    right = 2 * i + 2
    largest = i
    if left < n and aList[left] > aList[largest]:
        largest = left
    if right < n and aList[right] > aList[largest]:
        largest = right
    if largest != i:
        aList[largest], aList[i] = aList[i], aList[largest]
        maxHeapify(aList, largest, n)

def buildHeap(aList, n):
    for i in range(0, n//2):
        maxHeapify(aList, i, n)

def search(aList, val):
    for i in range(len(aList)):
        if aList[i] == val:
            return i
    return -1

def deleteNode(aList, val):
    index = search(aList, val)
    if index == -1:
        return
    aList[index], aList[-1] = aList[-1], aList[index]
    aList.pop()
    maxHeapify(aList, index, len(aList))

def insertionOrder(aList, i):
    parent = (i - 1) // 2
    while parent >= 0 and aList[parent] < aList[i]:
        aList[parent], aList[i] = aList[i], aList[parent]
        parent = (parent - 1) // 2
     
def maximumInRange(aList, k):
    ans=[]
    i=0
    heap=[]
    n=len(aList)
    while i < k:
        heap.append(aList[i])
        i+=1
    buildHeap(heap, len(heap))
    print(heap)
    j=0
    while i < n:
        ans.append(heap[0])
        print("on adding max", ans)
        deleteNode(heap, aList[j])
        print("on deleting node", heap)
        heap.append(aList[i])
        i+=1
        j+=1
        insertionOrder(heap, len(heap)-1)
        print("on adding new ", heap)
    ans.append(heap[0])
    return ans



def main():
    t=int(input())
    while t > 0:
        arr = [int(i) for i in input().split()]
        k = int(input())
        ans = maximumInRange(arr, k)
        print(ans)
        t-=1

if __name__=="__main__":
    main()
