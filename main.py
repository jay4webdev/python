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
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
game_image = [rock,paper,scissors]
user_choice = int(input("Welcome to ROCK PAPER SECSSOR Game.\n Press '0' for ROCK, '1' for  PAPPER ,'2' for SECSSOR : "))

if user_choice > 2 or user_choice < 0:
  print("Enter valid Number, Game Over")
else:
  print(game_image[user_choice])

  computer_choice = random.randint(0,2)
  print(game_image[computer_choice])
  
  
  if user_choice < computer_choice:
    print("Sorry.. You lose. Game Over")
  
  elif user_choice > computer_choice:
    print("Wow...You Won!!")
  
  elif user_choice == computer_choice:
    print("Match Draw..!!!")
  
  else:
    print("Enter Valid Number")