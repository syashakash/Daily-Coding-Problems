'''
30 08 2019
This problem was asked by Amazon.

There exists a staircase with N steps, 
and you can climb up either 1 or 2 steps at a time.
Given N, write a function that returns the number of 
unique ways you can climb the staircase. The order of the steps matters.

For example, if N is 4, then there are 5 unique ways:

1, 1, 1, 1
2, 1, 1
1, 2, 1
1, 1, 2
2, 2
What if, instead of being able to climb 1 or 2 steps at a time, 
you could climb any number from a set of positive integers X? 
For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time.
'''

def stepCountCustom(n_steps):
    dp = [0] * (n_steps + 1)
    dp[1] = 1
    dp[2] = 2
    dp[3] = 3
    if n_steps < 4:
        return dp[n_steps]
    for step in range(4, n_steps + 1):
        dp[step] = dp[step - 1] + dp[step - 2]
    return dp[n_steps]

def stepCountWithGivenSteps(n_steps, stepList):
    pass

def main():
    t = int(input("Enter testcases : "))
    while t > 0:
        stepList = [int(i) for i in input("Enter step List : ").split()]
        n_steps = int(input("Enter steps : "))
        ans = 0
        if len(stepList) == 0:
            ans = stepCountCustom(n_steps)
        else:
            ans = stepCountWithGivenSteps(n_steps, stepList)
        print(ans)
        t -= 1

if __name__ == "__main__" :
    main()
