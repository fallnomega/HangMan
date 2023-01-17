#imports
import random
import hangman_art
import words_list

word_list = words_list.word_list
stages = hangman_art.stages
print(hangman_art.logo)
print (stages[6])

chosen_word = random.choice(word_list)
display = []
show_display=''

for x in chosen_word:
    display+='_'

you_win = False
word_length = len(chosen_word)
result=""
lives = 6

while you_win==False:
    print(f'Pssst, the solution is: {chosen_word}.')
    guess = input("Guess a letter: ").lower()
    result = ""

    for x in range(word_length):
        letter = chosen_word[x]
        if guess == letter and display[x] is not letter:
            display[x]=letter
            for x in display:
                result += x
        elif guess == letter and display[x] == letter:
            print(f"You have already used '{guess}', try another letter.")
    if guess not in chosen_word:
        print(f"'{guess}' is not in the mystery word. Try again.")
        lives -=1
        print(stages[lives])

    if result == chosen_word:
        you_win=True
        print (f"You WIN! The word was {chosen_word}")
    elif lives==0:
        print ("You Lose after 6 wrong guesses!")
        you_win = True

