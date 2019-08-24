'''
19 08 2019

This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
'''

if __name__=="__main__":
    n = int(input("Number of Test Cases : "))
    while n > 0:
        lst = [int(i) for i in input("Enter List : ").strip().split()]
        k = int(input("Enter sum : "))
        lst = sorted(lst)
        i,j=0,len(lst)-1
        found = False
        while i < j:
            if lst[i] + lst[j] == k:
                found = True
                break
            elif lst[i] + lst[j] > k:
                j-=1
            else:
                i+=1
        print(found)
        n-=1