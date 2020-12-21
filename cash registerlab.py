total = 0 #total amount of cash in the register
count = 0 #number of sales

while True:#display menu
    print("-Menu")
    print("1-NEW SALE")
    print("2-CASH OUT")
    print("3-REPORT")
    print("4-EXIT")
    choice = int(input("Choice:"))
    
    if choice ==  1:# this part records sales made by the store
        quantity = int(input('Enter the amount sold: '))
        price = float(input('Enter the amount sold: '))

        print("your total is :$")
        total=print(quantity * price)
        
        
    elif choice ==2:# calculating cash out
        total = int(input('Enter the amount total: '))
        cashout = float(input('Enter the amount you are cashing out: '))
        
        print("cash left in registrar:$")
        print(total-cashout)
        
        
    elif choice == 3:# report
        total = int(input('Enter the amount total: '))
        cashout = input('Enter the amount you are cashing out: ')
        
        newtotal = int(input('Enter the amount total after cash out: '))
        print =("following is the report for todays sales:$")
        
        print("total sale:")
        print(total)
        print("total  cashout:")
        print(cashout)
        print("total sale after cashout:")
        print(newtotal)
        
        
        
        
    elif choice == 4:
        print("you have exited the prgram")
        exit
        
   
        break
    #this program is mostly pseducode, if i had more time i would be adding seprate functions for each choice
    #implemented functions would be able to recall and save the sale amount without the user asking to every time
    #function would help to output report of all the cash out and cash at once at the end