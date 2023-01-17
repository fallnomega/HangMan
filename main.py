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
selection = random.choice(word_list)
# print(selection)
# print (len(word_list))

word = word_list[2]
#Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
print('Please guess a letter to use')
#guess = input("Please guess a letter to use").lower()
guess = 'c'
#Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

for x in word:
    if guess == x:
        print (f"you have a match in {guess}")
