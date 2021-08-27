total_score = 0
counter = 0
print("Welcome to result portal")
print("===========================================")
print("kindly enter a valid score between 1 and 100")
print("please, feel free to exit by entering '999'")
score = int(input("please, enter a valid score between 1 and 100: "))
while True:
    if score > 0 and score <= 100:
        total_score += score
        counter += 1
    elif score == 999:
        break
    else:
        print("test score must be greater than 0 and must not be more than 100. please, try again")
    average_score = round(total_score / counter)
    print("========================================")
    print("Total score is: ", total_score, "\nAverage score is: ", average_score)
    print()
    print("bye")
