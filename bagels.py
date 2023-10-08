from numpy import random


NUM_DIGITS = 3
MAX_GUESS = 10 

def getSecretNumber():
    number = list("0123456789")
    random.shuffle(number)

    
    secretNum = ""
    for i in range(NUM_DIGITS):
        secretNum += number[i]
    return secretNum

def getClues(guess, secretNumber):
    if guess == secretNumber:
        return "You got it!"
    
    clues = []
    for i in range(len(guess)):
        if guess[i] == secretNumber[i]:
            clues.append("Fermi")
        elif guess[i] in secretNumber:
            clues.append("Pico")
    if len(clues) == 0:
        return 'Bagles'
    else:
        clues.sort()
        return ' '.join(clues)

def main():
    while True:
        #this stores the secret number player need s to guess 
        secretNum = getSecretNumber()

        print("I have thought up a number")
        print(f"You have {MAX_GUESS} guesses to get it")
        
        num_guess = 1
        while num_guess <= MAX_GUESS:
            guess = ''
            #keep looping until they enter a valid guess:
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print(f'Guess #{num_guess}')
                guess = input('> ')

            clues = getClues(guess, secretNum)
            print(clues)
            num_guess +=1 
            if guess == secretNum:
                print("Your guess is correct")
                break

        if num_guess > MAX_GUESS:
            print("You are run out of guesses")
            print(f"The answer was {secretNum}")
        
        print("Do you want to play again")
        print(" Yes or No")
        if not input('> ').lower().startswith('y'):
            break
    print("Thank for playing!")
    


if __name__ == "__main__":
    main()