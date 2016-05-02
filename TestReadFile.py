def main():
    f=open("C:/Users/Student 12/Documents/test.txt","r")
    myList=[]
    for line in f:
        myList.append(line)
    b=len(myList)
    for a in range(0,b):
        print(myList[a])
        

main()