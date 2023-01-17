#imports
import random

#code

#hangman picture

#Randomly choose a word from the word_list and assign it to a variable called chosen_word.

word_list = ['able', 'about', 'account', 'acid', 'across', 'act', 'addition', 'adjustment', 'advertisement', 'after', 'again', 'against',
'agreement', 'air', 'all', 'almost', 'among', 'amount', 'amusement', 'and', 'angle', 'angry', 'animal', 'answer', 'ant',
'any', 'apparatus', 'apple', 'approval', 'arch', 'argument', 'arm', 'army', 'art', 'as', 'at', 'attack', 'attempt',
'attention', 'attraction', 'authority', 'automatic', 'awake', 'baby', 'back', 'bad', 'bag', 'balance', 'ball', 'band',
'base', 'basin', 'basket', 'bath', 'be', 'beautiful', 'because', 'bed', 'bee', 'before', 'behaviour', 'belief', 'bell',
'bent', 'berry', 'between', 'bird', 'birth', 'bit', 'bite', 'bitter', 'black', 'blade', 'blood', 'blow', 'blue', 'board',
'boat', 'body', 'boiling', 'bone', 'book', 'boot', 'bottle', 'box', 'boy', 'brain', 'brake', 'branch', 'brass', 'bread']

chosen_word = random.choice(word_list)

display = []
show_display=''
for x in chosen_word:
    display+='_'

#Testing code

Use a while loop to let the user guess again.
# The loop should only stop once the user has guessed all the letters in
# the chosen_word and 'display' has no more blanks ("_").
# Then you can tell the user they've won.
you_win = False
word_length = len(chosen_word)
result=""

while you_win==False:
    print(f'Pssst, the solution is: {chosen_word}.')
    guess = input("Guess a letter: ").lower()
    result = ""
    for x in range(word_length):
        letter = chosen_word[x]
        if guess == letter:
            display[x]=letter
            for x in display:
                result += x

    if result == chosen_word:
        you_win=True
        print (f"You WIN! The word was {chosen_word}")
