Large_points = 0
Small_points = 0
Smart_points = 0

#beginning of quiz
answer = input("Would you rather A) Look at a planet, or B) look at an asteroid?")
if answer == "A":
    Large_points += 1 
elif answer == "B":
    Small_points += 1

answer = input("Would your rather A) Eat the food, or B) Smell the food?") 
if answer == "A":
    Small_points += 1
elif answer == "B":
    Large_points += 2

answer = input("Mcdonalds cheese burger contains A) 2 buns musterd ketchup 3 pickles and a patty or B) 2 buns musterd ketchup 2 pickles and a patty or C) Erm actualy Incorrect answers") 
if answer == "A":
    Small_points += -1
elif answer == "B":
    Large_points += -1
if answer == "C":
    Smart_points += 3
    Large_points += 1
# middle of quize
answer = input("Is 2 quarter pounders A) to much food or B) Not enough or C) Just right or D)IM GOING TO DIE")
if answer == "A":
    Small_points += 1
elif answer == "B":
    Large_points += 1
if answer == "C":
    Large_points += -2
elif answer == "D":
    Small_points += 2

answer = input("Is a Hot dog a A) Sandwich or B) a hot dog or C) its just food")
if answer == "A":
    Smart_points += 3
elif answer == "B":
    Small_points += 1
if answer == "C":
    Large_points += 2

# end of quiz:
if Large_points < Small_points:
    print("your are Smaller than the average human")
elif Small_points < Large_points:
    print("U are Bigger than the average human")
elif Smart_points < Large_points:
    print("U are Bigger than the average human")
if Large_points < Smart_points:
    print("Annoyingly smart")



