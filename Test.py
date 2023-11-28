# This is a supermarket.
# It has multiple departments and different types of clerks and workers that can either interact or not with the customers

# Departments: Meat, Seafood, Deli, organic_foods, care_products, health_and_beauty, fruit, tet_items, snacks, bread_isle,
# condiments_isle, pasta_isle, alcohol_isle, bakery, dairy, produce, frozen, cereal, front_ens, back_end

# People: Cashiers, cooks, customers, cleaners, stockers, warehouse_workers, farmacists, wine_specialists, managers, supervisors.

# am / pm shifts, overnight crew

# Only manager can purchase inventory
# Only cooks allowed in kitchen
# no customes allowed in back_end area
# all customers and all workers can purchase, they need to have a wallet
# all itrms have a 'key: value' = 'item: price', prices to be deducted from wallet, if not enough money in wallet, pop and delete an itmem,
# this would be like a return
# inventory is affected by item purchased

print()
print("Welcome to Good Day; your neighborhood virtual supermarket!")


"""players = ["Tracey", "John", "Sue", "Will", "Bryan", "Brock"]
print("The players are: Tracey, John, Sue, Will, Bryan, Brock")
customer = input(
    "Please select a player by entering the name of the player: ")
if customer in players:
    print("Ok, so you choose: ", customer)

else:
    print("Please choose one of the players above")
input("Please press enter to see details about " + customer)"""


# CUSTOMER CLASS STARTS HERE


class Customer:
    def __init__(self, first, last, budget):
        self.first = first
        self.last = last
        self.budget = budget

    def info(self):
        return "Got it! You are " + self.first + " " + self.last + " with a budget of " + self.budget + " dollars to spend."
        # return '{}{}{}'.format(self.first, self.last, self.budget)


first = input("please enter your first name: ")
last = input("please enter your last name: ")
budget = input("please enter your shopping budget amount: ")

cust_1 = Customer(first, last, budget)
print(cust_1.info())

response1 = input("Is this correct? ")

"""
cust_1 = Customer('Tracey', 'Spencer', '$250')
cust_2 = Customer('John', 'Stur', '$100')
cust_3 = Customer('Sue', 'Kind', '$230')
cust_4 = Customer('Will', 'Krog', '$125')
cust_5 = Customer('Bryan', 'Crot', '$200')
cust_6 = Customer('Brock', 'Nell', '$180')

print(cust_1.info())
print(cust_2.info())
print(cust_3.info())
print(cust_4.info())
print(cust_5.info())
print(cust_6.info())

"""

# CUSTOMER CLASS ENDS HERE


print()
print("We have a vast variety of departments stocked with some of the best products, where would you like to start", first + "?")
print()


departments = ["Meat", "Seafood", "Deli", "Organic Foods", "Care Products", "Health and Beauty", "Fruit", "Snacks", "Bread",
               "Condiments", "Pasta", "Alcohol", "Bakery", "Dairy", "Produce", "Frozen", "Cereal", "Front end", "Back end"]


meat = ["Pork", "Chicken", "Beef", "Lamb", "Goat",
        "Turkey", "Duck", "Buffalo", "Goose", "Rabbit"]
meat.sort()
seafood = ["Shrimp", "Salmon", "Prawns", "Scallops", "Bass", "Sea Bass", "Cod", "North Atlantic Cod",
           "Sandab", "Sole", "Crab", "Lobster", "Clams", "Mussels", "Crab legs", "Scottish Salmon"]
seafood.sort()
deli = ["Savory Whole Chicken", "Garlic Whole Chicken", "Potatoe Salad", "Macaroni Salad", "Classic Hummus", "Mustard Potatoe Salad", "Roasted Chicken", "Roasted Red Pepper Hummus", "Athenos Feta", "Black Forrest Ham",
        "Southern Style Potatoe Salad", "Oven Roasted Turkey", "Deviled Egss Potatoe Salad", "BBQ Ribs", "Coleslaw", "Tortilla Chips", "Guacamole", "Pico de Gallo", "Salsa Mexicana", "Naan Dippers", "Spinach Artichoke Dip"]
deli.sort()
organic = ["Strawberries", "Spinach", "Kale", "Collards", "Mustard Greens",
           "Nectarines", "Apples", "Grapes", "Bell Peppers", "Hot Peppers", "Cherries"]
