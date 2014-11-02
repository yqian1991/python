def getPrime(number):
    """
    find all prime numbers less than or equal the given number, 
    the return value is a list, which contains boolean elements. 
    if value is true, the index is prime. e.g. plist[4]=0, plist[3]=1
    """
    plist = [1 for i in range(0,number+1)]
    #0,1 false
    plist[0]=0
    plist[1]=0
    for i in range(0,number+1):
        if (i%2==0 and i>2):
            plist[i]=0 
    p = 2 # the first prime number is 2
    print plist
    while (p< int(number**0.5)+1):
        p +=1
        while not plist[p]: 
            p+=1
        ptimes = p*p
        print p, ptimes
        step = 2*p
        while ptimes < number:
            plist[ptimes]=0
            ptimes += step
    return plist

print getPrime(100) 