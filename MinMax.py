def main():
    global iterations
    iterations = getIterations()
    global numList
    numList(iterations)
    getMin(numList)



def getIterations():
    return int(input("How many numbers would you like to compare?"))

def numList(iteration):

    numList = []
    for iteration in range(0,iteration):
        num = int(input("Enter a number:"))
        numList.append(num)
    print("Your list of numbers are:")
    print(numList)


    count = 0
    for count in range(0,iteration+1):
        if numList[count]>=numList[count+1]:
            maxNum=numList[count]
        else:
            maxNum=numList[count+1]

        #print(numList[count])
        count = count + 1
    print(maxNum)







    while numList:
        minNum = numList[0]  # arbitrary number in list
        index=0
        for index in range (iterations):
            if numList[index] < numList[index+1]:
                minNum = numList[index]
            else:
                minNum=minNum
    print("The minimum number is:")
    print(minNum)

    while numList:
        maxNum = numList[0]
        index = 0

        for index in range(len(numList)):
            if maxNum > numList[index + 1]:
                maxNum = numList[index]
    print("The maximum number is:")
    print(maxNum)



'''continueProgram = True
while (continueProgram == True):
    wantToContinue = str(input("-----Press Q if you want to quit, all other input continues:"))
    wantToContinue = wantToContinue.strip()
    if wantToContinue == "Q" or wantToContinue == "q":
        continueProgram = False
        '''

main()