def search_car(data,MPG,HorsePower):
    print("The cars having minimum",MPG,"MPG and",HorsePower,"Horse power are:")
    for record in data:                                               # iterate through every record in data-base
        if float(record[1])>=MPG and float(record[2])>=HorsePower:    # searches the car with a minimum mpg and horse-power
            for value in record:
                print(value,end=" ")
            print()

def best_and_worst(data): 
    best = 0
    worst = 1000000000    # initialize best , worst and average 
    total = 0
    for i in range(len(data)):  # iterate through every record in database
        value = float(data[i][1]) # data[i][1] corresponds to mpg
        total = total + value   # calculating average mpg  
        if value>best:          # searches for best mpg value
            best = value
            best_mpg = i
        if value<worst:         # searches for worst mpg value
            worst = value
            worst_mpg = i
    average = total/len(data)
    print("The average MPG of all the cars is",average)
    print("The car with best MPG is:")
    for value in data[best_mpg]:
        print(value,end=" ")
    print("\nThe car with worst MPG is:")
    for value in data[worst_mpg]:
        print(value,end=" ")
    print()

def inventory_by_origin(data,origin):
    count = 0
    for record in data:     # iterate through all records in database list data
        if record[3]==origin.capitalize():  # record[3] represents origin column in database
            count=count+1
    print("The number of cars having the origin",origin,"are",count)


f = open("cars.txt",'r')  # read the data file from here
lines = f.readlines()     # read line by line from data-base
cars_data = []
for line in lines:
    cars_data.append(line.split()) 
    

while True:
    print("\nPlease choose a option in the menu :")
    print("Menu")
    print("----------")
    print("1. Search a car with minimum MPG and Horse Power")
    print("2. Best and Worst cars on MPG")
    print("3. Invetory of cars by Origin")
    print("4. Quit\n")
    option = int(input("Please enter a option: "))
    if option == 1:
        MPG=int(input("Please enter MPG: "))
        HP=int(input("Please enter Horse power: "))
        search_car(cars_data,MPG,HP)
    if option == 2:
        best_and_worst(cars_data)
    if option == 3:
        origin = input("Please enter origin: ")
        inventory_by_origin(cars_data,origin)
    if option == 4:
        break


