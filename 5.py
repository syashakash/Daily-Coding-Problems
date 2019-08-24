'''
This problem was asked by Jane Street.

cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair. 
For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.

Given this implementation of cons:

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair
Implement car and cdr.
'''

def cons(a, b):
    return (a,b)


def car(pair):
    a,_=pair
    return a

def cdr(pair):
    _,b=pair
    return b


if __name__=="__main__":
    a,b=1,2
    print(car(cons(a,b)))
    print(cdr(cons(a,b)))