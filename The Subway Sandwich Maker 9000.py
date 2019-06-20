### subway sandwich maker 9000
### generate a random sandwich
### add ingriedients to lists 
### dont mess up
### prob put in a selection thing 
### prob not
### stuff

import random
import time

size = [
		"6 Inch ",
		"Footlong "
]

bread = [
		"Wheat ",
		"Italian ",
		"Italian Herbs and Cheese ",
		"Honey Oat ",
		"Monterey Cheddar ",
		"Garlic ",
		"Flat ",
]

meat = [
		"Roast Beef",
		"Cold Cut Combo",
		"Tuna",
		"Chicken Breast",
		"Meatball Marinara",
		"Chicken Strips",
		"Chicken Bacon Ranch",
		"Chicken Pizziola",
		"Chicken Marinara",
		"Spicy Italian",
		"Pizza Sub",
		"Turkey Club",
		"Turkey Ham",
		"Ham",
		"Chicken Teriyaki",
		"Buffalo Chicken",
		"Philly Steak",
		"Big Philly Cheesesteak",
		"Veggie Delite",
		"Subway Melt",
		"BLT"
]

extra_meat = [
		"extra Bacon, ",
		"extra Pepperoni, ",
		"extra beef, ",
		"extra chicken, ",
		"extra ham, ",
		"extra turkey, ",
		"extra steak, ",
		"no extra meat, "
]

cheese = [
		"American cheese, ",
		"Provolone cheese, ",
		"Pepperjack cheese, ",
		"Monterey Cheddar cheese, ",
		"Mozzerella cheese, ",
		"no cheese, "
]

extra_cheese = [
		"extra cheese, ",
		"no extra cheese, "
]

toasty = [
		"toasted, ",
		"not-toasted, "
]

veggies = [
		"Spinach, ",
		"Lettuce, ",
		"Tomatoes, ",
		"Green Peppers, ",
		"Onions, ",
		"Cucumbers, ",
		"Pickles, ",
		"Olives, ",
		"Banana Peppers, ",
		"Jalapeños, "
]

sauces = [
		"Light Mayonnaise, ",
		"Regular Mayonnaise, ",
		"Oil, ",
		"Vinegar, ",
		"Ranch, ",
		"Sweet Onion, ",
		"Chipotle Southwest, ",
		"Honey Mustard, ",
		"Buffalo Sauce, ",
		"Mustard, ",
		"Red Wine Vinaigrette, ",
		"Balsamic Vinaigrette, ",
		"no sauce, "
]

seasoning = [
		"Salt",
		"Pepper",
		"Oregano",
		"Parmesan Cheese",
		"no seasoning"
]


burger_graphic = r'''
                _....----"""----...._
             ./'  o    o    o    o   '\.
            /  o    o    o         o    \
           /     o      o   o     o    o \
         _|   o   o    o      o  o     o  |_
        / `''-----.................-----''` \
        \___________________________________/
          \~`-`.__.`-~`._.~`-`~.-~.__.~`-`/
           \                             /
            `-._______________________.-'    
'''

print(burger_graphic)
print("Hello! \n") 
print("Ya hungry? ")
print("Want a Subway sandwich? ")
print("Dont know what sandwich to get? ")
print("\nWell let me introduce the Subway Sandwich Maker 9000! ")
print("\nThis script thing will generate a sandwich for you so you can spend less time thinking about what sandwich to get, ")
print("and more time thnking about more important things in life. ")
print("Enjoy! ")
input("\nPress 'enter' to think about more important things in life. ")

print("\nNow, time for the sandwich! ")

print("\nSo what kind of sandwich were you hoping to get? ")
time.sleep(1.5)
print("\nDON'T CARE!! ")

print("\nLETS SEE WHAT YOU'RE EATING TODAY! ")
time.sleep(1)
print("\nMAKING")
time.sleep(1)
print("SANDWICH")
time.sleep(0.5)
print("beep")
time.sleep(0.5)
print("boop")
time.sleep(0.5)

print("\nYou'll have a " + random.choice(size) + random.choice(meat) + " on " + random.choice(bread) + "bread, " + random.choice(extra_meat) + random.choice(cheese) + random.choice(extra_cheese) + random.choice(toasty) + random.choice(veggies) + random.choice(veggies) + random.choice(veggies) + random.choice(sauces) + "and " + random.choice(seasoning) + ".")

while True:
	second_sandwich = input("\nThat should hold you for lunch, unless you want another? (yes or no) ")
	if second_sandwich == 'yes':
		print("\nAlright! Lets make another one! ")
		time.sleep(1)
		print("MAKING")
		time.sleep(1)
		print("SANDWICH")
		time.sleep(0.5)
		print("beep")
		time.sleep(0.5)
		print("boop\n")
		time.sleep(0.5)
		print("\nYou'll have a " + random.choice(size) + random.choice(meat) + " on " + random.choice(bread) + "bread, " + random.choice(extra_meat) + random.choice(cheese) + random.choice(extra_cheese) + random.choice(toasty) + random.choice(veggies) + random.choice(veggies) + random.choice(veggies) + random.choice(sauces) + "and " + random.choice(seasoning) + ".")
	if second_sandwich == 'no':
		print("\nAlright then, thank you for using the Subway Sandwich Maker 9000! ")
		time.sleep(1)
		print("THANK")
		time.sleep(1)
		print("YOU!")
		time.sleep(0.5)
		print("beep")
		time.sleep(0.5)
		print("boop")
		time.sleep(0.5)
		input("\nPress 'enter' to leave and eat your sandwich. ")
		exit(0)
