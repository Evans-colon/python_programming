total_score = 0
for i in range(3):
    while True:
        score = int(input("please, enter a valid test score: "))
        if score > 0 or score < 100:
            total_score += score
            break
        else:
            print("test score must not be less than 0 and greater than 100")
print("total of the valid test score is: ", total_score)
