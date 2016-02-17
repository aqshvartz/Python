#!/usr/bin/python3
# -*- coding: utf-8 -*-

def memoize(func):
    class memoize:
        def __init__(self,f):
            self.f = f
            self.memo = {}
        def __call__(self, *args):
            if args not in self.memo:
                self.memo[args]=self.f(*args)
            return self.memo[args]
    return memoize(func)

def memoize1(func):
    memo = {}
    def wrap(x):
        if x not in memo:
            memo[x]=func(x)
        return memo[x]
    return wrap
    
@memoize
def trib(n):
    if n <= 1:
        return 0
    elif n == 2:
        return 1
    else:
        return trib(n-1) + trib(n-2) + trib(n-3)

@memoize
def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)

@memoize
def fib(n):
    if n <= 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

@memoize
def ackermahn(m,n):
    if m==0:
        return n+1
    elif m>0 and n==0:
        return ackermahn(m-1,1)
    elif m>0 and n>0:
        return ackermahn(m-1,ackermahn(m,n-1))

if __name__ == '__main__':
    import timeit
    print(timeit.timeit("trib(50)", setup="from __main__ import trib"))
    print(timeit.timeit("trib(51)", setup="from __main__ import trib"))
    print(timeit.timeit("fact(50)", setup="from __main__ import fact"))
    print(timeit.timeit("fact(51)", setup="from __main__ import fact"))
