#Merge sort algortmen for testing, store O notasjon paa formen O(n log(n)).

def sort(A) :
    
    if len(A) > 1:
        venstre_arr = A[:len(A)//2]
        hoyre_arr = A[len(A)//2:]
    
        #Rekursivt kall
        sort(venstre_arr)
        sort(hoyre_arr)

        i = 0 #Venstre array index
        j = 0 #Hoyre array index
        g = 0 #global merged array index
        
        while i < len(venstre_arr) and j < len(hoyre_arr) :
            if venstre_arr[i] < hoyre_arr[j]:
                A[g] = venstre_arr[i]
                i += 1
            else :
                A[g] = hoyre_arr[j]
                j += 1
            
            g += 1
        
        while i < len(venstre_arr):
            A[g] = venstre_arr[i]
            i += 1
            g += 1
        
        while j < len(hoyre_arr):
            A[g] = hoyre_arr[j]
            j += 1
            g += 1

    return A