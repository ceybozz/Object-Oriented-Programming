import random   #Gör så att all ramdom funkar

sticks = 21 #Variabel ett
print('\nThere are 21 sticks.') #Skrvier info
print('Every turn you or the computer pick 1 or 2 sticks.') #Skrvier info
print('The one who takes the last stick loses the game.')   #Skrvier info

while True: #While loop, är direkt på 
    
    sticksTaken = int(input('\nPick a stick: '))    #Variabel två, skriv sticka

    if sticksTaken < 1 or sticksTaken > 2:  #Om variabel två är mindre än ett eller större än två
        print('\nError! Try again!')    #Skriver försök igen
        
        sticksTaken = int(input('Please pick a stick between 1 and 2: '))   #Skriv sticka
    
    if sticksTaken == 1:    #Om 1 sticka taget
        sticks -= 1 #Variabel ett minus ett 
        value = random.randint(1,2) #Randomiserar ett tal mellan ett eller två
        sticksLeft = sticks - value #Variabel tre är kvar är lika med variabel ett minus vatiabel två.

    elif sticksTaken == 2:  #Om 2 sticka taget
        sticks -= 2 #Variabel ett minus två
        value = random.randint(1,2) #Randomiserar ett tal mellan ett eller två
        sticksLeft = sticks - value
    
    sticks = sticksLeft #Variabel ett är lika med variabel tre 
    
    print("\nComputer took", value, 'stick.')   #Skriver antal stickor datorn tar
    print(sticksLeft, 'sticks left.')   #Skriver ut varabel tre

    if sticks <= 0: #Om variabel ett slutar med 0
        print("Congrats! You won!")   #Skriver du vann
        break   #Stoppar programmet 

    if sticks == 1: #Om variabel ett slutar med 1
        print("Sorry! You lost!") #Skriver du förlora 
        break   #Stoppar programmet 