import random 

user_choice = int(input("What do you choose ? Type 0 for rock , 1 for paper , 2 for scissors"))
computer_choice = random.randint(0,2)
print(f"Computer choice is {computer_choice} ans user choice is {user_choice}")
print("Result is : ")
if user_choice == computer_choice:
    print("Draw!!")
elif user_choice == 0 and computer_choice ==2:
    print("You wins !!")
elif computer_choice > user_choice:
    print("You loose")
else:
    print("You win !!")