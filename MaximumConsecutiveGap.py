def maximumGap(A):
    A = list(A)
    n = len(A)
    if n <2:
        return 0
    maxElement = max(A)
    minElement = min(A)
    gap = (maxElement - minElement)/(n-1)
    if gap == 0:
        return 0
    numBuckets = [[] for i in range(int((maxElement - minElement)/gap))]

    for num in A:
        index = int((num - minElement)/gap)
        if index >= len(numBuckets):
            index = len(numBuckets)-1

        numBuckets[index].append(num)
    
    maxGap = 0
    list2 = []
    for lst in numBuckets:
        if len(lst) != 0:
            list2.append(lst)
    
    print(list2)
#     print(numBuckets)
    for i in range(1,len(list2)):
        maxValue = min(list2[i])
        minValue = max(list2[i-1])
        maxGap = max(maxGap,maxValue-minValue)
        
    return maxGap
            
            
        
