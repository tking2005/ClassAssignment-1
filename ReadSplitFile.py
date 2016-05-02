def main():
    readFile()

def readFile():
    file = open("C:/Users/Student 12/Documents/test.txt", "r")
    essay = file.readlines()
    for line in essay:
        words = line.split()
        print (words)

main()