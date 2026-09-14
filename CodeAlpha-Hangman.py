import random
words = ['Code','Alpha','Intern','Python','Hangman']
word = random.choice(words).lower()

spaces = ['_'] * len(word)
lives = 5

while lives != 0 and '_' in spaces :	
	guess= input('Enter a character : ').lower()
	
	if guess in  word :
		for i in range(len(word)) :
			if word[i] == guess :
				spaces[i] = guess
		print('correct')
	else :
		lives -= 1;
		print(f'wrong! {lives} lives left')
	print(spaces)
	
if '_' not in spaces :
		print('You won! ')
else :
		print(f'You lost! The word was {word} ')
	

		
	