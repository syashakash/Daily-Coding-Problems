'''
28 08 2019
This problem was asked by Apple.

Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.
'''

from time import sleep

def jobScheduler(func, nSecs):
    sleep(nSecs)
    func()

def customFn():
    print("Sorry for the delay!!!")

if __name__ == "__main__":
    nSecs=int(input("Enter delay period : "))
    jobScheduler(customFn, nSecs)
