Obese_points = 0
Malnourished_points = 0
Nerd_points = 0

answer = input("Would you rather A) Look at a planet, or B) look at an asteroid?")
if answer == "A":
    Obese_points += 1 
elif answer == "B":
    Malnourished_points += 1

answer = input("Would your rather A) Eat the food, or B) Smell the food?") 
if answer == "A":
    Malnourished_points += 1
elif answer == "B":
    Obese_points += 2

answer = input("Mcdonalds cheese burger contains A) 2 buns musterd ketchup 3 pickles and a patty or B) 2 buns musterd ketchup 2 pickles and a patty or C) Erm actualy Incorrect answers") 
if answer == "A":
    Malnourished_points += -1
elif answer == "B":
    Obese_points += -1
if answer == "C":
    Nerd_points += 3
    Obese_points += 1

answer = input("Is 2 quarter pounders A) to much food or B) Not enough or C) Just right or D)IM GOING TO DIE")
if answer == "A":
    Malnourished_points += 1
elif answer == "B":
    Obese_points += 1
if answer == "C":
    Obese_points += -2
elif answer == "D":
    Malnourished_points += 2

answer = input("Is a Hot dog a A) Sandwich or B) a hot dog or C) its just food")
if answer == "A":
    Nerd_points += 3
elif answer == "B":
    Malnourished_points += 1
if answer == "C":
    Obese_points += 2

# end of quiz:
if Obese_points < Malnourished_points:
    print("your are Malnourished")
elif Malnourished_points < Obese_points:
    print("your are OBESE YOUR BENDING TIME AND SPACE")
elif Nerd_points < Obese_points:
    print("your are OBESE YOUR BENDING TIME AND SPACE")
if Obese_points < Nerd_points:
    print("Nerd get out of school")



