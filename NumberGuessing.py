# Number Guessing Game
import random


def play_again():
  userinput = int(input("Welcome to the number guessing game! Would you like to play computer guessing mode (1) or human mode (2)? "))
  if userinput == 1:
    print("Entering computer guessing mode...")
    guessnum = int(input("What is the maximum number that I can guess? "))
    guessnum = guessnum//2
    prevnum = guessnum
    userinput = input(f"Is it {guessnum}? (too high/too low/yes) ")
    if userinput == "high":
      guessnum = guessnum//2
      userinput = input(f"Is it {guessnum}? ")
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
          userinput = input(f"Yay! I guessed correctly. The number is {guessnum}. Play again?(yes/no) ")
          if userinput != "yes":
            print("Okay!")
            exit()
          else:
            play_again()

    if userinput == "low":
      guessnum = guessnum + guessnum//2
      userinput = input(f"Is it {guessnum}? ")
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
          userinput = input(f"Yay! I guessed correctly. The number is {guessnum}. Play again?(yes/no) ")
          if userinput != "yes":
            print("Okay!")
            exit()
          else:
            play_again()
    if userinput == "yes":
      userinput = input(f"Yay! I guessed correctly. The number is {guessnum}. Play again?(yes/no) ")
      if userinput != "yes":
        print("Okay!")
        exit()
      else:
        play_again()
      
  if userinput == 2:
    print("Entering Human Guessing Mode...")
    userinput = int(input("Enter the maxinum number I can think of: "))
    rannum = random.randint(1,userinput)
    print("I am thinking of a random number between 1 and",userinput,". I will tell you whether your guess was too high or too low until you guess right.")
    while True:
      userinput = int(input("What is my number? "))
      if userinput > rannum:
        print("""The number is too high.
              
              """)
      if userinput < rannum:
        print("""The number is too low.
              
              """)
      if userinput == rannum:
        userinput = input(f"Yay! You guessed correctly! The number is {rannum}. Would you like to play again? (yes/no) ")
        if userinput != "yes":
          exit()
        else:
          play_again()

play_again()