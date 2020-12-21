class Ticket:
    def __init__(self,ticket_num,amount,plate_num):
        self.ticketNumber=ticket_num
        self.amount=amount
        self.plateNumber=plate_num
        self.paid=False
# changing the status of the current ticket to true
    def changeStatus(self):
        self.paid=True

    def getPlateNum(self):
        return self.plateNumber
# returns the ticket number
    def getTicketNum(self):
        return self.ticketNumber
# returns the amount
    def getAmount(self):
        return self.amount
#returns the status of teh ticket paid ot unpaid
    def getStatus(self):
        return self.paid
#lists holds all the tickets
tickets =[]
# function to create a new parking ticket
def createNewParking():
    ticketnum= input(" ticket number ?: ")
    amt =input(" dollar amount?: ")
    platenum=input(" plate number?: ")
#created a new ticket and append it into the previous list
    newTicket=Ticket(ticketnum,amt,platenum)
    tickets.append(newTicket)
    print("Ticket added !")
# functions for payment of a ticket
def payTicket(ticketnum):

    for ticket in tickets:
# checking if the number of current ticket is same as that of the passed one, to chanage status
        if ticket.getTicketNum() == ticketnum:
            ticket.changeStatus()
            print("Thank you for payment")
            return
        print("Invalid ticket")
# function to report all the ticket for plate number
def reportByPlateNum(plateNum):
    sum =0
    print("Ticket associated with the above plate:")
  
    for ticket in tickets:
# checking for ticket number
        if ticket.getPlateNum()==plateNum:
            print(ticket.getTicketNum())
            sum+=float(ticket.getAmount())
#also sum the amount of the ticket
            print("Total amount owed : ",sum)
#function to print all the tickets and the status
def grandReport():
#count the number of paid and unpaid tickets
    paid =0
    unpaid=0
# headings
    print("{0:<15}{1:<15}{2:<15}{3:<15}".format("Ticket Number","Plate Number","Amount","Status"))

    for ticket in tickets:
#display status of ticket
        if ticket.getStatus()==True:
            paid+=1
            print("{0:<15}{1:<15}{2:<15}{3:<15}".format(ticket.getTicketNum(), ticket.getPlateNum(), ticket.getAmount(),"Paid"))
        else:
            unpaid+=1
            print("{0:<15}{1:<15}{2:<15}{3:<15}".format(ticket.getTicketNum(), ticket.getPlateNum(), ticket.getAmount(), "Unpaid"))
            print("sum of paid Tickets: ",paid)
            print("sum of unpaid Tickets: ", unpaid)
#method to show user the choices
def menu():
    print("1. Create New Parking Ticket")
    print("2. Parking Ticket Payment")
    print("3. Reports of Plate Number")
    print("4. Generate Grand Report")
    print("5. Exit")
#main  running functiom of the program
def main():
#run a loop, wille exit when user chooses to do so
    while True:
#show the menu
        menu()
#asl users choice
    choice =int(input(" choice?: "))

    if choice == 1:
        createNewParking()
    elif choice==2:
        ticketnum=input(" ticket number?: ")
        payTicket(ticketnum)
    elif choice==3:
        platenum = input(" plate number?: ")
        reportByPlateNum(platenum)
    elif choice==4:
        grandReport()
    elif choice==5:
        print("Thank you GoodBye")
        exit(0)
    else:
        print("Invalid Choice , try again!")

if __name__=="__main__":
    main()