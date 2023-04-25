# program 1
'''
weight = int(input("Weight: "))
Unit = input("(L)bs or (K)g: ") 
if Unit.upper() == "L":
    converted = weight * 0.45
    print(f"You are {converted} Kilos")
elif Unit.upper() == "K":
    converted = weight // 0.45
    print(f"You are {converted} Pounds")
'''
# program 2

import random
print("You have 3 guesses to get the number I am thinking of from 1-10\n")
answer = random.randint(1,10)
Number = 0
while Number < 3:
    guess = input("Guess: ")
    Number += 1
    if guess.isdigit() == False:
        Number -= 1
        print("Your bitch ass didnt type a number")
        print("Go rethink your life and then come back")
        print("You prob never coming back cause you aint got no life")
        print("Now then sir may you continue with the program\n")
    elif int(guess) == answer:
        print("YOU WIN")
        break
else:
    print("\nSorry you failed")
    print(f"The number was {answer}")


# program 3
'''
car_start = False
while True:
    question = input("> ")
    if question.lower() == "help":
        print("Type start to start the car")
        print("Type stop to stop the car")
        print("Type quit to end the game")
    elif question.lower() == "start":
        if car_start:
            print("Car is alread started")
        else:
            print("The car is turning on")
            print("The car is on and ready to go")
            car_start = True
    elif question.lower() == "stop":
        if not car_start:
            print("Car is already stoped")
        else:
            print("Car has stoped")
            car_start = False
    elif question.lower() == "quit":
        break
    else:
        print("I dont understand")
print("Game Over")
'''
#program 4
'''
prices = [10,20,30]
total = 0
for price in prices:
    total = total + price
print(f"Total: {total}")
'''
#program 5 
'''
number = [5,2,5,2,2]
for x in number:
    print("x" * x)
'''
# program 6
'''
print("Type numbers in the following lines and I will tell you\nwhich one is the biggest")
a = int(input("1. "))
b = int(input("2. "))
c = int(input("3. "))
d = int(input("4. ")) 
number = [a, b, c, d]
value = number[0]
for item in number:
    if item > value:
        value = item
print(value,"is the biggest number amoung the listed numbers")
'''
#program 7
'''
import random
random_pick = random.randint(1,3)
# the randint command picks a random number
#random is a module
print("Lets play Rock Paper Scissors")
print("(Rock, Paper, Scissors)")
there_pick = input("Type one of the options above: ")
if random_pick == 1:
    print("The Computer picks:\tRock\n")
    if there_pick.lower() == "rock":
        print("Tie")
    elif there_pick.lower() == "paper":
        print("You win")
    elif there_pick.lower() == "scissor":
        print("You lose")
    else:
        print("I don't understand")
elif random_pick == 2:
    print("The Computer picks:\tPaper\n")
    if there_pick.lower() == "rock":
        print("You lose")
    elif there_pick.lower() == "paper":
        print("Tie")
    elif there_pick.lower() == "scissor":
        print("You win")
    else:
        print("I don't understand")
elif random_pick == 3:
    print("The Computer picks:\tScisser\n")
    if there_pick.lower() == "rock":
        print("You win")
    elif there_pick.lower() == "paper":
        print("You lose")
    elif there_pick.lower() == "scissor":
        print("Tie")
    else:
        print("I don't understand")

'''
#program 8
'''
import random
random_number = random.randint(1,20)

Guess = 0
number = 0
print("Guess a number from 1 to 20")
while Guess != random_number:
    Guess = int(input(""))
    number = number + 1
    if Guess <= random_number and Guess >= 1:
        if Guess != random_number:
            print("To low")
    elif Guess >= random_number and Guess <= 21:
        print("To high")
    elif Guess > 20:
        print("Number is higher than 20")
    elif Guess < 1:
        print("Number is lower than 1")
    else:
        print("Invalid input")
print("You win")
print(f"You took {number} tries")
'''
#program 9
'''
x = int(input("Number 1: "))
y = int(input("Number 2: "))
z = int(input("Number 3: "))

print("\nThe number following is the largest number:")
print(max(x, y, z))

print("\nThe following number is the smallest number:")
print(min(x, y, z))
'''

#program 10
'''
print("Movie Tickets")
total = 0
print("Type \"done\" to end program")
while True:
  age = input("Age: ")
  if age.lower() == "done":
    break
  if int(age) < 3:
    print("Your ticket is free")
  elif int(age) > 3 and int(age) < 13:
    print("Your ticket costs $10")
    total = total + 10
  elif int(age) > 13 and int(age) < 18:
    print("Your ticket costs $25")
    total = total + 20
  elif int(age) > 18 and int(age) < 40:
    print("Your ticket costs $20")
    total = total + 15
  elif int(age) > 40 and int(age) < 81:
    print("Your ticket costs $10")
    total = total + 10
  elif int(age) > 80:
    print("Age is to high")
if total != 0:
  print("You total is " + str(total))
print("Thank you for your purchase")
'''

