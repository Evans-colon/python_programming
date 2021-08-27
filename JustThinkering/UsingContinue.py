more = "y"
while more.lower() == "y":
    miles_driven = float(input("enter miles driven: \t"))
    gallon_used = float(input("enter gallons of gas used: \t"))
    if miles_driven <= 0 or gallon_used <= 0:
        continue
    mpg = round(miles_driven / gallon_used, 2)
    print("miles per gallon:", mpg, "\n")
    more = input("continue? (y/n): ")
    print()

    print("okay, bye!")
