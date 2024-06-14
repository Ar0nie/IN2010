import heapq

#Rekursiv metode som gir utskrift i riktig rekkefølge for et gitt input. Er paa formen av en heap og bruker kun heap kommandoer.
def heapUtskrift(heap) :

        heapMidt = len(heap)//2
        midl = []

        heapSist = []

        if len(heap) == 0: 
            return
        
        while len(heap) != heapMidt + 1:
            retur = heapq.heappop(heap)
            heapq.heappush(heapSist,retur)

        print(heapq.heappop(heap))

        heapUtskrift(heap)
        heapUtskrift(heapSist)
        return 

def main(): 

    n = input()
    heap1 = []
    
    while n != None:
        
        tall = int(n)
        heapq.heappush(heap1,tall)
        
        try :
            n = input()
        except EOFError as e :
            break
    
    heapUtskrift(heap1)
    
main()