

print("Welcome to my Inventory")
# start the program
ingresar=input("Do you want start the program?(YES/NO) ").lower()

while ingresar == "yes":
    # Name of the product
    name=input("Enter the name of the product: ")
    
    while True:
        #error handling
        try:
            precio= float(input("Enter the price of the product: ")) #price of product
            quantity=int(input("Enter the quantity: ")) # Quantity of product
            if precio < 1 or quantity < 1:  #parameters of error in price and quantity

                print("You can't buy lower than 1")
                continue
            # The total cost is calculated here
            total_cost=precio*quantity
            #show the result
            print(f"You're going to take {quantity} of the product {name} with the price of {precio}. The total is {total_cost} ")
            break

        except:
            print("Value incorrect") #when enter an incorrect value

    ingresar=input("Do you want start the program?(YES/NO) ").lower() #it backs to the start

print("GOOD BYE") #the end of the program

# This program simulates a simple inventory purchase system.
# It asks the user if they want to start the program and then requests
# the product name, price, and quantity. It validates that the user
# enters correct numeric values and that they are greater than 0.
# After that, it calculates and displays the total cost of the product.
# The program repeats until the user decides to exit.
