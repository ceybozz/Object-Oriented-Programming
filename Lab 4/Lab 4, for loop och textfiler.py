import random
gradeF = 0  #Variabel ett 
gradeE = 0  #Variabel två 
gradeC = 0  #Variabel tre 
gradeA = 0  #Variabel fyra 

txtFile = open('labb4.txt', 'r')    #Variabel fem, anger & öppnar textfilen

for line in range(145):
    randomPick = random.randint(45, 145) #Variabel sex, random väljer mellan 1 - 145

    if randomPick >= 0 and randomPick <= 59:   #Om siffrorna i raden är mellan 0 - 59
        gradeF += 1 #Variabel ett, plus 1,

    elif randomPick >= 60 and randomPick <= 75:  #Om siffrorna i raden är mellan 60 - 75
        gradeE += 1 #Variabel två, plus 1, 
    
    elif randomPick >= 76 and randomPick <= 89:  #Om siffrorna i raden är mellan 76 - 89
        gradeC += 1 #Variabel tre, plus 1, 

    elif randomPick >=90 and randomPick <= 100: #Om siffrorna i raden är mellan 90 - 100
        gradeA += 1 #Variabel fyra, plus 1, 
   
txtFile.close() #Stänger textfilen
allGrade = gradeF + gradeE + gradeC + gradeA    #Variabel sex = variabel ett, två, tre & fyra
passed = gradeE + gradeC + gradeA   #Variabel sju = variabel två, tre & fyra
hundredProcentpassed = 100 * round(passed/allGrade, 2)   #Variabel åtta = 100 * decimal, variabel sju / 145 
average = allGrade/4    #Variabel nio, medelvärde

print('')
print(f'All the grades: {allGrade}')    #Skriv variabel sju
print(f'Grade A: {gradeA}') #Skriv variabel fyra
print(f'Grade C: {gradeC}') #Skriv variabel tre
print(f'Grade E: {gradeE}') #Skriv variabel två
print(f'Grade F: {gradeF}') #Skriv variabel ett
print(f'Total passed the exam: {passed}')   #Skriv variabel sju
print(f'Total passed the exam: {hundredProcentpassed}%')    #Skriv variabel åtta
print(f'Average: {average}')    #Skriv variabel nio
print('')