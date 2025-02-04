# Number Guessing Game
userinput = int(input("Welcome to the number guessing game! Would you like to play computer guessing mode (1) or human mode (2)?"))
if userinput == 1:
  print("Entering computer guessing mode...")
  guessnum = int(input("What is the maximum number that I can guess? "))
  while True:
    guessnum = guessnum//2
    userinput = input("Is it",guessnum,"? (too high/too low)")
    if userinput == "too high":
      guessnum = guessnum//2
      print("Is it",guessnum,"? (too high/too low)")
    if userinput == "too low":
      guessnum = guessnum + guessnum//2
      print("Is it",guessnum,"? (too high/too low)")
