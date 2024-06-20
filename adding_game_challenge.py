import random

# Ask the user what difficulty rating they woul like to play
def get_difficuly_input():
    while True:
        difficulty = input(" Please enter the difficulty of the game you would like to play:")
        if difficulty not in ["1","2","3"]:
            continue
        else:
            break
    return  int(difficulty)

def get_number_of_questions():
    list_of_numbers = ["3","4","5","6","7","8","9","10"]
    while True:
        number_of_questions = input("please enter the number of questions you would like(must be 3-10):")
        if number_of_questions not in list_of_numbers: 
            continue
        else:
            break
    return int(number_of_questions)

def main():
    difficulty = get_difficuly_input()
    number_of_questions = get_number_of_questions()
    #Ask the user the number of questions they entered using a for loop
    for question in range(number_of_questions):
        #inside the loop generate two random numbers based on the difficulty    
        if difficulty == 1:
            x = random.randint(1,9)
            z = random.randint(1,9)
        elif difficulty == 2:
            x = random.randint(10,99)
            z = random.randint(10,99)
        elif difficulty == 3:
            x = random.randint(100,999)
            z = random.randint(100,999)
        #calculate the correct answer
        correct_answer = x + z
        total_correct_answer = 0
        incorrect = 0
        while True:
            print()
            try:
                user_answer = int(input(f"{x} + {z} = "))
                
                if user_answer != correct_answer:
                    print("WRONG")
                    incorrect += 1

                    if incorrect == 3:
                        break
                    continue

                else:
                    print("CORRECT!!!!")
                    total_correct_answer += 1
                    break
            except:
                print("WRONG")
                incorrect += 1

                if incorrect == 3:
                    break
                continue
    score = total_correct_answer / number_of_questions*100
    print(f"{score}%")






        #inside a while loop. run while loop while incorrect answers is less than 4 
            #ask the question to the user and ask for their answer(use input function)
            #make sure that the answer given is correct using an if statement
            #if answer correct add 1 to correct answers print correct ,  and break the loop
            #else answer is incorrect display Wrong and add 1 to the number_of_tries
            #if user gets the question wrong three times print the correct answer


main()

