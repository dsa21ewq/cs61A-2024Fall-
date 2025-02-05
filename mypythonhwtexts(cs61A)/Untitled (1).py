def unique_digits(n):
    """Return the number of unique digits in positive integer n.

    >>> unique_digits(8675309) # All are unique
    7
    >>> unique_digits(13173131) # 1, 3, and 7
    3
    >>> unique_digits(101) # 0 and 1
    2
    """
    i = 0
    cnt = 0
    while i < 10:

        if has_digit(n, i):
            cnt += 1
        i += 1
    return cnt


def has_digit(n, k):
    """Returns whether k is a digit in n.

    >>> has_digit(10, 1)
    True
    >>> has_digit(12, 7)
    False
    """
    assert 0 <= k < 10
    a = False
    while n > 0:
        x = n % 10
        if (x == k):
            return True
        n //= 10
    return False


def getfigs(n):
    i = 0
    while n // pow(10, i) != 0:
        i += 1
    return i


a = 1


def f(g):
    a = 2
    return lambda y: a * g(y)


k = lambda a: a + 3


def end(n, d):
    i = 1
    while n // pow(10, i - 1) > 0:
        x = n % pow(10, i)
        t = x // pow(10, i - 1)
        print(t)
        if t == d:
            return
        i += 1


def ds(x):
    if 0:
        return "wqew"


def search(f):
    x = 0
    while True:
        if f(x):
            return x
        x += 1


def inverse(f):
    def g(y):
        return search(lambda x: f(x) == y)

    return g


def squ(x):
    return x * x


def inv(f):
    def g(y):
        x = 0
        while f(x) != y:
            x += 1
            if f(x) == y:
                return x

    return g


"This is what recursion feels like：self reference"


def print_sums(x):
    print(x)

    def print_next(y):
        return print_sums(x + y)

    return print_next


def print_alot(x):
    print(x)
    return print_alot


def fig_path(m, n):
    if m == 1 or n == 1:
        return 1
    return fig_path(m - 1, n) + fig_path(m, n - 1)


def find_partition(n, m):
    if n == 0:
        return 1
    if m == 0:
        return 0
    return find_partition(n, m - 1) + find_partition(n - m, m)


# 这是luhn算法的一种，但也可以用递归实现
def luhn_check(number):
    def digits_of(n):
        return [int(d) for d in str(n)]

    digits = digits_of(number)
    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]
    checksum = sum(odd_digits)

    for d in even_digits:
        checksum += sum(digits_of(d * 2))

    return checksum % 10 == 0


def cascade(n):
    if n < 10:
        print(n)
    else:
        print(n)
        cascade(n // 10)
        print(n)


def cascade_another(n):
    print(n)
    if n >= 10:
        cascade_another(n // 10)
        print(n)
#this is an elegant example,building sequence
def f_then_g(f,g,n):
    if n>0:
        f(n)
        g(n)
grow=lambda n:f_then_g(grow,print,n//10)
shrink=lambda n:f_then_g(print,shrink,n//10)
def inverse_cascade(n):
    grow(n)
    print(n)
    shrink(n)

  #这是我个人的小好奇：指数的比例随n的增大如何变化
def is_prime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True

def rateofprime(n):
    cnt=0
    for i in range(1,n):
        if is_prime(i):
            cnt+=1
    return cnt/n
#TREE RECURSION：
def fib(n):
    if n==0:
        return 0
    if n==1:
        return 1
    return fib(n-1)+fib(n-2)
