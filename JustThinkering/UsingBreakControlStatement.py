print("please, enter 'exit' when you are done. \n")
while True:
    data = input("Enter the integer to square: ")
    if data == "exit":
        break
    i = int(data)
    print(i, "squared is", i * i, "\n")
print("okay, bye!")

