class Car:
    def __init__(self, brand, model, year, color, plate, price):
        self.__brand = brand
        self.__model = model
        self.__year = year
        self.__color = color
        self.__plate = plate
        self.__price = price


    def set_brand(self, brand):
        self.__brand = brand

    def set_model(self, model):
        self.__model = model

    def set_year(self, year):
        self.__year = year

    def set_color(self, color):
        self.__color = color

    def set_plate(self, plate):
        self.__plate = plate

    def set_price(self, price):
        self.__price = price


    def get_brand(self):
        return self.__brand

    def get_model(self):
        return self.__model

    def get_year(self):
        return self.__year

    def get_color(self):
        return self.__color

    def get_plate(self):
        return self.__plate
         
    def get_price(self):
        return self.__price

    def __str__(self):
        printing = '\nBrand: ' + self.get_brand()+\
                '\nModel: ' + (self.get_model())+\
                '\nYear: ' + str(self.get_year())+\
                '\nColor: ' + self.get_color()+\
                '\nPlate: ' + self.get_plate()+\
                '\nPris: ' + str(self.get_price())
        return printing