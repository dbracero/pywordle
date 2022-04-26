from operator import le
import random
import json
from colorama import Fore, Back, Style

LETTERS_COUNT: int = 5

words: list = []
miss: str = '[_]'
result: list = [miss] * LETTERS_COUNT
occurrences: dict = {}
letter_counters: dict = {}
guessed: bool = False

MAX_ATTEMPTS: int = 6

def load_dictionary() -> None:
	with open('dict.json') as f:
		global words
		words = json.load(f)

def load_word(word: str) -> None:
	for letter in word:
		if letter not in occurrences:
			occurrences[letter] = 1
		else:
			occurrences[letter] += 1

def check(attempt: str, word_to_guess: str) -> None:
	letter_counters: dict = {}

	for letter in attempt:
		letter_counters[letter] = 0

	for i in range(len(attempt)):
		letter: str = attempt[i]
		if letter in word_to_guess:
			letter_counters[letter] += 1
			if letter_counters[letter] <= occurrences[letter]:
				if letter == word_to_guess[i]:
					#result[i] = '[' + letter + ']'
					print(Fore.LIGHTGREEN_EX + '[' + letter + ']', end='')
				else:
					#result[i] = '(' + letter + ')'
					print(Fore.LIGHTYELLOW_EX + '(' + letter + ')', end='')
			else:
				#result[i] = miss
				print(Fore.LIGHTRED_EX + miss, end='')
		else:
			#result[i] = miss
			print(Fore.LIGHTRED_EX + miss, end='')
	print(Fore.RESET)

if __name__ == '__main__':
	load_dictionary()
	word_to_guess: str = random.choice(words)
	load_word(word_to_guess)

	attempt_count: int = 0
	while (attempt_count < MAX_ATTEMPTS and not guessed):
		print('Write your guess...')
		attempt: str = input()
		while len(attempt) != 5:
			print('Your guess must have 5 letters!')
			attempt = input()
		while attempt not in words:
			print('Your word must be in the dictionary!')
			attempt = input()
		check(attempt, word_to_guess)
		attempt_count += 1
		if attempt == word_to_guess:
			guessed = True
			print('You guessed it!')
	print('The word was: ' + Fore.GREEN + word_to_guess)
