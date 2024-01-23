import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
         (_______
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

while True:
    game_images = [rock, paper, scissors]

    user_choice = int(input("enter your choice 0,1 or 2\n"))

    if user_choice >= 3 or user_choice < 0:
        print("you entered wrong choice! you lost")
    else:
        print(game_images[user_choice])

        comp_choice = random.randint(0, 2)

        print(game_images[comp_choice])

        if user_choice == 0 and comp_choice == 2:
            print("you win")

        elif comp_choice == 0 and user_choice == 2:
            print("you lose")

        elif comp_choice > user_choice:
            print("you lose")

        elif user_choice > comp_choice:
            print("you win")
        elif comp_choice == user_choice:
            print("draw")
