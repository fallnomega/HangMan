#imports
import random
#hangman picture

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']


#Randomly choose a word from the word_list and assign it to a variable called chosen_word.
#Create a variable called 'lives' to keep track of the number of lives left.
# Set 'lives' to equal 6.

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


you_win = False
word_length = len(chosen_word)
result=""
print (stages[6])

#If guess is not a letter in the chosen_word,
# Then reduce 'lives' by 1.
# If lives goes down to 0 then the game should stop and it should print "You lose."
lives = 6
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
    if guess not in chosen_word:
        lives -=1
        print(stages[lives])

    if result == chosen_word:
        you_win=True
        print (f"You WIN! The word was {chosen_word}")
    elif lives==0:
        print ("You Lose after 6 wrong guesses!")
        you_win = True

