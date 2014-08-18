def is_palindrome(s):
    """

    >>> is_palindrome('noon')
    True
    >>>
    """
    return reverse(s) == s

def reverse(s):
    cs=''
    for ch in s:
        cs=ch+cs

    return cs

def is_palindrome_2(s):
    n = len(s)
    return s[:n//2]==reverse(s[n-n//2:])
        
        
def is_palindrome_3(s):
    i=0
    j=len(s)-1

    while i<j and s[i] == s[j]:
        i=i+1
        j=j-1

    return j<=i
        
