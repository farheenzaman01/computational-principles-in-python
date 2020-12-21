n = int(input("How many months"))

payment = 1
print("month $",payment)
#for m in range(n):
m = 0  
 
while m < n:
    p = payment
    
    payment = payment + p
    
    if m % 2 == 0 :
         print("Month: $",payment)
         m = m + 1
         continue
         
       # payment = payment *2
    # else:
      
    payment = payment + p
    print("month :$",payment)
    m = m + 1
     

        