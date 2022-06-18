import random
import hangman_words
import hangman_art

word_bank = hangman_words.word_list

pictures = hangman_art.picture_bank
print("Welcome to Hangman")
print(hangman_art.logo)
print(pictures[0])

random_word = random.choice(word_bank)
blank_number = len(random_word)
placeholder = ["_"] * blank_number
complete = False
print(random_word)
j=0
already_guessed = []
while not complete:
  letter_guess = input("\nPlease enter your guess: ").lower()
  i = 0
  
  for letter in random_word:
    
    
    if letter_guess == letter:
      placeholder[i] = letter_guess
      if letter_guess not in already_guessed:
        already_guessed.append(letter_guess)
      else:
        print(f"\nYou already guessed the letter {letter_guess}.")
      
    i += 1
    
  print("\n" + "".join(placeholder))
  if "_" not in placeholder:
    complete = True
    print("\nYou win")
  if letter_guess not in random_word:
    if letter_guess not in already_guessed:
      already_guessed.append(letter_guess)
      j += 1
      print(pictures[j])
      if j < 6:
        print("\nWrong. Please Try Again\n")
      if j == 6:
        print("\nGAME OVER")
        complete = True
    else:
      print(f"\nYou have already guessed the letter {letter_guess}. This letter is not in the word.")
    