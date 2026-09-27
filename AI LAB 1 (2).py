import random

words = ["sneakers","propaganda","performance","project","behaviour","boots","appothecary","unjust","imagination","aware","sleepless","together","pretend","bingo","feelings","potato","pesto","cinnamon","wanted","germany","persue","habit","happen","reason", "python", "school", "computer", "console","debug","problems","microsoft","gesture","crossside","driving","mysterious","hangman","treason"]
word = random.choice(words)
guessed_word = ["_"] * len(word)
wrong_choice = 0
hangman = [
    """
       -----
       |   |
           |
           |
           |
           |
    =========
    """,

    """
       -----
       |   |
       O   |
           |
           |
           |
    =========
    """,

    """
       -----
       |   |
       O   |
       |   |
           |
           |
    =========
    """,

    """
       -----
       |   |
       O   |
      /|   |
           |
           |
    =========
    """,

    """
       -----
       |   |
       O   |
      /|\\  |
           |
           |
    =========
    """,

    """
       -----
       |   |
       O   |
      /|\\  |
      /    |
           |
    =========
    """,

    """
       -----
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    =========
    """
]

print("--- HANGMAN GAME ---")

while wrong_choice < 6 and "_" in guessed_word:
    print(hangman[wrong_choice])
    print("Word:", " ".join(guessed_word))
    guess = input("Enter a letter: ").lower()

    if guess in word:
        print("Correct guess :)")

        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess

    else:
        wrong_choice += 1
        print("Wrong guess :(")

print(hangman[wrong_choice])

if "_" not in guessed_word:
    print("🎉 You won  ^ ^")
    print("The word was:", word)
else:
    print("You lost > <")
    print("The word was:", word)
