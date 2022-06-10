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
all_choises = [rock, paper, scissors]

your_choise = int(input("Введи '1' для камня, '2' для бумаги и '3' для ножниц.\n"))
print(f"Твой выбор:\n{all_choises[your_choise - 1]}")

computer_choise = random.randint(1, 3)
print(f"Выбор компьютера:\n{all_choises[computer_choise - 1]}")

if your_choise == computer_choise:
  print("Ничья.")
elif your_choise == 1 and computer_choise == 3 or your_choise == 2 and computer_choise == 1 or your_choise == 3 and computer_choise == 2:
  print("Ты выиграл!")
else:
  print("Ты проиграл!")
