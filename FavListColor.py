'''
1. Create 2 lists
    a) input name store in one list
    b) Input favorite color store in second list

2. Type Q to quit
3. Print each name with corresponding Favorite color
'''


def main():
    getNameFavColor()


def getNameFavColor():
    continueProgram = True
    nameList = []
    colorList = []
    while(continueProgram==True):
        firstName=str(input("Enter your first name:"))
        nameList.append(firstName)
        favColor=str(input("Enter your favorite color:"))
        colorList.append(favColor)
        lengthofNameList=len(nameList)
        count=0
        for count in range(0, lengthofNameList):
            print("Hello there!")
            print(nameList[count],", your favorite color is",colorList[count])
            print("That's fantastic!")
        wantToContinue=str(input("-----Press Q if you want to quit, all other input continues:"))
        wantToContinue = wantToContinue.strip()
        if wantToContinue == "Q" or wantToContinue == "q":
            continueProgram = False

main()



