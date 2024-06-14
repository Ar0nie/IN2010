#Dette er et svar paa oppgave 2, for en koe med innsetting paa tre plasser, foran, bak og i midten.
#I denne implementasjonen har vi benyttet den innebygde liste-strukutren som man finner i python, dette gjor metodene svaert oversiktlige. Derimot er kjoretiden noe varierende, 
#og er tilnaermet linear tid paa flere av operasjonene.

#Man kunne sett for seg at enkelte operasjoner ville ha kunnet blitt gjort om til O(1) derav, push_front dersom dette var implementert som en lenkeliste istedenfor.

class Oppgave2 :

    def __init__(self) :
        self._size = 0
        self._teque = []
    
    def pushBack(self, x) :
        self._teque.append(x)
        self._size += 1
    
    def pushFront(self, x) :
        self._teque.insert(0, x)
        self._size += 1
        
    def pushMiddle(self, x) :
        size = self.size()

        if size == 0 :
            return self.pushFront(x)
        if size == 1 :
            return self.pushBack(x)
        
        index = (size + 1)//2
        self._teque.insert(index, x)
        self._size += 1

    def get(self, i) :
        print(self._teque[i])
    
    def size(self) :
        return self._size

def main():

    n = int(input())
    test = Oppgave2()

    for _ in range(n) :
    
        argumenter = input()
        arg = str(argumenter)
        delopp = arg.split(" ")

        if(delopp[0] == "push_back") :
            test.pushBack(int(delopp[1]))
            
        elif(delopp[0] == "push_front") :
            test.pushFront(int(delopp[1]))

        elif(delopp[0] == "push_middle") :
            test.pushMiddle(int(delopp[1]))

        elif(delopp[0] == "get") :
            test.get(int(delopp[1]))

main()
