'''
This problem was asked by Uber.

Given an array of integers, return a new array such that each element at index i of 
the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. 
If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?
'''

def solve(alist):
    n = len(alist)
    left = [1] * n
    right = [1] * n
    for i in range(1,n):
        left[i] = left[i-1] * alist[i-1]
    for i in range(n-2,-1,-1):
        right[i] = right[i+1] * alist[i+1]
    ans=[1] * n
    for i in range(n):
        if i == 0:
            ans[i] = right[i]
        elif i == n-1:
            ans[i] = left[i]
        else:
            ans[i] = left[i] * right[i]
    return ans


if __name__ == "__main__":
    t = int(input("Enter test cases : "))
    while t > 0:
        alist = [int(i) for i in input("Enter List : ").strip().split()]
        alist = solve(alist)
        print(alist)
        t-=1