organic.sort()
care_products = ["Cleanser", "Shampoo", "Lotion", "Toner", "Soap", "Toothpaste", "Eye Cream",
                 "Tooth Brushes", "Baby Shampoo", "Lip Sticks", "Cosmetics", "Creams", "Sunscreens", "Fragrances", "Dental Care", "Eye Care"]
care_products.sort()
health_beauty = ["Face Primer", "Foundation", "Concealer", "Face Pouder", "Rouge", "Blush", "Highlighter", "Bronzer", "Contour Powder", "Makeup Remover",
                 "Nail Polish", "Nail Polish Remover", "Eyebrow Pencils", "Eye Primer", "Mascara", "Lip Balm", "Lip Gloss", "Lip Sticks", "Setting Spray"]
health_beauty.sort()
fruit = ["Apple", "Mango", "Watermelon", "Grape", "Orange", "Strawberry", "Kiwi", "Avocado", "Cherry", "Pineapple", "Banana", "Pear",
         "Blueberry", "Peach", "Grapefruit", "Papaya", "Apricot", "Plum", "Raspberry", "Pomegranate", "Fig", "Cranberry", "Guava", "Lime"]
fruit.sort()
snacks = ["Popcorn", "Trail Mix", "Potatoe Chips", "Cookies", "Bhel Puri", "Cookies", "Papri Chaat", "Crackers", "Aloo Tikki", "Dried Fruit",
          "Banana Chips", "Hummus", "Edamame", "Cheese", "Cheese Puffs", "Doritos", "Cheetos", "Totopos", "Guacamole", "Tortilla Chips"]
snacks.sort()
bread = ["White", "Wholewheat", "Rye", "Sourdough", "Multigrain", "Baguette", "Ciabatta",
         "Pumpernickel", "Challah", "Brioche", "Flatbread", "Bagel", "Focaccia", "Cornbread", "Sodabread"]
bread.sort()
condiments = ["Yellow Mustard", "Relish", "Vinegar", "Wasabi", "Hot Sauce", "Dijon Mustard", "Mayonnaise", "Ketchup", "Barbecue Sauce", "Soy Sauce",
              "Burger Toppings", "Pretzel Toppings", "Potatoe Salad", "Marinades", "Chutneys", "Preservatives", "Salad Dressings", "Tomatoe Sauces", " Pickled Foods"]
condiments.sort()
pasta = ["Angel Hair", "Bowtie", "Farfalle", "Bucatini", "Ditalini", "Egg Noodles", "Fettuccine", "Fusilli", "Gemelli", "Gnocchi", "Lasagna", "Linguine", "Macaroni",
         "Manicotti", "Orecchiette", "Orzo", "Penne", "Radiatore", "Ravioli", "Rigatoni", "Rotelle", "Rotini", "Shells", "Spaghetti", "Tagliatelle", "Tortellini", "Vermicelli", "Ziti"]
pasta.sort()
alcohol = ["beer", "ale", "wine", "red wine", "white wine", "champagne", "vodka",
           "cognac", "brandy", "whiskey", "whisky", "gin", "rum", "liqueur", "cocktail", "punch"]
alcohol.sort()
bakery = ["roll", "bread roll", "sesame roll", "poppy seed roll", "cinnamon roll", "crescent roll", "croissant", "bagel", "hamburger bun", "hot dog bun", "cracker", "biscuit", "cookie", "toast", "breadstick", "pretzel", "hardtack", "ship biscuit", "wafer",
          "waffle", "crouton", "knish", "pizza", "muffin", "blueberry muffin", "raisin muffin", "sour cream biscuit"]
bakery.sort()
dairy = ["milk", "whole milk", "skim milk", "low fat milk", "nonfat milk", "pasteurized milk", "2% milk", "Vitamin D", "dry milk", "condensed milk",
         "yogurt", "kefir", "sour milk", "buttermilk", "cream", "sour cream", "butter", "cottage cheese", "farmers cheese", "homemade cheese", "cream cheese"]
dairy.sort()
produce = ["tomato", "cucumber", "carrot", "beet", "potato", "onion", "green onions", "spring onions", "leek", "sweet pepper", "red pepper", "green pepper", "yellow pepper", "paprika", "hot pepper", "chili pepper", "cabbage", "cauliflower", "broccoli", "brussels sprouts",
           "collard", "kale", "kohlrabi", "mushrooms", "lettuce", "spinach", "celery", "asparagus", "artichoke", "cress", "watercress", "chicory", "endive", "garlic", "eggplant", "aubergine", "squash", "gourd", "zucchini", "pumpkin", "turnip", "parsnip", "radish", "horse radish"]
