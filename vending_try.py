def main():
    amount_due = 50
    
    while True:
        print(f"Amount Due {amount_due}")
        coin =  input("Please enter 25,10,5,1:")
        if (coin.isnumeric()):
            coin = int(coin)
            if((coin) == 1 or (coin) == 5 or (coin) == 10 or (coin) == 25):
                amount_due = amount_due - coin
            else:
               print("Error: Please enter a 1, 5, 10, or 25")  
        else:
            print("Error: Please enter a 1, 5, 10, or 25")
        if amount_due < 0:
            print(f"Return Amount {amount_due * -1} gyatt")
            break







main()
