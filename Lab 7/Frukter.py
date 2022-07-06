class Frukter:
    def __init__(self,namn,antal,pris):
        self.__namn = namn
        self.__antal = antal
        self.__pris = pris

    def set_namn(self,namn):
        self.__namn = namn
    def set_antal(self,antal):
        self.__antal = antal    
    def set_pris(self,pris):
        self.__pris = pris

    def get_namn(self):
        return self.__namn
    def get_antal(self):
        return self.__antal
    def get_pris(self):
        return self.__pris

    def __str__(self):
        utskrift = 'Namn: ' + self.get_namn() + '\n' + \
                    'Antal: ' + str(self.get_antal()) + \
                    '\nPris Kr: ' + str(self.get_pris())
        return utskrift