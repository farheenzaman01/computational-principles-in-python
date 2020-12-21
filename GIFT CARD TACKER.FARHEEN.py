def addgiftcard(code, giftcard_dic):#storing gift card ammount to the assigned codes to create a new card
    if code < 10000:
        print("Invalid code")
        return
    elif code >= 50000:
        c = "$5"
    elif code in range(40000, 50000):
        c = "$4"
    elif code in range(30000, 40000):
        c = "$3"
    elif code in range(20000, 40000):
        c = "$2"
    elif code in range(10000, 20000):
        c = "$1"
        
    if c in giftcard_dic:
        giftcard_dic[c] += 1

def removegiftcard(code, giftcard_dic):#storing gift card ammount to the assigned codes for removal
    if code < 10000:
        print("Invalid code")
        return
    elif code >= 50000:
        c = "$5"
    elif code in range(40000, 50000):
        c = "$4"
    elif code in range(30000, 40000):
        c = "$3"
    elif code in range(20000, 40000):
        c = "$2"
    elif code in range(10000, 20000):
        c = "$1"
        
    if c in giftcard_dic:
        giftcard_dic[c] -= 1

def report(giftcard_dic): #FUNCTION TO SHOW REPORT BASED OFF USERINPUT KEYS
    c = n = tot = 0
    print("You have:")
    for key in giftcard_dic:
        k = key
        val = giftcard_dic[key]
        print("    ",val,key+"-card")
        c += val
        d = int(key[-1])
        tot += d*val
        if val > 0:
            n += 1
    avg = tot/n
    print("Total:",str(c)+" cards.")
    print("Average:$" + str(round(avg,2)))

ch = 1
giftcard_dic = {"$5":0, "$4":0, "$3":0, "$2":0, "$1":0}
while ch != 0:
    print()
    print("Gift Card Tracker") #MAIN MENU
    print("1- Add Gift Card")
    print("2- Remove Gift Card")
    print("3- Report")
    print("0- Exit")
    ch = input("Choice: ")
    ch = int(ch)
    if ch in range(0,4):#asking using for userinput for gift code
        if ch == 1 or ch == 2:
            code = input("Code: ")
            code = int(code)
        if ch == 1:#putting created function as output to user choices
            addgiftcard(code, giftcard_dic)
        elif ch == 2:
            removegiftcard(code, giftcard_dic)
        elif ch == 3:
            report(giftcard_dic)
    else:
        print("Invalid ")