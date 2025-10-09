import random

number = random.randint(1, 20)
print("Welcome To The Guess The Number Game")
no_of_attempts = 0
attempts = 10 #by deafult attempts value
isStart = False
gameOn = True
win = 0
loss = 0



while gameOn :
    difficulty = int(input("Enter the difficulty in no. (1:Easy, 2:Medium, 3:Hard): "))
    if difficulty == 1:
        number = random.randint(1, 10)
        attempts = 7
        isStart = True
        max_number = 10
    elif difficulty == 2:
        number = random.randint(1, 20)
        attempts = 10
        isStart = True    
        max_number = 20
    elif difficulty == 3 :
        number = random.randint(1, 50)
        attempts = 12
        isStart = True
        max_number = 50
    else:
        print("Invalid Input try again")
    
    if isStart :
        while no_of_attempts < attempts:
            print(f"Guess the number between 1 to {max_number}")
            usernumber = int(input())
            no_of_attempts += 1
            if usernumber == number:
                print("Congratulations! You guessed in ", no_of_attempts , "attempts")
                win += 1
                break
            elif usernumber> number :
                print("Too High!")
                print(f"Attempt left {attempts - no_of_attempts}")
            elif usernumber < number :
                print("Too Low!")
                print(f"Attempt left {attempts - no_of_attempts}")
                
            if no_of_attempts == 5 and number % 2 == 0:
                print("Number is even")
            elif no_of_attempts == 5 and number % 2 != 0:
                print("Number is odd")
        else: 
            print("Game Over! The number was:", number)
            loss += 1
        print("Do You Want To Play Again (Y/N)")
        play_again = str(input()).upper()
        if play_again == "Y":
            gameOn = True
            no_of_attempts = 0
        elif play_again == "N":
            gameOn = False
            print("Thank you for playing")
            print(f"You win {win} Times & Lose {loss} Times")