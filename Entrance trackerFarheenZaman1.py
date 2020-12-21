# I created a progra for a user to sign in using their name a
#program records the number of people each user is signing in
#Program detects if the building is exceeding capacity
#proogram signs out user out of the system
#prpgram reports the signed in people (min/max) by one user

#declaring the function to ask the user for the number of sign is getting input
def entranceTracker():
    try:
        print("welcome to our service building, Please sign in")
        name = str(input("Enter your name to sign in: "))
        
        entry = float(input('Enter the number of people you want to sign in: '))
        if 1 <= entry <= 5:#condiitonal variable to limit sign ins to minimum 5 people
            return entry
        else:#send invalid message if the user enters more than higher capacity
            print('Error: Building cannot be occupied by more than 5 sign in')
            return None
    except:
        print('Error: Invalid number')
def main():
    repeat = 'y'
    highest = 0
    lowest = 0
    total = 0
    count = 0
    while repeat == 'y':
        entry = entranceTracker()
        if entry == None: continue
        if count == 0:
            lowest = highest = entry
         
        else:#declare that the building is at high capacity if the number is higher than 5
            if highest < entry:
                print('Currenty building is the highest capacity.'.format(entry))
                highest = entry
                
            elif lowest > entry:# declare vacancy for sign ins
                print('There is more  entry sign ins available .'.format(entry))
                lowest = entry
        total += entry
        count += 1
        repeat = input('Do you want to sign in more people?(y/n): ').lower()  # asking the user for more input      
     #printing   final output
    
    print('Highest capacity recorded  : {}'.format(highest))
    print('Lowest capacity Recorded   : {}'.format(lowest))
    print("Enjoy your stay,Goodbye")
    


main()# ending the main function
