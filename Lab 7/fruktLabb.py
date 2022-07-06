import Frukter
import pickle

FILNAMN = 'frukter.dat'
def main():  
    minaFrukter = hamtaFrukter()
    if not minaFrukter:
        minaFrukter = startUpFruktDict()
    else:
        skrivaUtInfoOmAllaFrukter(minaFrukter)

    val = 0

    while val != 10:
        val = getMenyVal()

        if val == 1:
            addFrukt(minaFrukter)
        if val == 2:
            print(f'Antal frukter: {antal(minaFrukter)}')
        if val == 3:
            sokInfoOmFrukt(minaFrukter)
        if val == 4:
            skrivaAllaNamnOmFrukter(minaFrukter)
        if val == 5:
            skrivaUtInfoOmAllaFrukter(minaFrukter)
        if val == 6:
            uppdateraAntalOchPrisOmFrukt(minaFrukter)
        if val == 7:
            berankaTotalPrisMedAllaFrukter(minaFrukter)
        if val == 8:
            taBortFrukt(minaFrukter)
        if val == 9:
            minaFrukter.clear()
            print(minaFrukter)
        if val == 10:
            print('Programmet är avslutat')
            break
        sparaFrukter(minaFrukter)

def getMenyVal():
    print('------------------------------------------------')
    print('Meny val\n')
    print('------------------------------------------------')
    print('1. Lägg till en frukt')
    print('2. Skriv ut antal frukter i listan')
    print('3. Sök information om en frukt')
    print('4. Skriv ut alla namn på frukterna i listan')
    print('5. Skriv ut info om alla frukter i listan')
    print('6. Uppdatera antal och pris på en frukt')
    print('7. Beräkna kostnaden för alla frukter')
    print('8. Ta bort frukt - Namn')
    print('9. Töm hela listan på frukter')
    print('10. Avsluta programmet')
    print('------------------------------------------------')

    val = int(input('Välj mellan 1-10: ')) 
    while val < 1 or val > 10:
        val = int(input('Välj 1-10'))
    return val

def sparaFrukter(frukt_dict):
    outputFile = open(FILNAMN, 'wb')
    pickle.dump(frukt_dict, outputFile)
    outputFile.close()

def hamtaFrukter():
    try:
        inputFile = open(FILNAMN, 'rb')
        frukt_dict = pickle.load(inputFile)
        inputFile.close()
    except IOError:
        frukt_dict = {}
    return frukt_dict

def startUpFruktDict(): 
    item1 = Frukter.Frukter('Äpple', 6, 10)
    item2 = Frukter.Frukter('Banan', 5, 20)
    item3 = Frukter.Frukter('Kiwi', 10, 15)
    frukt_dict = {'Äpple':item1,'Banan':item2,'Kiwi':item3}
    return frukt_dict

def sokInfoOmFrukt(dictG): ## Knapp 3
    namn = input('\nSkriv namn: ')
    print(dictG.get(namn, 'Namnet finns inte.'))

def addFrukt(dictG): ## Knapp 1
    namn = input('\nSkriv in namn: ')
    antal = float(input('Skriv in antal: '))
    pris = float(input('Skriv in pris: '))
    fruktObj = Frukter.Frukter(namn, antal, pris)
    if namn not in dictG:
        dictG[namn] = fruktObj
        print(namn + 'har lagts till')
    else:
        print('Oj, något fick fel.. Namnet finns redan')

def uppdateraAntalOchPrisOmFrukt(dictG): ## Knapp 6
    namn = input('\nVilken frukt ska uppdateras?')

    antal = float(input('Nytt antal: '))
    pris = float(input('Nytt pris: '))
    objList = list(dictG.values())
    for item in objList:
        namnObj = item.get_namn()
        if namn == namnObj:
            item.set_antal(antal)
            item.set_pris(pris)
            print(item.get_namn())
            print(item.get_antal())
            print(item.get_pris())

def skrivaUtInfoOmAllaFrukter(dictG): ## Knapp 5
    for v in dictG.values():
        print(v)

def taBortFrukt(dictG): ## Knapp 8
    namn = input('\nSkriv in den frukt du vill ta bort: ')
    if namn in dictG:
        del dictG[namn]
        print(namn + ' är borttaget.')
    else:
        print('Hittade inte namnet: '+ namn)

def antal(dictG): ## Knapp 2
    kvantitet = len(dictA) 
    return kvantitet

def skrivaAllaNamnOmFrukter(dictA): # Knapp 4
    for namn in dictA:
        print(namn)

def berankaTotalPrisMedAllaFrukter(dictG): # Knapp 7
    total = 0
    for obj in dictG.values():
        total +=int(obj.get_pris()) * int(obj.get_antal())
    print(f'Total kostnad av varor:{total}') 

main()