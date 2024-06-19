import random
# Ask the user what difficulty rating they woul like to play
def get_difficuly_input():
    while True:
        difficulty = input(" Please enter the difficulty of the game you woul like to play")
        if difficulty not in ["1","2","3"]:
            continue
        break
    return int(difficulty)
def get_number_of_questions():
    #prompt the user for how many questions they would like,(must be between 3-10)
    number_of_questions = input("please enter a number of questions between 3 and 10")
    while True:
        if number_of_questions != "3" or"4" or "5" or "6" or "7" or " 8" or "9" or "10":
            continue
        break
    return number_of_questions

def main():
    # if the user chooses a difficult of one the program should be able to give the user equations with a difficulty of 1 and should generate number_of_question amount

    difficulty = get_difficuly_input()
    print(difficulty)
main()
