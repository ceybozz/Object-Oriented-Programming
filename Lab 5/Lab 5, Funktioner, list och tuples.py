def main():
    myDrinkShoppingList = ['Cola Zero', 'Fanta', 'Pepsi', 'Cola', 'Fanta Exotic', 'Pepsi Max']
    
    continued = True
    while continued:
        print()
        
        choice = int(input('1. Add\n2. Add position\n3. Delete index position\n4. Delete object\n5. Delete list\n6. Amount in lis\n7. Seach position\n8. Sort list\n9. Show list\n10. End program: \n'))
        if choice == 1:
            addMyDrinkShoppingList(myDrinkShoppingList)
        if choice == 2:
            addPositionMyDrinkShoppingList(myDrinkShoppingList) 
        if choice == 3: 
            updateMyDrinkShoppingList = deletePositionMyDrinkShoppingList(myDrinkShoppingList)
            print(updateMyDrinkShoppingList)
        if choice == 4:
            deleteObjMyDrinkShoppingList(myDrinkShoppingList)
        if choice == 5:
            deleteMyDrinkShoppingList(myDrinkShoppingList)
        if choice == 6:
            amountObjMyDrinkShoppingList(myDrinkShoppingList)
        if choice == 7:
            showPositionMyDrinkShoppingList(myDrinkShoppingList)
        if choice == 8:
            sortMyDrinkShoppingList(myDrinkShoppingList)
            print(myDrinkShoppingList)
        if choice == 9:
            print(myDrinkShoppingList)
        if choice == 10:
            print('\nProgram ended')
            break

def addMyDrinkShoppingList(myDrinkShoppingList):    #Knapp 1
    
    continued = 1
    while continued == 1:
        drinks = input('Add a drink: ')
        myDrinkShoppingList.append(drinks)
        continued = int(input('Add more dricks type 1 or else type 2 to continue: '))
    print(myDrinkShoppingList)
    return myDrinkShoppingList

def addPositionMyDrinkShoppingList(myDrinkShoppingList):    #Knapp 2
    continued = 1
    while continued == 1:
        position = int(input('Type index position: '))
        drinks = input('Add drink: ')
        myDrinkShoppingList.insert(position, drinks)
        continued = int(input('Add more index positions type 1 or else type 2 to continue: '))
    print(myDrinkShoppingList)
    return myDrinkShoppingList

def deletePositionMyDrinkShoppingList(myDrinkShoppingList): #knapp 3
    position = int(input('Type index position: '))
    del myDrinkShoppingList[position]
    return myDrinkShoppingList

def deleteObjMyDrinkShoppingList(myDrinkShoppingList):  #knapp 4
    continued = 1
    while continued == 1:
        print(myDrinkShoppingList)
        drinks = input('Type drink: ')
        myDrinkShoppingList.remove(drinks)
        print()
        continued = int(print('Delete more dricks type 1 or else type 2 to continue: '))
    print(myDrinkShoppingList)
    return myDrinkShoppingList

def deleteMyDrinkShoppingList(myDrinkShoppingList): #knapp 5
   myDrinkShoppingList.clear()
   print(myDrinkShoppingList)
   print('List is deleted.')

def amountObjMyDrinkShoppingList(myDrinkShoppingList):  #knapp 6
    amountObj = len(myDrinkShoppingList)
    print(f'There are {amountObj} amount of drinks in the list.')

def showPositionMyDrinkShoppingList(myDrinkShoppingList):   #knapp 7
    continued = 1
    while continued == 1:
        position = int(input('Type index position: '))
        print(myDrinkShoppingList[position])
        continued = int(input('Show more index positions type 1 or else type 2 to continue: '))
    return myDrinkShoppingList

def sortMyDrinkShoppingList(myDrinkShoppingList):   #knapp 8
    myDrinkShoppingList.sort()
    return myDrinkShoppingList
main()