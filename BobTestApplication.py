def main():
    iterations = getIterations()
    getAverage(iterations)

def getIterations():
    return int(input("How many numbers will you add?"))

def getAverage(y):
    firstList=[]
    for a in range (0,y):
        testscore=int(input("Enter your test score:"))
        firstList.append(testscore)


    firstList.append(100)
    lengthofList=len(firstList)
    sum=0
    print("The numbers you entered were:", end=" ")
    for c in range(0,lengthofList):
        print(firstList[c], end=" ")
        sum=sum+firstList[c]
    firstList.append(100)
    sum=sum+firstList[lengthofList]
    print("")
    print("The average of your numbers are",sum/lengthofList+1)

'''
    for c in len(firstList):
        print(b)
    for b in firstList:
        print(b)
    firstList.append(100)
    lengthofList=len(firstList)
    for c in len(firstList):
        sum=sum+firstList[c]
        print(firstList[c])

'''
main()


