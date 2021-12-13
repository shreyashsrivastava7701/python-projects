import random
import time
import datetime

print("Welcome to the game")
print("You can choose between rock, paper and scissor")
print("The computer will choose randomly")
print("Write 'exit' to exit the game")

while True:
    dt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    choice = str(input("Enter your choice (rock, paper, scissor): "))
    choice = choice.lower()
    options = ["rock", "paper", "scissor"]
    comp_choice = random.choice(options)

    file = open(r'C:\Users\HP\OneDrive\Desktop\PROJECTS\Beginner Projects\Rock, Paper and Scissor\log.txt', "a")
    file.write(f"Date and Time: {dt} \n")
    file.write(f"User Choice: {choice} \n")
    file.write(f"Computer Choice: {comp_choice} \n")
    file.close()

    win1 = "Computer Wins"
    win2 = "You Win"

    if comp_choice == choice:
      print(f"Draw as computer chose {comp_choice}")
    if comp_choice == "rock":
      if choice == "scissor":
        print(f"{win1} as computer chose {comp_choice}")
      elif choice == "paper":
        print(f"{win2} as computer chose {comp_choice}")
    if comp_choice == "paper":
      if choice == "scissor":
        print(f"{win2} as computer chose {comp_choice}")
      elif choice == "rock":
        print(f"{win1} as computer chose {comp_choice}")
    if comp_choice == "scissor":
      if choice == "paper":
        print(f"{win1} as computer chose {comp_choice}")
      if choice == "rock":
        print(f"{win2} as computer chose {comp_choice}")
    if choice == "exit":
        print("Thank you for playing")
        print("Exiting in 5 seconds")
        time.sleep(5)
        exit()