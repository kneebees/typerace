import time
import random

nouns = ['flower', 'girl', 'boy', 'ball', 'piano', 'glasses', 'fire', 'paper', 'phone', 'lion', 'rock', 'stone', 'hair', 'school', 'house', 'sentence', 'game', 'car', 'story', 'list', 'paragraph', 'name', 'time', 'plane', 'book']
verbs = ['ran', 'took', 'was', 'stole', 'looked', 'typed', 'wrote', 'read', 'ignored', 'bugged', 'escaped', 'drank', 'ate', 'robbed', 'invaded', 'lived', 'died', 'charged', 'made', 'broke', 'went']
adjetives = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'cool', 'hot', 'warm', 'cold', 'evil', 'ugly', 'small', 'big', 'sharp', 'dull', 'bright', 'dark', 'nice', 'reliable', 'troublesome']
adverbs = ['slowly', 'quickly', 'beautifully', 'blindly', 'knowingly', 'lazily', 'happily', 'sadly', 'angrily', 'worriedly', 'skillfully']
pronoun = ['he', 'she', 'they', 'it']
determiner = ['the', 'a', 'that', 'every']
conjunction = ['and', 'but', 'because', 'although', 'or']
preposition = ['away', 'with', 'to', 'after', 'before', 'while']
punctuation = ['.', '!', '?']

name = input("What is your name? ").strip().capitalize()

print("Welcome to the game, {}.".format(name))

start = input("Would you like to start (y/n)? ")

def choose():
  global rNoun
  global rVerbs
  global rAdjetives
  global rAdverbs
  global rPronoun
  global rConjunction
  global rPunctuation
  global rPreposition
  global rDeterminer
  rDeterminer = random.choice(determiner)
  rPreposition = random.choice(preposition)
  rNoun = random.choice(nouns)
  rVerbs = random.choice(verbs)
  rAdjetives = random.choice(adjetives)
  rAdverbs = random.choice(adverbs)
  rPronoun = random.choice(pronoun)
  rConjunction = random.choice(conjunction)
  rPunctuation = random.choice(punctuation)

def sentence_types():
  beginning = random.randint(1, 4)
  compound = random.randint(1, 4)
  if beginning == 1:
    choose()
    start = [rDeterminer, rNoun, rVerbs]
  elif beginning == 2:
    choose()
    start = [rPronoun, rAdverbs, rVerbs, rDeterminer, rAdjetives, rNoun]
  elif beginning == 3:
    choose()
    start = [rDeterminer, rAdjetives, rNoun, rAdverbs, rVerbs]
  else:
    choose()
    start = [rPronoun, rVerbs, rPreposition, rDeterminer, rNoun]
  if compound == 1:
    choose()
    end = [rConjunction, rPronoun, rVerbs]
  elif compound == 2:
    choose()
    end = [rConjunction, rDeterminer, rAdjetives, rNoun, rAdverbs, rVerbs]
  elif compound == 3:
    choose()
    end = [rConjunction, rPronoun, rAdverbs, rVerbs]
  else:
    choose()
    end = [rConjunction, rDeterminer, rNoun, rVerbs]
  sentence1 = [start, end]
  sentence2 = [start]
  sentence = [sentence1, sentence2]
  sentence = random.choice(sentence)
  sentence = str(sentence)
  sen = sentence.replace(',', '')
  sen = sen.replace('\'', '')
  sen = sen.replace('[', '')
  sen = sen.replace(']', '')
  choose()
  sent = sen + rPunctuation
  sent = sent.capitalize()
  print(sent, end =' ')

print("\n")

i = 0

for i in range(6):
  sentence_types()

start = time.time()
go = input('\n\n').strip()
end = time.time()

record = end - start
print("\nYour time:", record)

print("\nLeaderboard: \n{}: {}".format(name, record))
