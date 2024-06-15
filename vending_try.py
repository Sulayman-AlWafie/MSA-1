def main():
    amount_due = 50
    print(f"Amount Due: {amount_due}")
    while True:
        coin = int(input("Please enter 25,10,5,1:"))
        amount_due = amount_due - coin 
        print(f"Amount Due {amount_due}")
        if amount_due < 0:
            print(f"Return Amount{amount_due}")
        
        

       







main()
