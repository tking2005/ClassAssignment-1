def main():

    global randomNumber
    randomNumber=getRandomNum()
    guessRandomNumber(randomNumber)





def getRandomNum():
    import random
    return random.randint(1,10)

def guessRandomNumber (randomNumb):
    global continueProgram
    continueProgram = True

    while (continueProgram == True):
        print("Welcome to the Number Guessing Game!!!")
        #continueProgram = True
        print("What number am I thinking of from 1 to 10? You have 3 chances!")
        global num
        guessNum=False
        guessChance=1
        while (guessNum==False):
            validInput = False

            while (validInput == False):


                try:
                    if guessNum !=4:
                        num = int(input("Please guess a number from 1 to 10:"))
                        num > 0 and num < 11
                        validInput = True
                except:
                    print("Silly...I said a NUMBER from 1 to 10!")

                    if guessChance == 3:
                        guessNum = True
                        validInput = True
                        num=0
                        print("Sorry!!!! The number I was thinking of is:")
                        print(randomNumb)
                    guessChance = guessChance + 1

                '''try:
                    num >0 and num<11
                    validInput = True
                except:
                    print("DOPE!...I said a NUMBER from 1 to 10!")
                    '''

            if  num>11 or num<0 or (num!=int):
                print("Silly...I said a NUMBER from 1 to 10!")
            else:
                validInput = True

                if guessChance == 3:
                    guessNum = True
                    print("Sorry!!!! The number I was thinking of is:")
                    print(randomNumb)
                guessChance = guessChance + 1



            if num == randomNumb:
                    print("Hooray! You guessed the number I was thinking of!!!!")
                    print("The number I was thinking of is:")
                    print(randomNumb)
                    guessNum=True
            if ((num==randomNumb+1) or num==(randomNumb-1))and (guessChance!=4):
                print("Your guess is HOT!!!...CALIENTE!!!")
                if guessChance==3:
                    guessNum=True
                    print("Sorry!!!! The number I was thinking of is:")
                    print(randomNumb)


            elif ((num==randomNumb+2) or num==(randomNumb-2))and (guessChance!=4):

                print("Your guess is WARM!")

                if guessChance == 3:
                    guessNum = True
                    print("Sorry!!!! The number I was thinking of is:")
                    print(randomNumb)
                guessChance = guessChance + 1
            else:
                if (num <randomNumb or num>randomNumb) and (guessChance!=4) and (0<num<11):
                    print("Sorry!!!Your guess is COLD..BRRRR")
                if guessChance == 3 and num!=randomNumb:
                    guessNum = True
                    print("The number I was thinking of is:")
                    print(randomNumb)
                guessChance = guessChance + 1
        wantToContinue = str(input("--Do you want to play again?  Press Q if you want to quit, all other input continues:"))
        wantToContinue = wantToContinue.strip()
        if wantToContinue == "Q" or wantToContinue == "q":
            continueProgram = False

        else:
            main()


main()
