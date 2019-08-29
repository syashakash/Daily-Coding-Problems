'''
27 08 2019
This problem was asked by Airbnb.

Given a list of integers, write a function that returns the 
largest sum of non-adjacent numbers. Numbers can be 0 or negative.

For example, [2, 4, 6, 2, 5] should return 13, 
since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.

Follow-up: Can you do this in O(N) time and constant space?
'''
# def maxSumForNonAdjacent(alist):
#     n = len(alist)
#     dp = [alist[i] for i in range(n)]
#     if n == 0:
#         return 0
#     elif n == 1:
#         return alist[0]
#     elif n == 2:
#         return max(alist[0],alist[1])
#     dp[1] = max(alist[0], alist[1])
#     for i in range(2, n):
#         dp[i] = max(dp[i], max(dp[i-2] + alist[i], dp[i-1]))
#     return dp[-1]

def maxSumForNonAdjacent(alist):
    n = len(alist)
    #dp = [alist[i] for i in range(n)]
    if n == 0:
        return 0
    elif n == 1:
        return alist[0]
    elif n == 2:
        return max(alist[0],alist[1])
    alist[1] = max(alist[0], alist[1])
    for i in range(2, n):
        alist[i] = max(alist[i], max(alist[i-2] + alist[i], alist[i-1]))
    return alist[-1]

# def kadane(alist):
#     maxSumSoFar, maxEndingHere = alist[0], alist[0]
#     for i in range(1, len(alist)):
#         maxEndingHere+=alist[i]
#         if maxEndingHere < 0:
#             maxEndingHere=0
#         maxSumSoFar=max(maxSumSoFar, maxEndingHere)
#     return maxSumSoFar

def main():
    t = int(input("Enter testcases : "))
    while t > 0:
        alist = [int(i) for i in input("Enter list : ").split()]
        print(maxSumForNonAdjacent(alist))
        t-=1

if __name__ == "__main__":
    main()
