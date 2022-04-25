import random

wordList = ["cat","dog","mouse","snake","brazil"]
wordChosen = random.choice(wordList)
used = []
display = wordChosen
for i in range (len(display)):
  display = display[0:i] + "_" + display[i+1:]
print (" ".join(display))
attempts = 0
while display != wordChosen:
  guess = input("Please enter a letter: ")
  guess = guess.lower()
  used.extend(guess)
  print ("Attempts: ")
  for i in range(len(wordChosen)):
    if wordChosen[i] == guess:
      display = display[0:i] + guess + display[i+1:]
  print("Used letters: ")
  print(used)
  print(" ".join(display))
  attempts = attempts + 1 
print("Well done, you guessed right!")
