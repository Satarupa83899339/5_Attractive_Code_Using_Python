#python-project:-1
import random

number = random.randint(1,10)

for i in range(3):
    user = int(input("Guess the number(1-10): "))
    
    if user == number:
        print(f"Hurray! You gussed the number right, it's{number}.")
        break
    else:
        print("Wrong guess.Try again!")
        
if user != number:
    print(f"Sorry, you've used all attempts. The number was {number}.")
