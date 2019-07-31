#imports the ability to get a random number (we will learn more about this later!)
from random import *

#Create the list of words you want to choose from.


#Generates a random integer.


Sides = ["Fries", "Salad", "Soup", "Nachos", "Pretzels"]
print("")
MainCourses = ["Grilled Cheese", "Pizza", "Burrito", "Sushi", "Pasta"]
print("")
Desserts = ["Brownie", "Mousse", "Cheesecake", "Cake", "Gelato"]
print("")
Drinks = ["Water", "Soda", "Sweet Tea", "Orange Juice", "Milkshake"]
print("")

aList = [0, 1]
sidesIndex = randint(0, len(Sides)-1)
mainIndex = randint(0, len(MainCourses)-1)
DessertsIndex = randint(0, len(Desserts)-1)
DrinksIndex = randint(0, len(Drinks)-1)

print ("Your order will be:")
print (MainCourses[mainIndex] , " with a side of", Sides[sidesIndex] ,  Desserts[DessertsIndex] , "for dessert, and" , Drinks[DrinksIndex])
