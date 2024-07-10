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



import random

computer = random.randint(0,2)


user = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

computer = random.randint(0,2)


if user == computer == 0:
    print(f"You chose: {rock}")
    print(f"Computer chose: {rock}")
    print("Try again.")
elif user == computer == 1:
    print(f"You chose: {paper}")
    print(f"Computer chose: {paper}")
    print("Try again.")
elif user == computer == 2:
    print(f"You chose: {scissors}")
    print(f"Computer chose: {scissors}")
    print("Try again.")
elif user == 0 and computer == 1:
    print(f"You chose: {rock}")
    print(f"Computer chose: {paper}")
    print("You lose, computer wins.")
elif user == 1 and computer == 0:
    print(f"You chose: {paper}")
    print(f"Computer chose: {rock}")
    print("You win, computer loses.")
elif user == 0 and computer == 2:
    print(f"You chose: {rock}")
    print(f"Computer chose: {scissors}")
    print("You win, computer loses.")
elif user == 2 and computer == 0:
    print(f"You chose: {scissors}")
    print(f"Computer chose: {rock}")
    print("You lose, computer wins.")
elif user == 1 and computer == 2:
    print(f"You chose: {paper}")
    print(f"Computer chose: {scissors}")
    print("You lose, computer wins.")
elif user == 2 and computer == 1:
    print(f"You chose: {scissors}")
    print(f"Computer chose: {paper}")
    print("You win, computer loses.")