produce.sort()
frozen = ["Salmos", "Chicken", "Ground Beef", "Ground Pork", "Ground Chicken",
          "Sea Bass", "Mussels", "Crab", "Calamari", "Edemame", "Squid", "Fruit", "Vegetables"]
frozen.sort()
cereal = ["Cornflakes", "Muesli", "Oats", "Porridge", "Granola", "Rice Krispies", "Wheat Flakes", "Bran Cereal", "Cheerios",
          "Bunuelitos", "Batman Cereal", "Aquaman Cereal", "Capitan Crunch", "Cars 2", "Cars 3", "Cinnamon Chex", "Coco Roos"]
cereal.sort()
front_end = []
front_end.sort()
back_end = [""]
back_end.sort()


departments.sort()
departments_length = len(departments)
index = 0
while index < departments_length:
    print((departments[index]))
    index += 1
department = input("Please enter the department you'd like to start:")
# Check if the department exists in the departments list
if department in departments:
    print("Ok, let's head on over to", department)
    print("This is what you can find in", department + ":")
else:
    print("Please choose one of the departments above")

if department == "Meat":
    # print(meat)
    meat_length = len(meat)
    index = 0
    while index < meat_length:
        print((meat[index]))
        index += 1

if department == "Seafood":
    # print(seafood)
    seafood_length = len(seafood)
    index = 0
    while index < seafood_length:
        print((seafood[index]))
        index += 1

if department == "Alcohol":
    # print(alcohol)
    alcohol_length = len(alcohol)
    index = 0
    while index < alcohol_length:
        print((alcohol[index]))
        index += 1

if department == "Dairy":
    # print(dairy)
    dairy_length = len(dairy)
    index = 0
    while index < dairy_length:
        print((dairy[index]))
        index += 1

if department == "Produce":
    # print(produce)
    produce_length = len(produce)
    index = 0
    while index < produce_length:
        print((produce[index]))
        index += 1

if department == "Bakery":
    # print(bakery)
    bakery_length = len(bakery)
    index = 0
    while index < bakery_length:
        print((bakery[index]))
        index += 1

if department == "Deli":
    # print(deli)
    deli_length = len(deli)
    index = 0
    while index < deli_length:
        print((deli[index]))
        index += 1

if department == "Organic Foods":
    # print(organic)
    organic_length = len(organic)
    index = 0
    while index < organic_length:
        print("Organic " + (organic[index]))
        index += 1

if department == "Care Products":
    # print(care_products)
    care_products_length = len(care_products)
    index = 0
    while index < care_products_length:
        print((care_products[index]))
        index += 1

if department == "Health and Beauty":
    # print(health_beauty)
    health_beauty_length = len(health_beauty)
    index = 0
    while index < health_beauty_length:
        print((health_beauty[index]))
        index += 1

if department == "Fruit":
    # print(fruit)
    fruit_length = len(fruit)
    index = 0
    while index < fruit_length:
        print((fruit[index]))
        index += 1

if department == "Snacks":
    # print(snacks)
    snacks_length = len(snacks)
    index = 0
    while index < snacks_length:
        print((snacks[index]))
        index += 1

if department == "Bread":
    # print(bread)
    bread_length = len(bread)
    index = 0
    while index < bread_length:
        print((bread[index]))
        index += 1

if department == "Condiments":
    # print(condiments)
    condiments_length = len(condiments)
    index = 0
    while index < condiments_length:
        print((condiments[index]))
        index += 1

if department == "Pasta":
    # print(pasta)
    pasta_length = len(pasta)
    index = 0
    while index < pasta_length:
        print("Pasta " + (pasta[index]))
        index += 1

if department == "Frozen":
    # print(frozen)
    frozen_length = len(frozen)
    index = 0
    while index < frozen_length:
        print((frozen[index]) + " (Frozen)")
        index += 1

if department == "Cereal":
    # print(cereal)
    cereal_length = len(cereal)
    index = 0
    while index < cereal_length:
        print((cereal[index]))
        index += 1

x = input("Please choose from the above list:")
shopping_cart = []
if x in meat or seafood or alcohol or dairy or produce or bakery or deli or organic or care_products or health_beauty or fruit or snacks or bread or condiments or pasta or frozen or cereal:
    # print(x)
    shopping_cart.append(x)
print("So far you have this in your shopping cart: " + str(shopping_cart))
print("... to be continued")
