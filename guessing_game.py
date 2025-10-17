import random

word_bank = ['java', 'python', 'javascript', 'scala', 'typescript']

word = random.choice(word_bank)
attempts = 10

guessWord = ['_'] * len(word)


while attempts > 0:
    
    print("\n" + " ".join(guessWord))

    lettersTried = ""

    if lettersTried == "":
        print("No letters or words tried yet.")
    else:
        print("Letters or word tried: " + lettersTried)

    guess = input("Guess a letter or the entire word: ").lower()

    if (guess not in lettersTried):
        lettersTried += guess + " "

    # Si le joueur devine le mot entier
    if (word == guess):
        print(f"Congratulations! You've guessed the word {word} correctly!")
        break
    
    # Si le joueur devine une lettre ou un caractère invalide
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single alphabetical character or the entire word.")
        continue

    # Si la lettre a déjà été devinée ne perd aucun essai
    if guess in guessWord:
        print("You've already guessed that letter.")
        continue

    # Si la lettre est dans le mot
    if guess in word:
        # Met à jour guessWord avec la lettre devinée
        for index, letter in enumerate(word):
            if letter == guess:
                guessWord[index] = guess
        # Si le mot est complètement deviné
        if '_' not in guessWord:
            print("\n" + " ".join(guessWord))
            print("Congratulations! You've guessed the word correctly!")
            break
    # Si la lettre n'est pas dans le mot
    else:
        attempts -= 1
        print(f"Incorrect guess. You have {attempts} attempts left.")

