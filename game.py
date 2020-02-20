import random

hidden = random.randrange(1,100)
found = False

while found == False:
  guess = int(raw_input("Please enter your guess: "))
  if guess == hidden:
    found = True
    print("You've won!")
  elif guess < hidden:
    print("Too low!")
  else:
    print("Too high!")
  