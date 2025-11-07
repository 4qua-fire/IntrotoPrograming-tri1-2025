import random
number = random.randint(1,10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000)
history  = []
while number not in history:
    while True:
        try: 
            guess = int(input("Guess the number\n>"))
            if guess in history:
                print("you already guessed that dingus") 
            else: break       
        except: print("you must guess a number")
    history.append(guess)
    if guess == number:
        print(f"You got it\n it took you {len(history)} guesses")
    elif guess > number:
        print(f"The number is less than {guess}")
    elif guess < number:
        print(f"The number is greater than {guess}")