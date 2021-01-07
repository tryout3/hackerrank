# Complete the compareTriplets function below.
def compareTriplets(a, b):
    
    sumA = 0
    sumB = 0
    
    for i in range(3):
        if a[i] > b[i]:
            sumA +=1
        if a[i] < b[i]:
            sumB +=1
                
    return (sumA, sumB)
