import Car

def main():

    continued = True
    car0 = Car.Car('Audi', 'A4 Quattro', 2016, 'Black', 'GWK180', 450000)
    car1 = Car.Car('Peugeot', '308', 2010, 'Grey', 'KMD732', 50000)
    car2 = Car.Car('BMW', 'I8', 2015, 'White', 'URT873', 270000)
    car3 = Car.Car('Lamborghini', 'Veneno', 2013, 'Red', 'ASG693', 420000)
    car4 = Car.Car('Bugatti', 'Veyron', 2005, 'Blue', 'JHL208', 800000)

    carShopp = [car0, car1, car2, car3, car4]
    print(carShopp)

    while continued:
        
        choice = int(input('\n1- Add a car. \n2- Show amount of cars in list. \n3- Search for car. \n4- Show all brands. \n5- Show the cars. \n6- Update year and price. \n7- Total cost of cars. \n8- Delete index position, \n9- Delete car. \n10- Delete shop. \n11- End shop.\n'))
        if choice == 1:
            cars = addCar(carShopp)
        
        if choice == 2:
            print(f'Amout of cars left: {amount(carShopp)}')

        if choice == 3:
            searchCar(carShopp)

        if choice == 4:
            showBrand(carShopp)

        if choice == 5:
            showAllCars(carShopp)

        if choice == 6:
            updateYearPrice(carShopp)

        if choice == 7:
            totoalCost(carShopp)

        if choice == 8:
            deleteCarPosition(carShopp)

        if choice == 9:
            deleteCar(carShopp)

        if choice == 10:
            carShopp.clear()
            print(carShopp)

        if choice == 11:
            print('Program ended.')
            break

def addCar(carShopp):
    brand = input('Brand: ')
    model = input('Model: ')
    year = input('Year: ')
    color = input('Color: ')
    plate = input('Plate: ')
    price = input('Price: ')

    cars = Car.Car(brand, model, year, color, plate, price)
    carShopp.append(cars)
    return cars

def amount(carShopp):
    quantity = len(carShopp)
    return quantity

def searchCar(carShopp):
    search = str(input('Search for a car: '))
    value = 0
    for obj in carShopp():
        if search == obj.get_brand():
            value = 1
    if value == 1:
        print(f'{search}')
    else:
        print('Do not exist.')

def showBrand(carShopp):
    for brand in carShopp:
        print(brand.get_brand())

def showAllCars(carShopp):
    for car in carShopp:
        print(car)

def updateYearPrice(carShopp):
    searchCar = input('Uppdatera ett tillgänglig vara: ')
    value = 0
    for obj in carShopp:
        if searchCar == obj.get_brand():
            value = 1 
    if value == 1:
        price = float(input('Uppdatera pris: '))
        year = float(input('Uppdatera antal: '))
        obj.set_price(price)
        obj.set_year(year)
        print(f'{obj.get_brand} pris: {obj.get_price()} antal: {obj.get_year}') 
    else:
        print('Finns ej')

def totoalCost(carShopp):
    totoalCost = 0
    for car in carShopp:
        totoalCost += int(car.get_year()) * int(car.get_price())
        print(f'Total cost of cars: {totoalCost}kr')

def deleteCarPosition(carShopp):
    deleteCarPosition = int(input('Type in index position: '))
    del carShopp[deleteCarPosition]
    print('Cars left: ')
    for car in carShopp:
        print(car)

def deleteCar(carShopp):
    deleteCar = str(input('Type in brand: '))
    for car in carShopp:
        if deleteCar == car.get_brand():
            carShopp.remove(car)
            print(f'This car has been deleted: \n{car}')
            print('-------------- \nCars left: \n')
    for car in carShopp:
        print(car)
main()