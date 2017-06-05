def insertionSort(A):
    for i in range(1, len(A)):
        key = A[i]
        j = i-1
        while j >=0 and key < A[j] :
                A[j+1] = A[j]
                j -= 1
        A[j+1] = key
 
# Test Code
A = [19, 11, 13, 15, 6]
print ("Array before sorting:")
print A

insertionSort(A)

print ("Array after sorting:")
print A
