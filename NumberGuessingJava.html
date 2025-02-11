// Number Guessing Game
const readline = require('readline').createInterface({
  input: process.stdin,
  output: process.stdout
});

function playAgain() {
  readline.question("Welcome to the number guessing game! Would you like to play computer guessing mode (1) or human mode (2)? ", (userInput) => {
    userInput = parseInt(userInput);
    if (userInput === 1) {
      console.log("Entering computer guessing mode...");
      readline.question("What is the maximum number that I can guess? ", (maxNum) => {
        maxNum = parseInt(maxNum);
        let guessNum = Math.floor(maxNum / 2);
        let prevNum = guessNum;
        askQuestion(guessNum, prevNum);
      });
    } else if (userInput === 2) {
      console.log("Entering Human Guessing Mode...");
      readline.question("Enter the maximum number I can think of: ", (maxNum) => {
        maxNum = parseInt(maxNum);
        const randNum = Math.floor(Math.random() * maxNum) + 1;
        console.log(`I am thinking of a random number between 1 and ${maxNum}. I will tell you whether your guess was too high or too low until you guess right.`);
        humanGuess(randNum);
      });
    }
  });
}

function askQuestion(guessNum, prevNum) {
  readline.question(`Is it ${guessNum}? (too high/too low/yes) `, (userInput) => {
    if (userInput === "high") {
      guessNum = Math.floor(guessNum / 2);
      askQuestionLoop(guessNum, prevNum);
    } else if (userInput === "low") {
      guessNum += Math.floor(guessNum / 2);
      askQuestionLoop(guessNum, prevNum);
    } else if (userInput === "yes") {
      readline.question(`Yay! I guessed correctly. The number is ${guessNum}. Play again? (yes/no) `, (response) => {
        if (response !== "yes") {
          console.log("Okay!");
          readline.close();
        } else {
          playAgain();
        }
      });
    }
  });
}

function askQuestionLoop(guessNum, prevNum) {
  readline.question(`Is it ${guessNum}? (too high/too low/yes) `, (userInput) => {
    if (userInput === "high") {
      if (prevNum < guessNum) {
        guessNum -= Math.floor((guessNum - prevNum) / 2);
        prevNum = 2 * guessNum - prevNum;
      } else {
        guessNum -= Math.floor((prevNum - guessNum) / 2);
        prevNum = Math.floor((2 * guessNum + prevNum) / 3);
      }
      askQuestionLoop(guessNum, prevNum);
    } else if (userInput === "low") {
      if (prevNum < guessNum) {
        guessNum += Math.floor((guessNum - prevNum) / 2);
        prevNum = Math.floor((2 * guessNum + prevNum) / 3);
      } else {
        guessNum += Math.floor((prevNum - guessNum) / 2);
        prevNum = 2 * guessNum - prevNum;
      }
      askQuestionLoop(guessNum, prevNum);
    } else if (userInput === "yes") {
      readline.question(`Yay! I guessed correctly. The number is ${guessNum}. Play again? (yes/no) `, (response) => {
        if (response !== "yes") {
          console.log("Okay!");
          readline.close();
        } else {
          playAgain();
        }
      });
    }
  });
}

function humanGuess(randNum) {
  readline.question("What is my number? ", (userInput) => {
    userInput = parseInt(userInput);
    if (userInput > randNum) {
      console.log("The number is too high.\n");
      humanGuess(randNum);
    } else if (userInput < randNum) {
      console.log("The number is too low.\n");
      humanGuess(randNum);
    } else {
      readline.question(`Yay! You guessed correctly! The number is ${randNum}. Would you like to play again? (yes/no) `, (response) => {
        if (response !== "yes") {
          readline.close();
        } else {
          playAgain();
        }
      });
    }
  });
}

playAgain();

