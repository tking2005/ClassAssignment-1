def main():

    global iterations
    iterations = getIterations()
    global numList
    numList=getNumList()
    getMin(numList)
    getMax(numList)
    sortList(numList)
    programContinues()


def getIterations():
    return int(input("How many numbers would you like to compare?"))

def getNumList():
    numList=[]
    for iteration in range(0,iterations):
        num=int(input("Enter your number:"))
        numList.append(num)
    print("Your list of numbers are:")
    print(numList)
    return numList

def getMin(numCompare):
    numMin = numCompare[0]
    for iteration in range(0,iterations):
        if numMin>numCompare[iteration]:
            numMin=numCompare[iteration]
    print("Your min number is:")
    print(numMin)

def getMax(numCompare):
    numMax = numCompare[0]
    for iteration in range(0, iterations):
        if numMax < numCompare[iteration]:
            numMax = numCompare[iteration]
    print("Your max number is:")
    print(numMax)

def sortList(numbList):
    sortedList=[]
    while numbList:
        minimum = numbList[0]
        for sort in numbList:
            if sort < minimum:
                minimum = sort
        sortedList.append(minimum)
        numbList.remove(minimum)
    print ("Your numbers sorted are:")
    print (sortedList)

def programContinues():
    continueProgram = True
    while(continueProgram==True):
        wantToContinue=str(input("-----Press Q if you want to quit, all other input continues:"))
        wantToContinue = wantToContinue.strip()
        if wantToContinue == "Q" or wantToContinue == "q":
            continueProgram = False
        else:
            main()

main()
