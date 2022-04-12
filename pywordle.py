import random

LETTERS_COUNT: int = 5

#TODO: Load words from file"
words: list = ["angel", "pilas", "remar", "indio", "fugaz"]
result: list = [None] * LETTERS_COUNT
occurrences: dict = {}
guessed: bool = False

MAX_ATTEMPTS: int = 6

def load_word(word: str) -> None:
	for letter in word:
		if letter not in occurrences:
			occurrences[letter] = 1
		else:
			occurrences[letter] += 1

def check(attempt: str, word_to_guess: str) -> None:
	partial_occurrences: dict = {}
	for i in range(len(attempt)):
		letter: str = attempt[i]
		if letter not in partial_occurrences:
			partial_occurrences[letter] = 1
		else:
			partial_occurrences[letter] += 1

		if letter == word_to_guess[i]:
			result[i] = "[" + letter + "]"
		elif letter in word_to_guess:
			if partial_occurrences[letter] <= occurrences[letter]:
				result[i] = "(" + letter + ")"
		else:
			result[i] = "[_]"
		

if __name__ == '__main__':
	word_to_guess: str = random.choice(words)
	load_word(word_to_guess)

	attempt_count: int = 0
	while (attempt_count < MAX_ATTEMPTS and not guessed):
		print("Write your guess...")
		attempt: str = input()
		check(attempt, word_to_guess)
		attempt_count += 1
		if attempt == word_to_guess:
			guessed = True
			print("You guessed it!")
		else:
			print(result)
