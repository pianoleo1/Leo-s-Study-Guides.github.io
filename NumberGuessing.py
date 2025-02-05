# Number Guessing Game
def guessed():
  userinput = input(f"Yay! I guessed correctly. The number is {guessnum}. Play again?(yes/no)")
  if userinput == "yes":
    print("Okay!")
  else:
    quit()
while True:
  userinput = int(input("Welcome to the number guessing game! Would you like to play computer guessing mode (1) or human mode (2)? "))
  if userinput == 1:
    print("Entering computer guessing mode...")
    guessnum = int(input("What is the maximum number that I can guess? "))
    guessnum = guessnum//2
    prevnum = guessnum
    userinput = input(f"Is it {guessnum}? (too high/too low) ")
    if userinput == "high":
      guessnum = 250
      userinput = input("Is it 250? ")
      while True:
        if userinput == "high":
          if prevnum < guessnum:
            guessnum = guessnum - (guessnum - prevnum)//2
            prevnum = 2*guessnum - prevnum
          else:
            guessnum = guessnum - (prevnum - guessnum)//2
            prevnum = (2*guessnum + prevnum)//3
          userinput = input(f"Is it {guessnum}? (too high/too low/yes) ")
          if userinput == "yes":
            guessed()
        if userinput == "low":
          if prevnum < guessnum:
            guessnum = guessnum + (guessnum - prevnum)//2
            prevnum = (2*guessnum + prevnum)//3
          else:
            guessnum = guessnum + (prevnum - guessnum)//2
            prevnum = 2*guessnum - prevnum
          userinput = input(f"Is it {guessnum}? (too high/too low/yes) ")
        if userinput == "yes":
          guessed()

    if userinput == "low":
      guessnum = 750
      userinput = input("Is it 750? ")
      while True:
        if userinput == "high":
          if prevnum < guessnum:
            guessnum = guessnum - (guessnum - prevnum)//2
            prevnum = 2*guessnum - prevnum
          else:
            guessnum = guessnum - (prevnum - guessnum)//2
            prevnum = (2*guessnum + prevnum)//3
          userinput = input(f"Is it {guessnum}? (too high/too low/yes) ")
        if userinput == "low":
          if prevnum < guessnum:
            guessnum = guessnum + (guessnum - prevnum)//2
            prevnum = (2*guessnum + prevnum)//3
          else:
            guessnum = guessnum + (prevnum - guessnum)//2
            prevnum = 2*guessnum - prevnum
          userinput = input(f"Is it {guessnum}? (too high/too low/yes) ")
        if userinput == "yes":
          guessed()
