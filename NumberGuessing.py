# Number Guessing Game
userinput = int(input("Welcome to the number guessing game! Would you like to play computer guessing mode (1) or human mode (2)? "))
if userinput == 1:
  print("Entering computer guessing mode...")
  guessnum = int(input("What is the maximum number that I can guess? "))
  guessnum = guessnum//2
  prevnum = guessnum
  userinput = input(f"Is it {guessnum}? (too high/too low) ")
  if userinput == "high":
    userinput = input("Is it 250? ")
    while True:
      if userinput == "high":
        guessnum = guessnum - (guessnum - prevnum)//2
        userinput = input(f"Is it {guessnum}? (too high/too low/yes) ")
        prevnum = guessnum
        if userinput == "yes":
          print("Yay! I guessed correctly. The number is",guessnum,".")
          quit()
      if userinput == "low":
        guessnum = guessnum + (guessnum*2 - guessnum)//2
        userinput = input(f"Is it {guessnum}? (too high/too low/yes) ")
        prevnum = guessnum
        if userinput == "yes":
          print("Yay! I guessed correctly. The number is",guessnum,".")
          quit()

  if userinput == "low":
    userinput = input("Is it 750? ")
    while True:
      if userinput == "high":
        guessnum = guessnum - (guessnum - prevnum)//2
        userinput = input(f"Is it {guessnum}? (too high/too low/yes) ")
        prevnum = guessnum
        if userinput == "yes":
          print("Yay! I guessed correctly. The number is",guessnum,".")
          quit()
      if userinput == "low":
        guessnum = guessnum + (guessnum*2 - guessnum)//2
        userinput = input(f"Is it {guessnum}? (too high/too low/yes) ")
        prevnum = guessnum
        if userinput == "yes":
          print("Yay! I guessed correctly. The number is",guessnum,".")
          quit()
