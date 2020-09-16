  
secret_number = 10
guess_your_count = 0
guess_your_limit=int(input("Enter how many times you want to guess: "))
while guess_your_count<guess_your_limit:
    guess = int(input('Guess the number: '))
    guess_your_count+=1
    if guess == secret_number:
        print("You won!")
        break
    else:
        print("You have failed! Try again...")
