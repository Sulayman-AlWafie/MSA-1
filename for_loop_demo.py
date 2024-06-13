def main():
    #print intergers between 0 and 10:
    for number in range(11):
        print(number)

    #print integers between 5 and 10
    print("\n\n")
    for number in range (5,11):
        print(number)

    #print even numbers between 0 - 10
    print("\n\n")
    for number in range(0, 11, 2):
        print(number)
    #prompt the user for start an stop value and print the number between start and stop
    #get the start value from the user and convert to an integer
    #get the stop value from the user and convert to an integer
    #use start and stop value in a for loop
    start_value = int(input("Enter an start value: "))
    stop_stop =  int(input("Enter a stop value: "))

    for number in range ( start_value, stop_stop):
        print(number)

main()
