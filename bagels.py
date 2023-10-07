from numpy import random


NUM_DIGITS = 3
NUM_GUESS = 10 

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
    
    
    


if __name__ == "__main__":
    secretNum = getSecretNumber()
    print(secretNum)
    print(type(secretNum))