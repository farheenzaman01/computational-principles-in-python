def addMember(member_list):
    # Ask user to enter id, age
    id = input('Enter your Member ID: ')
    age = int(input(' Member Age? '))

    # If age < youngest_age, member is youngest
    if youngest_age(member_list) > age:
        print('You are the youngest so far.')

    # If age > oldest_age, member is oldest
    if oldest_age(member_list) < age:
        print('You are the oldest so far')

    # Calculate fees
    if age <= 25:
        fee = 30
    elif age >= 55:
        fee = 15
    else:
        fee = 50
    # Add member to member_list
    member_list.append([id, age, fee])
    print('Your monthly fee is $' + str(fee))


def youngest_age(member_list):
    # Initially set youngest to  value 200
    youngest = 200

    # Iterate over member_list
    # If youngest > member_list[i][1], set youngest = member_list[i][1]
    for i in range(0, len(member_list)):
        if youngest > member_list[i][1]:
            youngest = member_list[i][1]

    # return youngest age (smallest age)
    return youngest


def oldest_age(member_list):
    # Initially set oldest to a smaller value
    oldest = 0

    # Iterate over member_list
    # If oldest < member_list[i][1], set oldest = member_list[i][1]
    for i in range(0, len(member_list)):
        if oldest < member_list[i][1]:
            oldest = member_list[i][1]

    # returning oldest age (largest age)
    return oldest


def report(member_list):
    total_members = len(member_list)  # calculate length of list
    total_fees = 0
    #  add all fees to totalfees
    for member in member_list:
        total_fees += member[2]
    # Calculate average fees
    average = total_fees // total_members
    average_age = 0
    #   add all age to average_age
    for member in member_list:
        average_age += member[1]
    # Calculate average age
    average_age //= total_members

    # Print report
    print('There are', total_members, 'members.')
    print('Total fees $' + str(total_fees) + ' from members.')
    print('Average fee per members is $' + str(average))
    print('Average member age is', average_age)
    print('Youngest member is', youngest_age(member_list), 'years old.')
    print('Oldest members is', oldest_age(member_list), 'years old.')


if __name__ == '__main__':

    choice = 1
    # Create a member_list which contain members overall report containing member details
    
    member_list = []
    while choice != 0:
        print('CLUB MEMBERSHIP TRACKER')
        print('1- Add Member\n2- Report\n0-Exit')
        choice = int(input('Choice: '))
        if choice == 1:
            addMember(member_list)
        elif choice == 2:
            report(member_list)
        elif choice == 0:
            print('Goodbye!')
        else:
            print('Invalid ')
        print()