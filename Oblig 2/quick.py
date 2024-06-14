#Maa gjore slik at sort kaller paa quicksort videre for aa ungaa error med testprogram,
#  derfor er det delt opp slik at quicksort metoden egt er den ordinaere sort metoden.

def sort(A):
    venstre = 0
    hoyre = len(A) -1
    return quickSort(A, venstre, hoyre)


def quickSort(A, venstre, hoyre) :
    if venstre < hoyre :
        del_pos = delOpp(A, venstre, hoyre)
        quickSort(A, venstre, del_pos -1)
        quickSort(A, del_pos + 1, hoyre)

    return A

def delOpp(A, venstre, hoyre) :

    i = venstre
    j = hoyre - 1
    pivot = A[hoyre]

    while i < j:
        while i < hoyre and A[i] < pivot :
            i += 1
        
        while j > venstre and A[j] >= pivot:
            j -= 1
        
        if i < j:
            A.swap(i, j)
    
    if A[i] > pivot :
        A.swap(i, hoyre)
    
    return i
