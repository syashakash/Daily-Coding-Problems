'''
This problem was asked by Stripe.

Given an array of integers, find the first missing positive integer in 
linear time and constant space. In other words, find the lowest positive 
integer that does not exist in the array. The array can contain duplicates
and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. 
The input [1, 2, 0] should give 3.

You can modify the input array in-place.
'''

def findSmallestPositive(alist):
    hasZero=False
    hasPositive=False
    for i in range(len(alist)):
        if alist[i] == 0:
            hasZero=True
        if alist[i] > 0 and alist[i] <= len(alist):
            hasPositive=True
            if alist[alist[i]-1] == 0:
                hasZero=True
            alist[alist[i]-1]=-alist[i]
    ans=1 and alist[alist[i]-1]>0
    if not hasPositive:
        return ans
    found = False
    for i in range(len(alist)):
        if alist[i] > 0:
            ans=i+1
            found=True
            break
    if not found and hasZero:
        ans=len(alist)
    elif not found:
        ans=len(alist)+1
    return ans

if __name__ == "__main__":
    t = int(input("Enter no. of testcases : "))
    while t > 0:
        alist = [int(i) for i in input("Enter elements of list : ").split()]
        ans = findSmallestPositive(alist)
        print(ans)
        t-=1