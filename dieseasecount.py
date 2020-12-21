class Disease:
        def __init__(self,disease,symptom):
            self.disease = disease
            self.symptom = symptom
  
        def __str__(self):
            return self.disease+","+self.symptom
  
  
#print menu function
def printMenu():
    print('1- Display count of Disease ')
    print('2- Symptoms Counted by Diesase')
    print('3- Diagnose')
    print('0- Exit')
  
def getFileInfo():
#reading the file with stored symptomps and diseases
    file = open('diagnostic.txt')
#storing the date file in a list
    lines = [x.split('\n')[0].split(' ') for x in file.readlines()]
#listing Diesase objects
    diseasesList = []
    for i in lines:
        
        diseasesList.append(Disease(i[0].strip(),i[1].strip()))
        return diseasesList

def displayDiseaseCount(diseases):
    diseaseCount = 0

    diseaseNameList = []
    for i in diseases:
#if disease was out of list
        if(i.disease not in diseaseNameList):
            diseaseNameList.append(i.disease)
            diseaseCount += 1
#printing 
    print('Theres {} diseases in the system.'.format(str(diseaseCount)))

#counting function for symptoms
def symptomCountByDisease(diseases):
#name of disease names in the list
    diseaseNameList = []
    for i in diseases:
        count = 0
        if(i.disease not in diseaseNameList):
            diseaseNameList.append(i.disease)
#counting each disease symptom
    for j in diseases:
#checking the number of similar disease in the list
        if(i.disease == j.disease):
            
            count += 1
#displaying 
    print('Theres{} symptoms shown for {}'.format(str(count),i.disease))

#diagnosingfunction
def diagnose(symptom,diseases):
#loop 
    found = False
    for i in diseases:
#displaying all s diseases with smilar symptoms
        if(symptom == i.symptom):
            found = True
        print('You might have '+i.disease)
        if(not found):
            print('No match')
  
def main():
#retrieving list of Disease objects
    diseases = getFileInfo()
#showing the menu
    while(True):
        printMenu()
        choice = int(input(' choice?: '))
        print()
#calling the menu functions 
        if(choice == 1):
            displayDiseaseCount(diseases)
        elif(choice == 2):
            symptomCountByDisease(diseases)
        elif(choice == 3):
#ask user for the symptoms
            symptom = input('Whats the symptom? ')
            diagnose(symptom.strip(),diseases)
        elif(choice == 0):
            break
        else:
            print('Invalid ')
            print()
  
        main()