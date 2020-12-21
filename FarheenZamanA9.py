f=open("input.txt",'r')
s=f.read() 

lines=s.split("\n")
priceMax=0
priceMin=9999
total=0
for line in lines:
#print(line)
 cols=line.split(" ")
price=(float)(cols[1])
total=total+price
if(price>priceMax):
 priceMax=price
if(price<priceMin):
 priceMin=price
f.close()
f=open("output.txt",'w')
f.write("*******************************************\n")
f.write(" TICKET REPORT\n")
f.write("*******************************************\n\n")
f.write("There are " + str(len(lines)) + " tickets in the database.\n\n")
f.write("Maximum Ticket price is $" + str(priceMax) + "\n")
f.write("Minimum Ticket price is $" + str(priceMin) + "\n")
f.write("Average Ticket price is $" + str(total / len(lines)) + "\n\n")
f.write("Thank you for using our ticket system!\n\n")
f.close()

print("File Created sucessfully")