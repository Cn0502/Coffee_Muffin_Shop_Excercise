
# setting variables for prices and a list for ship items
from ast import Is


menulist = ["coffee","muffin","tea","donut"]
muffprice = 4.00
coffeeprice = 5.00
donutprice = 3.50
teaprice = 4.50
prices = {menulist[0]:coffeeprice,menulist[1]:muffprice,menulist[2]:teaprice,menulist[3]:donutprice }
shopcart = {}
finalcost = 0
#prompt for customer or user displaying shop items and price 
print("Hello and welcome to The Coffee Muffin Shop.")
print("menu.........................price")
print("coffee.........................$5")
print("muffin..........................$4")
print("tea..............................$4.50")
print("donut............................$3.50")
# this is the Customer order loop using the variables defined to hold the values of price quantity and menu items as well as putting it through some logical statements
# making sure the inputs are correct and dont cause errors as well as looping back if the customer wants more to order.
while True :
  print("what would you like")
  order = input()
  print("how many would you like")
  amount = int(input())
  if isinstance(order,str) == True :
      
        if order.lower() == menulist[0] :
          finalcost += amount * coffeeprice
          shopcart[menulist[0]] += amount
  
        elif order.lower() == menulist[1]:
          finalcost += amount * muffprice
          shopcart[menulist[1]] = amount
        elif order.lower() == menulist[2]:
          finalcost += amount * teaprice
          shopcart[menulist[2]] = amount
        elif order.lower() == menulist[3]:
          finalcost += amount * donutprice
          shopcart[menulist[3]] = amount
        
  print("does that complete your order 'yes' or 'no' ")
  cashout = input()
  if cashout == "yes":
         break
  else : 
     pass   
else :
   print( "there was an error with your order make sure you typed in your order correctly")
   pass
# this where we output all the info for the costomer regarding what he bought and the cost

print("thanks for shopping at The Coffee Muffin Shop")   
print("receipt")
print("item......quantity.......price ")
# this for loop prints out the items quantity and prices in succession that the customer ordered and finally calculates the total of these at the bottom
x = 0
for i in shopcart:
  print(i,"......",shopcart[i],"......" ,prices[i]  * shopcart[i])
  x += 1
print("your total is",finalcost)