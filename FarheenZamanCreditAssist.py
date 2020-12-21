

# credit assist

#input from user
income = float(input("Income??"))
debt = float(input("Debt??"))
minPay = float(input("minPay??//"))




#calculating and evaulating

if debt > (6 * income):
    print("LOAN DECLINED")
else:
    credit = float(income - minPay)*0.3

#output
print ("you now have store credit of : $")
print  (credit)




