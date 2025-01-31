def unique_digits(n):
    """Return the number of unique digits in positive integer n.

    >>> unique_digits(8675309) # All are unique
    7
    >>> unique_digits(13173131) # 1, 3, and 7
    3
    >>> unique_digits(101) # 0 and 1
    2
    """
    i=0 
    cnt=0 
    while i<10:
        
        if has_digit(n,i):
            cnt+=1
        i+=1    
    return cnt
def has_digit(n, k):
    """Returns whether k is a digit in n.

    >>> has_digit(10, 1)
    True
    >>> has_digit(12, 7)
    False
    """
    assert 0<=k < 10
    a=False
    i=getfigs(n)-1
    while n>0:
        t =pow(10,i)
        this=n//t
        i-=1
        n=n-this*t 
        if n == 0:
            return k == 0
        if(this==k):
            a= True
            break
    return a
        
        
def getfigs(n):
    i=0
    while n//pow(10,i)!=0:
        i+=1
    return i
a=1
def f(g):
    a=2
    return lambda y:a*g(y)

k=lambda a:a+3
def end(n,d):
    i=1
    while n//pow(10,i-1)>0 :
        x=n%pow(10,i)
        t=x//pow(10,i-1)
        print(t)
        if t==d:
            return
        i+=1
def ds(x):
    if 0:
        return "wqew"
def search(f):
    x=0
    while True:
        if f(x):
            return x
        x+=1
def inverse(f):
    def g(y):
        return search(lambda x:f(x)==y)
    return g
def squ(x):
    return x*x
def inv(f):
    def g(y):
        x=0
        while f(x)!=y:
            x+=1
            if f(x)==y:
                return x
    return g
