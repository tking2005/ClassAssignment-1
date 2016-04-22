def main():
    getQuadraticEquation()


def getQuadraticEquation():
    continueProgram = True

    while (continueProgram == True):
        print("Welcome to Quadratic Computation! Enter integer values of A,B,C, and X at the corresponding prompts.")
        continueProgram = True
        while (continueProgram == True):
            try:
                valueA = int(input("Enter a value for A:"))
            except:
                print("Didn't I say an INTEGER!");valueA = int(input("Enter a value for A:"))
            try:
                valueB = int(input("Enter a value for B:"))
            except:
                print("That is not an integer!"); valueB = int(input("Enter a value for B:"))
            try:
                valueC = int(input("Enter a value for C:"))
            except:
                print("Didn't I say an INTEGER!");valueC = int(input("Enter a value for C:"))
            try:
                valueX = int(input("Enter a value for X:"))
            except:
                print("That is not an integer!");valueX = int(input("Enter a value for X:"))

            print("The following quadratic equation will compute:")
            print("(",valueA,"*",valueX,"^","2) +",valueB,"+",valueC)
            quadraticEquation = (valueA*(valueX**2)+(valueB*valueX)+(valueC))
            print("The value of the quadratic equation is:",quadraticEquation)
            wantToContinue = str(input("-----Press Q if you want to quit, all other input continues:"))
            wantToContinue = wantToContinue.strip()
            if wantToContinue == "Q" or wantToContinue == "q":
                continueProgram = False
main()