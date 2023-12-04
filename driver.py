# The driver program will import the class module you created.
from shopLegs import ShopALM

# A function that creates a list of objects. 
# The function accepts no parameters but returns the list of objects.
def shopListALM():

    # Make empty list
    shopList = []

    # Prompt the user for the number of items. This value will be used to determine
    # the number of repetitions for a necessary loop. (Make sure to include input
    # validation to ensure that the number of items purchases is at least 1.)
    num_of_items = 0
    while num_of_items < 1:
        num_of_items = int(input("Please enter how many items you would like to addd to your shopping list: "))
        print('---------------------------------')
    
    # Contain a loop that prompts the user for the name of the item and the amount
    # of the item in pounds. (Make sure to include input validation to ensure that the
    # number of pounds is greater than 0.) The loop should use this information to
    # create an object, and append the object to the list
    for order in range(num_of_items):
        print('=================================')
        item = input(f'Please enter name of Item {order+1}\t: ')
        amount = int(input(f'Please enter amount of Item {order+1}\t: '))
        shopList.append(ShopALM(item, amount))
        print('=================================')
    
    # Returns the list (once the loop is completed)
    return shopList

# A function to display the contents of the list.
# This function accepts a list of objects as a parameter but does not return a value.
def displayContentsALM(list):
    i = 1

    # Display the contents of each object in the list (all 4 attributes).
    # Make sure to include appropriate formatting for prices.
    for item in list:
        if item.food.title() in item.prices.keys():
            print('=================================')
            print(f'Item {i}:')
            print('---------------------------------')
            print(f'Shop Item name\t: {item.food.title()}')
            print(f'Amount of item\t: {item.amount}')
            print(f'Price per Pound\t: {item.prices[item.food.title()]}')
            print(f'Total price\t: {item.calculatePriceALM()}')
            print('=================================')
            i += 1
        else:
            print('=================================')
            print(f"ITEM ERROR:\n'{item.food}' is not an available item")
            print('=================================')
            
# A function that calculates the total cost of all items.
# Recall, your object will only have the cost of each item (based on the amount of pounds ordered for that item).
# This function accepts the list of objects as a parameter and returns a value.
def calcTotalCostALM(list):
    totalCost = 0

    # access the individual cost of each ordered item
    for item in list:

        # calculate the total cost of all the items in the list
        item.calculatePriceALM()
        totalCost += item.total
    
    # return the total cost
    return totalCost

# A main function
def mainALM():
    shopping_list = shopListALM()

    displayContentsALM(shopping_list)

    cost = calcTotalCostALM(shopping_list)
    print(f"You need to pay ${cost}, damn")

mainALM()