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
    def segregate(alist):
        i,j=0,0
        while j < len(alist):
            if alist[j] <= 0:
                alist[i],alist[j]=alist[j],alist[i]
                i+=1
            j+=1
        return i
    shift = segregate(alist)
    alist=alist[shift:]
    for i in range(len(alist)):
        if abs(alist[i]) -1 < len(alist) and alist[abs(alist[i])-1] > 0:
            alist[abs(alist[i])-1]=-alist[abs(alist[i])-1]
    for i in range(len(alist)):
        if alist[i] > 0:
            return i+1
    return len(alist)+1

if __name__ == "__main__":
    t = int(input("Enter no. of testcases : "))
    while t > 0:
        alist = [int(i) for i in input("Enter elements of list : ").split()]
        ans = findSmallestPositive(alist)
        print(ans)
        t-=1