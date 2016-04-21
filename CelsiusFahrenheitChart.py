def main():
    CelsiusFahrenheitTemp()



def CelsiusFahrenheitTemp():
    CelsiusFahrenheitTitle="Celsius   Fahrenheit"
    print(CelsiusFahrenheitTitle)
    CTemp = 0
    count = 100
    while CTemp<count:
        FTemp=float(1.8*CTemp+32)
        print(CTemp,"C",end="    ")
        print(FTemp,"F")
        CTemp = CTemp+5

main()

for celsius in range (0,101,5):
    print("Celsius:",celsius, "Fahrenheit:",float(1.8*celsius+32))