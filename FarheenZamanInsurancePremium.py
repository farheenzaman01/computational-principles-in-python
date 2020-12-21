baseCost = 50
#user input
print("age of driver??")
#age validaing calculation
age = int(input())
if age<25:
   baseCost =  baseCost = + 100
elif age<35:
    baseCost =  baseCost = + 20
#user input
print(" number of accidents in last 5 years??")
#accident charges calculation
accd= int(input())

if accd ==2:
   baseCost = baseCost + accd*40
elif accd ==3 or accd ==4:
   baseCost = baseCost + accd*60
elif accd>4:
   baseCost = baseCost - 50
   #output
print(" monthly premium for the driver is Below") 
print(baseCost)    