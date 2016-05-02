def main():
    global essayList
    essayList =[]
    readFile()
    #endOfSentence()
    countWords()

def readFile():
    file = open("C:/Users/Student 12/Documents/test.txt", "r")
    essay = file.readlines()
    essayWordList=[]


    for line in essay:
        count = 0
        words = line.split()
        while count<len(words):
            essayList.append(words[count])
            count+=1

    #print(words)
    print(essayList)

def countWords ():
    file = open("C:/Users/Student 12/Documents/test.txt", "r")
    eachWord=""
    endOfLineCharacters = ""
    validWord = 0
    #endOfFile = len(file)
    count=0
    counter=0
    while counter < len(essayList):
        eachWord = essayList[counter]
        #print (endOfLineCharacters)
        #print (len(eachWord))

        counter+=1
        for count in range(0, len(eachWord)):

            #print (endOfLineCharacters)
            if (len(eachWord)>3) and ((eachWord[count] != '!') or (eachWord[count] != '?') or (eachWord[count] != '.') or (eachWord[count] != ';') or(eachWord[count] != ':')):
                validWord+=1

            count += 1
            print (validWord)
    #return endOfLineCharacters
    #print (validWord)
    #return validWord

def endOfSentence():
    file = open("C:/Users/Student 12/Documents/test.txt", "r")
    # eachWord=str()
    endOfLineCharacters = ""
    numberOfSentence = 0
    # endOfFile = len(file)
    count = 0
    counter = 0
    while counter < len(essayList):
        endOfLineCharacters = essayList[counter]
        # print (endOfLineCharacters)
        # print (len(endOfLineCharacters))
        counter += 1
        for count in range(0, len(endOfLineCharacters)):
            print(endOfLineCharacters)
            if (endOfLineCharacters[count] == '!' and endOfLineCharacters[count + 1] == ' ') or (
                    endOfLineCharacters[count] == '?' and endOfLineCharacters[count + 1] == ' ') or (
                    endOfLineCharacters[count] == '.' and endOfLineCharacters[count + 1] == ' ') or (
                    endOfLineCharacters[count] == ':' and endOfLineCharacters[count + 1] == ' ') or (
                    endOfLineCharacters[count] == ';' and endOfLineCharacters[count + 1] == ' '):
                endOfLineCharacters = endOfLineCharacters + endOfLineCharacters[count]
                numberOfSentence += 1
            count += 1
            # return endOfLineCharacters


main()