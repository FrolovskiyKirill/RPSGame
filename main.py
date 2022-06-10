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
all_choices = [rock, paper, scissors]

your_choice = int(input("Введи '1' для камня, '2' для бумаги и '3' для ножниц.\n"))
print(f"Твой выбор:\n{all_choices[your_choice - 1]}")

computer_choice = random.randint(1, 3)
print(f"Выбор компьютера:\n{all_choices[computer_choice - 1]}")

if your_choice == computer_choice:
  print("Ничья.")
elif your_choice == 1 and computer_choice == 3 or your_choice == 2 and computer_choice == 1 or your_choice == 3 and computer_choice == 2:
  print("Ты выиграл!")
else:
  print("Ты проиграл!")
