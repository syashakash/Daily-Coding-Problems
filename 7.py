'''
25 08 2019
This problem was asked by Facebook.

Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. For example, '001' is not allowed.
'''
def main():
    t=int(input("Enter testcases : "))
    while t > 0:
        n=input("Enter sequence : ")
        ans=getAllCombinations(n)
        print(ans)
        t-=1

def getAllCombinations(string):
        n=len(string)
        return util(string,0,n)

def util(string, i, n):
        if i >= n:
                return 1
        k1 = 0
        if 1 <= int(string[i]) <= 26:
                k1 = int(string[i])
        k2 = 0
        if i < n - 1:
                if 10 <= int(string[i]) * 10 + int(string[i + 1]) <= 26:
                        k2 = int(string[i]) * 10 + int(string[i + 1])
                else:
                        k2 = 0
        if k1 > 0 and k2 > 0: 
                return util(string, i+1, n) + util(string, i+2, n)
        elif k1 > 0:
                return util(string, i+1, n)
        elif k2 > 0:
                return util(string, i+2, n)
        else:
                return 0

if __name__=="__main__":
    main()