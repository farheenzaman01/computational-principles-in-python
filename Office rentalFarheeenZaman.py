total_money = 0
count = 0
#display main menu

another = 'y'
while(another=='y'):
 print("Welcome to our office rental calculator")
 print('Need Office Space?')
 print('1- Private Office')
 print('2- location')
 print('3- Temporary Workspace')
 option = input('What type of space? ')
 
 spaceCharge = 0
 phone_charges = 0
 #declare the options  using if else statement
 if option=='1':
  spacecharges = spaceCharge + 1000
 elif option=='2':
  spaceCharge = spaceCharge+ 500
 elif option=='3':
     #calculating total cost of charge
  days = int(input('number of days do you need? '))
 spaceCharge = spaceCharge + (days*60)
  
 phone = input('Phone service? (Y/N) ')
 if phone=='y':
  minutes = int(input('How many minute do you need? '))
  #calculating total phonge
 phone_charges = phone_charges + (minutes*0.50)
  
 print('Your total monthly charge is $'+str(spaceCharge+phone_charges))
  #declaring the variable to calculate the averyage value
 count = count+1
 total_estimate = total_money + spacecharges + phone_charges
 #asking user if they want a new calculation
  
 another = input('Another quote(y/n)? ')
 
 print('Your Average quotation provided was $'+str(total_estimate/count))