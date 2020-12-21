#list created to store menue details
names = ['Coffee',  'Pizza', 'Burger', 'Fries',  'Donut']
costs = {"a":5.00, "b":6.00, "c":7.00, "d":8.00, "e":0}
status = {"default":"Confirmed", "a":"Prepared", "b":"On Delivery", "c":"Delivered", "d":"Cancelled"}
#following class and object is supposed to store the costs and names of food together
class Food(object):
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def getprice(self):
        return self.price
    
    def __str__(self):
        return self.name + ' : ' + str(self.getprice())
    
def buildmenu(names, costs):
    menu = []
    for i in range(len(names)):
        menu.append(Food(names[i], costs[i]))
    return menu
def report(orders, status):
    print()
    print(status + " Orders:")
    count = 0
    sum = 0
# for loop to check the  status type in orders
    for order in orders:
        if status in orders[order]:
            print(status + " order ", order, orders[order][0])
#  sum of the orders
            for value in orders[order][0]:
                sum += value
                count+= 1 
                
    else:
        # print the report
        print("There are %d orders in %s state"%(count, status))
        if count!= 0:
            print("Average order amount is $%1.2f"%(sum/count))
            
            orders = {}
            Foods = buildmenu(names, costs)

   


while choice != 0:
      n = 1
      for el in Foods:
        print(n,'. ', el)
        n = n + 1
        print("Restaurant Ordering System")
        print("1- Place an Order")
        print("2- Change Order Status")
        print("3- Report")
        print("0- Exit")
choice = int(input("Choice:"))
while choice not in choices:
        print("Invalid Choice!")
        choice = int(input("Choice:"))


if choice == 1:
        order = int(input("Order num?"))
        while order in orders:
            print("order number  already in system")
            order = int(input("Order #:"))
            if choice == 2:
                order = int(input("Order #:"))
            if order not in orders:

                print("Cannot find order")
            else:
                print("Status")
                print("a- Prepared")
                print("b- On Delivery")
                print("c- Delivered")
                print("d- Cancelled")
        state = input("Set new order status: ")
        if state not in status:
            print("Invalid status!")
        
        else:
            orders[order][1] = status[state]
        if choice == 3:
            for key, value in status.items():
                report(orders, value)
  
        else:
            print ("bye")
        