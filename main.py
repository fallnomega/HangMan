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
#Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.

display = []
show_display=''
for x in chosen_word:
    display+='_'

#Testing code
print(f'Pssst, the solution is: {chosen_word}.')

#Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
print('Guess a letter: ')
#guess = input("Guess a letter: ").lower()
guess = 'e'

#Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
#Loop through each position in the chosen_word;
#If the letter at that position matches 'guess' then reveal that letter in the display at that position.
#e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].
word_length = len(chosen_word)
for x in range(word_length):
    letter = chosen_word[x]
    if guess == letter:
        display[x]=letter


#Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
#Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.
print(display)
