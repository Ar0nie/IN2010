#Implementasjon av Insertion sort, med O notasjon O(n^2).

def sort(A):

    for i in range(1, len(A)):
        j = i
        #Er hoyre nabo storre enn venstre nabo?
        while A[j - 1] > A[j] and j > 0:
            #Swap
            A.swap(j-1,j)
            # A[j-1], A[j] = A[j], A[j-1]
            #Gaa videre til venstre
            j -= 1


    return A