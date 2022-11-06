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

user_option = int(input("What do you choose? Type 0 for Rock, 1 for paper or 2 for Scissors."))

cpu_option = random.randint(0,2)

if user_option == 0 and cpu_option == 0:
  print("Your option")
  print(rock)
  print("Computer option")
  print(rock)
  print("Tie")
elif user_option == 0 and cpu_option == 1:
  print("Your option")
  print(rock)
  print("Computer option")
  print(paper)
  print("You lose")
elif user_option == 0 and cpu_option == 2:
  print("Your option")
  print(rock)
  print("Computer option")
  print(scissors)
  print("You win")

if user_option == 1 and cpu_option == 1:
  print("Your option")
  print(paper)
  print("Computer option")
  print(paper)
  print("Tie")
elif user_option == 1 and cpu_option == 2:
  print("Your option")
  print(paper)
  print("Computer option")  
  print(scissors)
  print("You lose")
elif user_option == 1 and cpu_option == 0:
  print("Your option")
  print(paper)
  print("Computer option")
  print(rock)
  print("You win")

if user_option == 2 and cpu_option == 2:
  print("Your option")
  print(scissors)
  print("Computer option")
  print(scissors)
  print("Tie")
elif user_option == 2 and cpu_option == 0:
  print("Your option")
  print(scissors)  
  print("Computer option")
  print(rock)
  print("You lose")
elif user_option == 2 and cpu_option == 1:
  print("Your option")
  print(scissors)
  print("Computer option")  
  print(paper)  
  print("You win")