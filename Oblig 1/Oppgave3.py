#Dette er et svar for oppgave 3, der oppgaven var aa lese inn en tekstfil, skape et tre og navigere en katt ned fra en gitt node i treet.
#Implementasjonen er ikke saa effektiv, og benytter dessverre noen sub-optimale implementasjoner for aa skape selve treet. Insetting forekommer for det meste paa linear tid.
#Selve metoden for at katten skal navigere seg ut av treet er derimot, ganske saa rask, da det kun innebaerer aa folge foreldrepekeren til noden helt til roten av treet.

class Node :

    #Hver node har et element, altsaa en verdi, en liste av referanser til barnenoder og en foreldrenode referanse.
    def __init__(self, element) :
        self._element = element
        self._children = []
        self._forelder = None

    #Legger til barn i barnenodelisten for en node.
    def addChild(self, child) :
        self._children.append(child)
    #Setter forelder for noden. Benyttes for aa navigere katten ut av treet.
    def settForelder(self, forelder) :
        self._forelder = forelder

    def __str__(self) :
        return str(self._element)

class Oppgave3 :
    
    def __init__(self) :
        self._alle = []
    
    #Benytter en listestruktur for aa representere treet. Dersom elementet ikke allerede ligger i treet, legg det til. Har ingenting aa si med index.
    def insert(self, x) :
        nyNode = Node(x)

        if not self.inneholder(x):
            self._alle.append(nyNode)
    
    def __str__(self) :
        return str(self._alle)
    #metode som sjekker om treet/lista vaar inneholder et gitt element x.
    def inneholder(self, x) :
        i = 0

        while i < len(self._alle) :
            elem = int(self._alle[i]._element)
            if elem == int(x) :
                return True
            i += 1
        
        return False
    
    #return av en referanse for en gitt node x.
    def hentNode(self, x) :
        i = 0

        while i < len(self._alle) :
            elem = int(self._alle[i]._element)
            if elem == int(x):
                return self._alle[i]
            i += 1
    #Metode for aa printe og navigere katten ut av treet fra noden den sitter paa.
    def reddKatten(self, katteNode) :
        while katteNode != None :
            print(katteNode)
            katteNode = katteNode._forelder
    
    def __str__(self) :
        return str(self._alle)

    #Enkel return av storrelsen paa lista var
    def size(self) :
        return len(self._alle)

def main(): 

    n = str(input())
    test = Oppgave3()
    katteNodeTall = 0

    while n != "-1" :
        
        streng = str(n)
        arg = streng.split(" ")

        if len(arg) == 1 :
            katteNodeTall = int(arg[0])

        else :

            forelderNodeTall = int(arg[0])
            test.insert(forelderNodeTall)

            e = 1
        
            for i in range(len(arg) -1) :
                nyBarneNodeTall = arg[e]
                test.insert(nyBarneNodeTall)

                forelder = test.hentNode(forelderNodeTall)
                barn = test.hentNode(nyBarneNodeTall)

                barn.settForelder(forelder)
                forelder.addChild(barn)

                e += 1

    
        n = str(input())
    
    katteNode = test.hentNode(katteNodeTall)
    test.reddKatten(katteNode)


main()

#Mulig utivkle implementasjon slik at hver tallverdi tilsvarer indexen, kan aksessere kjapper på O(1) istedenfor O(n).'
#Ettersom jeg bruker liste-strukturen i python, må jeg ikke vite på forhånd hva størrelsen på array skal være.
