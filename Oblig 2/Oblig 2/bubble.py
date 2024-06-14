#Implementasjon av bubble sort paa kjoretiden O(n^2).
def sort(A) :
    
    for i in range(len(A)-1, 0,-1):
        for j in range(i) :
            if A[j] > A[j + 1] :
                A.swap(j, j+1)
    
    return A