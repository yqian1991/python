def linear_search(L, v):
    
    i = 0
    
    while i != len(L) and v != L[i]:
        i = i+ 1

    if i == len(L):
        return -1
    else:
        return 1
    
