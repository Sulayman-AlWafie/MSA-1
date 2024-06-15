#create a program that accepts a hightway# and outputs the direction
#user enters: 95
#Output: Interstate 95 run South to North
#Error check program so that it doesn't crash

def main():
    while True:
        number = int(input(" Please enter a highway number"))
        remainder = number % 2
        if remainder == 0:
            print(" Hight way goes east to west and vice versa")
        if remainder == 1:
            print("Highway runs north to south and vice versa")
            continue
        break
    while True:
        number_2 = int(input(" Please enter a highway number"))
        number_3 = number_2 - number
        if number_3 == 0:
            print("Error: cannot enter same number")
        elif number_3 < 0:
            print("You are going south or west ")
        else: number_3 > 0
        print(f"Highway run north or east")
        break
    return number
main()

