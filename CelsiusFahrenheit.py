def main():
    GetCelsius()

def GetCelsius():
    ContinueProgram=True
    while(ContinueProgram==True):
        DegreeInFahrenheit=float(input("Please enter the temperature in Farenheit: "))
        DegreeInCelsius=float(DegreeInFahrenheit-32)/1.8
        print(DegreeInFahrenheit,"F is equal to",DegreeInCelsius,"C")
        WantToContinue = "N"
        WantToContinue = str(input("Do you want to continue the program? Type 'Y' for Yes and 'N' for No "))
        if WantToContinue=="Y" or WantToContinue=="y":
            ContinueProgram=True
        else:
            ContinueProgram=False



main()
