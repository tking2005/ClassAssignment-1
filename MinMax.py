def main():
    getMinMaxNum()


def getMinMaxNum():
    continueProgram = True
    numTuple =()
    while(continueProgram==True):
        numTuple=int(input("Enter your numbers followed by a comma:"))
        numList.append(num)
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



data_list = [-5, -23, 5, 0, 23, -6, 23, 67]

new_list = []

minimum = data_list[0]  # arbitrary number in list

for x in data_list:
  if x < minimum:
    minimum = value
    new_list.append(i)