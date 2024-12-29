import random 

def main():
    secret_number = random.randint(1, 100)
    print("Guess My Number. \nI am thinking of a number between 1 and 100.")
    guess = int(input("Enter a guess: "))

    while guess != secret_number:
        if guess > secret_number:
            print("Your guess is too High!")
        elif guess < secret_number:
            print("Your guess is too Low")

        print() #Look clean and tidy
        guess = int(input("Guess a new number: "))

    print(f"Congrats! The number was: {secret_number}")

  

if __name__ == '__main__':
    main()