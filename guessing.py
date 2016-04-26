def main():

    global randomNumber
    randomNumber=getRandomNum()
    guessRandomNumber(randomNumber)





def getRandomNum():
    import random
    return random.randint(1,10)

def guessRandomNumber (randomNumb):
    continueProgram = True

    while (continueProgram == True):
        print("Welcome to the Number Guessing Game!!!")
        continueProgram = True
        print("What number am I thinking of from 1 to 10?")
        global num
        guessNum=False
        guessChance=1
        while (guessNum==False):
            validInput = False

            while (validInput == False):
                global num
                try:
                    num = int(input("Please guess a number from 1 to 10:")) and 0<num<11
                    return num
                    validInput = True
                except:
                    print("DOPE! please guess a NUMBER from 1 to 10!")


                '''if num<11 and num>0 :
                    validInput = True
                else:
                    print("DOPE! please guess a NUMBER from 1 to 10!")


                    print("DOPE! please guess a NUMBER from 1 to 10!") 
'''

            if num == randomNumb:
                    print("Hooray! You guessed the number I was thinking of!!!!")
                    guessNum=True
            if ((num==randomNumb+1) or num==(randomNumb-1)):
                print("Your guess is HOT!!!...CALIENTE!!!")
                if guessChance==3:
                    guessNum=True
                    print("The number I was thinking of is:")
                    print(randomNumb)
                guessChance = guessChance + 1

            elif ((num==randomNumb+2) or num==(randomNumb-2)):

                print("Your guess is WARM!")
                if guessChance == 3:
                    guessNum = True
                    print("The number I was thinking of is:")
                    print(randomNumb)
                guessChance = guessChance + 1
            else:
                if num <randomNumb or num>randomNumb:
                    print("Your guess is COLD..BRRRR")
                if guessChance == 3:
                    guessNum = True
                    print("The number I was thinking of is:")
                    print(randomNumb)
                guessChance = guessChance + 1
        wantToContinue = str(input("--Do you want to play again?  Press Q if you want to quit, all other input continues:"))
        wantToContinue = wantToContinue.strip()
        if wantToContinue == "Q" or wantToContinue == "q":
            continueProgram = False


main()