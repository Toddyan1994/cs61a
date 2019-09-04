def gcd(m,n):
    """Returns the largest k that devides m and n
    k,m,n are all positive integers
    >>> gcd(4,6)
    2
    >>> gcd(9,9)
    9
    >>> gcd(20,10)
    10
    >>> gcd(7,9)
    1
    """
    if m==n:
        return m
    elif m<n:
        return gcd(n,m)
    else:
        return gcd(m-n,n)
