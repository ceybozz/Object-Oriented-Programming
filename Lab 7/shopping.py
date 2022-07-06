class Shopping: # klassen är en model för de objekten vi ska skapa och börjar alltid med storbokstav. 
                #namn på klassen "Shopping".
                # Shopping klassen innehåller en __init__ klassmetod.

    def __init__(self,name,amount,price): # __init__ klassmetoden även kallad kontruktormetod anropas när en ny-
        #vara(objekt) skapas med ett self-argument.
        # metoden ser till att objektet får sina klassattribut(värden).
        # self argumentet i objektets metod ser till att värden i instantvariabeln sparas och inte-
        #förkastas när __init__ metoden hamnar ur räkkvidd.
        # utan self argumentet har objektes attributer inte sparats efter __init__ metoden körts-
        # nedan finns det instantvariablar som innehåller värden. de har gjorts private med dubbla understräck-
        #dvs. funktionerna definerat för klassen körs istället när värdet på variabel ändras.
        self.__name = name # instantvariabel __namn kopplas till en sträng med objektets namn variabel.
        self.__amount = amount # instantvariabeln __antal kopplas till en integer med objektets antal variabel.
        self.__price = price # instantvariabeln __pris kopplas till en integer med objektets pris variabel.

    # set - get metoder.
    def set_name(self,name):
        self.__name = name
    def set_amount(self,amount):
        self.__amount = amount
    def set_price(self,price):
        self.__price = price
    def get_name(self):
        return self.__name
    def get_amount(self):
        return self.__amount
    def get_price(self):
        return self.__price

    def __str__(self): # __str__ metoden omvandlar objektet till en sträng.
        # utskrift av objektet.
        utskrift = 'Namn:'+ self.get_name()+\
        '\nAntal: '+ str(self.get_amount())+\
        '\nPris: ' + str(self.get_price())
        return utskrift