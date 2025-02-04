# Number Guessing Game
userinput = int(input("Welcome to the number guessing game! Would you like to play computer guessing mode (1) or human mode (2)? "))
if userinput == 1:
  print("Entering computer guessing mode...")
  guessnum = int(input("What is the maximum number that I can guess? "))
  guessnum = guessnum//2
  userinput = input(f"Is it {guessnum}? (too high/too low)")
  while True:
    if userinput == "too high":
      guessnum = guessnum//2
      userinput = input(f"Is it {guessnum}? (too high/too low/yes) ")
      if userinput == "yes":
        print("Yay! I guessed correctly. The number is ",guessnum,".")
        quit()
    if userinput == "too low":
      guessnum = guessnum + guessnum//2
      userinput = input(f"Is it {guessnum}? (too high/too low/yes)")
      if userinput == "yes":
        print("Yay! I guessed correctly. The number is ",guessnum,".")
        quit()
