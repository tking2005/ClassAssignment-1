import sys

# the following prints one system argument
def arg1():
    print(sys.argv[1])



#The following prints 2 system arguments
def arg2():
    print(sys.argv[1],sys.argv[2])

# the following reads 3 arguments and assigns them to variables.
def arg3():
    first=sys.argv[1]
    second=sys.argv[2]
    third=sys.argv[3]
    print("First argument is",first,"! The second argument is", second, " ! The third argument is", third)



# the following reads a file as an argument
def readfilearg():
    ValidFile=False
    while ValidFile==False:
        try:
            file = sys.argv[1]  # get the file from the argument
            f = open(file, "r")  # opens the file essay.txt
            print(f.read())
            ValidFile=True
        except:
            print("File not found")
            break

#uncomment whichever function call you want to run
#arg1()
#arg2()
#arg3()
readfilearg()