#program 11
'''
import random
print("Lets play Double O Seven")
print("(Reload, Shoot, Sheld, Quit)")
turn = 0
bullet1 = 0
bullet2 = 0
while True:
  turn = turn + 1
  print("Round",turn)
  if bullet2 == 0:
    if turn == 1:
      random_pick = 1
    elif turn > 1 and bullet1 > 0:
      random_pick_option = random.randint(1,2)
      if random_pick_option == 1:
        random_pick = 1
      elif random_pick_option == 2:
        random_pick = 3
    elif bullet1 == 0:
      random_pick = 1
  else:
    random_pick_option = random.randint(1,8)
    if random_pick_option == 1:
      random_pick = 2
    elif random_pick_option == 2:
      random_pick = 2
    elif random_pick_option == 3:
      random_pick = 3
    elif random_pick_option == 4:
      random_pick = 2
    elif random_pick_option == 5:
      random_pick = 3
    elif random_pick_option == 6:
      random_pick = 1
    elif random_pick_option == 7:
      random_pick = 2
    elif random_pick_option == 8:
      random_pick = 3
  pick = input("Type one of the options above: ")
  if pick.lower() == "quit":
    message = "YOU HAVE SUCCESFULLY QUITTED"
    break
  elif random_pick == 1:
    bullet2 = bullet2 + 1
    print("\nComputer got one more bullet")
    print("Current bullets(Computer):",bullet2,"\n")
    if pick.lower() == "reload":
      bullet1 = bullet1 + 1
      print("You got one more bullet")
      print("Current bullets(You):",bullet1,"\n")
    elif pick.lower() == "shoot":
      if bullet1 > 0:
        print("You shoots the Computer")
        print("The computer dies")
        message = "YOU WIN"
        break
      elif bullet1 == 0:
        print("You have no bullets")
    elif pick.lower() == "shield":
      print("You protected yourself\n")
  elif random_pick == 2:
    if bullet2 > 0:
      print("\nComputer shoots")
      bullet2 = bullet2 - 1
      print("Computers bullets left:",bullet2,"\n")
      if pick.lower() == "reload":
        bullet1 = bullet1 + 1
        message = "YOU LOSE"
        break
      elif pick.lower() == "shoot":
        if bullet1 > 0:
          print("You also shoot")
          print("Both of you miss\n")
          bullet1 = bullet1 -1 
          print("Current bullets(You)", bullet1,"\n")
        elif bullet1 == 0:
          print("You have 0 bullets")
      elif pick.lower() == "shield":
        print("You protected yourself")
      elif bullet2 == 0:
        bullet2 = bullet2
  elif random_pick == 3:
    print("\nComputer protected it self\n")
    if pick.lower() == "reload":
      bullet1 = bullet1 + 1
      print("You got one more bullet")
      print("Current bullets(You):", bullet1,"\n")
    elif pick.lower() == "shoot":
      if bullet1 > 0:
        print("You missed")
        bullet1 = bullet1 - 1
        print("Current bullets(You):", bullet1,"\n")
      elif bullet1 == 0:
        print("You have no bullet")
    elif pick.lower() == "shield":
      print("You protected yourself")
print(message)
'''
#program 12
'''
import random
print("Black Jack")
computer_card1 = random.randint(1,13)
computer_card2 = random.randint(1,13)
your_card1 = random.randint(1,13)
your_card2 = random.randint(1,13)
your_card3 = 0
your_card4 = 0
your_card5 = 0
turn = 0
while True:
  turn = turn + 1
  total1 = your_card1 + your_card2 + your_card3 + your_card4 + your_card5
  print( "Your cards: ",your_card1, "+",your_card2 ,"+", your_card3,"+",your_card4,"+",your_card5, "=", total1)
  print("(Stick, Hit)")
  pick = input("")
  if pick.lower() == "stick":
    break
  elif pick.lower() == "hit":
    if turn == 1:
      your_card3 = random.randint(1,13)
    elif turn == 2:
      your_card4 = random.randint(1,13)
    elif turn == 3:
      your_card5 = random.randint(1,13)
    elif turn > 3:
      print("You can't have any more turns")
    total1 = your_card1 + your_card2 + your_card3 + your_card4 + your_card5
  if total1 > 21:
    print( "Your cards: ",your_card1, "+",your_card2 ,"+", your_card3,"+",your_card4,"+",your_card5, "=", total1)
    break

print( "Computer cards: ",computer_card1, "+",computer_card2 , "=", computer_card1 + computer_card2)
total2 =  computer_card1 + computer_card2
if total1 > total2 and total1 < 22 and total2 < 22:
  print("You win")
elif total2 > total1 and total1 < 22 and total2 < 22:
  print("You Lose")
elif total1 > 21 and total2 < 22:
  print("You lose")
elif total2 > 21 and total1 < 22:
  print("You win")
elif total1 > 21 and total2 > 21:
  print("Tie")
elif total1 == total2:
  print("Tie")
'''
#program 13

