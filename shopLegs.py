class ShopALM:

    # An initializer method that accepts two parameters
    # - A parameter corresponding to the name of the food
    # - A parameter corresponding to the amount of the food (in pounds) to order
    def __init__(self, food, amount):

        # The name of the food - to be updated using the food parameter
        self.food = food

        # The amount in pounds - to be updated using the amount parameter
        self.amount = amount

        # The calculated price of the ordered item (based on amount ordered) – to be
        # updated using a public method
        self.total = 0

        # The standard prices of the food items per pound
        self.prices = {
            'Dry Cured Iberan Ham'  : 177.80,
            'Wagyu Steaks'          : 450.00,
            'Matsutake Mushrooms'   : 272.00,
            'Kopi Luwak Coffee'     : 306.50,
            'Moose Cheese'          : 487.20,
            'White Truffles'        : 3600.00,
            'Blue Fin Tuna'         : 3603.00,
            'Le Bonnotte Potatoes'  : 270.81,
        }

    # Accessoor method
    def __str__(self):

        # If food name is within price list
        if self.food.title() in self.prices.keys():
            print("You've given:")
            print(f"Food Name\t: {self.food.title()}")
            print(f"Food Price\t: {self.prices[self.food.title()]}")
            
        # if food name not within price list
        else:
            print("ERROR: Given food is not within list")
    
    # A public method to calculate the cost of the ordered food.
    def calculatePriceALM(self):
        if self.food.title() in self.prices.keys():
            self.total = self.amount * self.prices[self.food.title()]
        else: 
            self.total = 0
        return self.total