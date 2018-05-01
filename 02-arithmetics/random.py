import random

number = random.randint(1, 10)

guess = int(input('What\'s your first guess?'))
guesses = 1

while guess != number:
  if guess < number:
    print('Nope. Higher.')
  elif guess > number:
    print('Nope. Lower.')

  guess = int(input('Try again: '))
  guesses += 1
else:
  print('That\'s it! %d guesses' % guesses)