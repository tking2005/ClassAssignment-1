def main():
    getQuadraticEquation()


def getQuadraticEquation():
    continueProgram = True

    while (continueProgram == True):
        print("Welcome to Quadratic Computation! Enter integer values of A,B,C, and X at the corresponding prompts.")
        continueProgram = True
        validInputA = False
        validInputB = False
        validInputC = False
        validInputX = False
        while(validInputA==False):
            try:
                valueA = int(input("Enter a value for A:"))
                validInputA=True
            except:
                print("Didn't I say an INTEGER!")
        while (validInputB == False):
            try:
                valueB = int(input("Enter a value for B:"))
                validInputB = True
            except:
                print("That is not an integer!")
        while (validInputC == False):
            try:
                valueC = int(input("Enter a value for C:"))
                validInputC = True
            except:
                print("Didn't I say an INTEGER!")
        while (validInputX == False):
            try:
                valueX = int(input("Enter a value for X:"))
                validInputX = True
            except:
                print("That is not an integer!")

            print("The following quadratic equation will compute:")
            if valueB<0 and valueC<0:
                print(valueA,"X","^","2",valueB,"X",valueC)
            elif valueB<0:
                print(valueA,"X" , "^" , "2", valueB , "X", "+" , valueC)
            elif valueC<0:
                print(valueA , "X" , "^" , "2", "+" , valueB , "X", valueC)
            else:
                print(valueA , "X" , "^" , "2", "+" , valueB ,"X", "+", valueC)
            quadraticEquation = (valueA*(valueX**2)+(valueB*valueX)+(valueC))
            print("The value of the quadratic equation is:",quadraticEquation)
            wantToContinue = str(input("-----Press Q if you want to quit, all other input continues:"))
            wantToContinue = wantToContinue.strip()
            if wantToContinue == "Q" or wantToContinue == "q":
                continueProgram = False
main()