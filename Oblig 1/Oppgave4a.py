#Svar paa oppgave 4 kun ved bruk av lister.

class Oppgave4a :

    def balanse(self, array) :
        
        if len(array) == 0:
            return
        
        midtpunkt = len(array)//2
        print(array[midtpunkt])
        self.balanse(array[:midtpunkt])
        self.balanse(array[midtpunkt + 1:])
    
def main(): 

    n = input()
    test = Oppgave4a()
    liste = []

    while n != None:
        
        tall = int(n)
        liste.append(tall)
        
        try :
            n = input()
        except EOFError as e :
            test.balanse(liste)
            return

main()