
class Node :

    neste = None

    def __init__(self, data) :
        self.data = data

    def __str__(self) :
        return str(self.data)

class Set :

    start = None
    slutt = None

    def contains(self, y):

        peker = self.start

        while peker != None :
            if peker.data == y :
                return True
            peker = peker.neste
        
        return False

    def insert(self, y) :
        nyNode = Node(y)

        if self.start == None :
            self.start = nyNode
            self.slutt = nyNode
            return True

        else :

            if not self.contains(y):

                peker = self.start
                while peker.neste != None :
                    peker = peker.neste
                
                peker.neste = nyNode
                self.slutt = nyNode
                return True

        return False
    
    def remove(self, y) :
        peker = self.start
        forrige = None

        if self.contains(y) :
            while peker.data != y :
                forrige = peker
                peker = peker.neste
            
            if self.size() == 1 :
                self.start = None
                self.slutt = None
            else :
                if peker == self.start :
                    self.start = peker.neste
                elif peker == self.slutt :
                    self.slutt = forrige
                    forrige.neste = None
                else :
                    forrige.neste = peker.neste
                    peker.neste = None

    def size(self) :
            peker = self.start
            storrelse = 0

            while peker != None :
                storrelse += 1
                peker = peker.neste
            
            return storrelse
    

def main():


    n = int(input())

    test = Set()

    for _ in range(n) :
    
        argumenter = input()
        arg = str(argumenter)
        delopp = arg.split(" ")

        if(delopp[0] == "insert") :
            test.insert(delopp[1])
        elif(delopp[0] == "contains") :
            print(test.contains(delopp[1]))
        elif(delopp[0] == "remove") :
            test.remove(delopp[1])
        elif(delopp[0] == "size") :
            print(test.size())

main()