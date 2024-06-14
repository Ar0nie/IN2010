#Et binaert soketree som legger inn nye elementer, men ingen duplikater, derav oppforer det seg som datastrukturen set.
#Det meste av kode er tilnærmet lik psudo-koden fra forelesning med unntak av testprogrammet som benyttes helt nederst.

#Klassen Node som benyttes for elementer i settet.
class Node :

    def __init__(self, element) :
        self._element = element
        self._left = None
        self._right = None

    def __str__(self) :
        return str(self._element)


class Oppgave1 :

    def __init__(self) :
        self._size = 0

    #Insert for elementer i treet. Inserter ikke duplikater. Returnerer roten av treet vårt for hvert kall.
    def insert(self, v, x) :
        if v == None:
            v = Node(x)
            self._size += 1
            return v
            
        elif x < v._element :
            v._left = self.insert(v._left, x)
        elif x > v._element :
            v._right = self.insert(v._right, x)

        return v
    
    #Metoden contains returnerer true eller false for om x forekommer i treet. 
    def contains(self, v, x) :
        if v == None :
            return False
        
        if v._element == x :
            return True
        
        if x < v._element :
            return self.contains(v._left, x)
        
        if x > v._element :
            return self.contains(v._right, x)

    #Metoden finnMinste, benyttes i det man skal fjerne elementer i fra treet for å erstatte en verdi som fjernes.
    #Finner minste ved å forflytte seg frem til venstre barn, så lenge det lar seg gjøre.
    def finnMinste(self, v) :
        if v._left != None:
            return self.finnMinste(v._left)
        else :
            return v
    
    #fjerner element i fra treet, sammenligner verdien på noden man er ved og forflytter seg nedover deretter.
    def remove(self, v, x) :
        if v == None :
            return None
        
        if x < v._element :
            v._left = self.remove(v._left, x)
            return v
        
        if x > v._element :
            v._right = self.remove(v._right, x)
            return v
        
        if v._left == None :
            self._size -= 1
            return v._right

        if v._right == None :
            self._size -= 1
            return v._left
        
        #maa finne minste for aa kunne erstatte den verdien som fjernes.
        u = self.finnMinste(v._right)
        v._element = u._element
        v._right = self.remove(v._right, u._element)

        return v

    #Enkel return.
    def size(self) :
        return self._size

#Testprogram for inndeling etter ord og tilhorende input.
def main():

    n = int(input())
    test = Oppgave1()
    rot = None

    for _ in range(n) :
    
        argumenter = input()
        arg = str(argumenter)
        delopp = arg.split(" ")

        if(delopp[0] == "insert") :
            rot = test.insert(rot,int(delopp[1]))
            
        elif(delopp[0] == "contains") :
            print(test.contains(rot,int(delopp[1])))

        elif(delopp[0] == "remove") :
            rot = test.remove(rot,int(delopp[1]))

        elif(delopp[0] == "size") :
            print(test.size())

main()
