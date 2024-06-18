def main():

    menu_prices = {
        "Baja Taco": 4.00,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }
    total = 0
    while True:
        customer_order = (input("Please enter what you would like to order:"))
        if customer_order.lower() == ("end"):
            break
    
        try:
            price = menu_prices[customer_order]
        except KeyError:
            continue
        
        total = total + price

        print(f" Total: ${total}")


      
            
       
main()
