def run():
 depth = float(input(' depth?: '))
 width = float(input(' width?: '))
 height = float(input(' height?: '))
 thickness = float(input(' thickness?: '))

 area1 = depth * height
 area2 = width * height

 unit_price = 1.49 
 # unit price to be applied, based on total area
 if area1 + area2 >= 3000:
  unit_price = 1.29
 if area1 + area2 >= 6000:
  unit_price = 0.99

surcharge = 0 
# surcharge to be added, based on thickness
 if thickness >= 0.375:
   surcharge = 0.2
 if thickness >= 0.5:
  surcharge = 0.5
 
discount_code = input('Enter discount code: ')
discount = 0 
# discount to be added based on discount code
 if discount_code == '112233':
 discount = 0.2
 elif discount_code == '111222':
 discount = 0.1
 elif discount_code != '0':
 print('Discount code is invalid!')
# calculating unit price and area
basic_price = unit_price * (area1 + area2) 
# ading surcharge on top of basic price
surcharged_price = basic_price + surcharge * basic_price 
# apply discount on surcharged price to get final price

finalPrice = surcharged_price - discount * surcharged_price  
print('Price:', finalPrice)

while True:
 choice = int(input('Enter 1 to calculate price, 2 to exit: '))
if choice == 1:
 run()
elif choice == 2:
 print ("Goodbye!")