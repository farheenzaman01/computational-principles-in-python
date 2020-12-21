#creating a list with ordered values

is_booked=[False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
names=["Available", "Available", "Available", "Available", "Available", "Available", "Available", "Available", "Available", "Available", "Available", "Available", "Available", "Available", "Available", "Available", "Available", "Available", "Available", "Available"]

while(True):
    print("1 - Reserve a table\n2 - Clear reservation\n3 - Report\n0 - Exit program")
    choice = int(input("Enter your choice: "))
    if(choice==0):
        break
    elif(choice==1):
        table_num = int(input("Enter table number from 0-19: "))#the usedr input with match to the position of the value in the list
        if(~is_booked[table_num]):
               name = input("Enter your name: ")#list value gets replaced and saved by user name
               names[table_num]=name
               is_booked[table_num]=True
               print("Table",table_num,"booked for you")
        else:
            print("Selected table is not available")
     elif(choice==2):
         table_num = int(input("Enter table number from 0-19): ")) #clearing the reservaions
        if(is_booked[table_num]):
                    names[table_num]="Avilable"
                    is_booked[table_num]=False
                    print("Table",table_num," is no longer reserved.")
                else:
                    print("Selected table is already available.")
            elif(choice==3):#report the selected tables with the user input
                for i in range(20):
                    print(i,names[i])
                print("\n")
            else:
                print("Invalid choice!!!")