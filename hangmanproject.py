import random
word_list = [
    "apple",
    "banana",
    "cherry",
    "date",
    "elderberry",
    "fig",
    "grape",
    "honeydew",
    "kiwi",
    "lemon",
    "mango",
    "nectarine",
    "orange",
    "papaya",
    "quince",
    "raspberry",
    "strawberry",
    "tangerine",
    "ugli",
    "watermelon"
]

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
chosen_word = random.choice(word_list)
word_length = len(chosen_word)


lives = 6

display = []
for _ in range(word_length):
    display += "_"


end_of_game = False
while not end_of_game:
 guess = input("Guess a letter : ").lower()
 for position in range(word_length):
       letter = chosen_word[position]
    
       if letter == guess:
         display[position] = letter
       

  
 if guess not in chosen_word:
   lives -= 1
   if lives == 0:
       end_of_game = True
       print(f"You lose\n Your word is {chosen_word}")
   print(display)
   if "_" not in display:
      end_of_game = True
      print("You Win")
   print(stages[lives])