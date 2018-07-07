def findCount(A, B):
    A = list(A)
    low = 0
    high = len(A)-1
    first = -1
    last = -1
    while(low<=high):
        mid = low +(high-low)//2
        if A[mid] == B:
            first= mid
            high = mid-1
        elif B <A[mid]:
            high = mid -1
        else:
            low = mid+1
            
    low = 0
    high = len(A)-1
    while(low<=high):
        mid = low +(high-low)//2
        if A[mid] == B:
            last= mid
            low = mid+1
        elif B <A[mid]:
            high = mid -1
        else:
            low = mid+1
    
    if (first ==-1) and (last ==-1):
        return 0
    else:
        return last - first +1
    
            
            
            
    
