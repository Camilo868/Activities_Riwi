

print("Welcome to my Inventory")
# start the program
ingresar=input("Do you want start the program?(SI/NO) ").lower()

while ingresar == "si":
    # Name of the product
    name=input("Enter the name of the product: ")
    
    while True:
        #error handling
        try:
            precio= float(input("Enter the price of the product: ")) #price of product
            quantity=int(input("Enter the quantity: ")) # Quantity of product
            
            if precio < 0 or quantity < 0:  #parameters of error in price and quantity

                print("This values can't a number negative.")
                continue
            break

        except:
            print("Value incorrect") #when enter an incorrect value

    ingresar=input("Do you want start the program?(SI/NO) ").lower() #it backs to the start

print("chao") #the end

