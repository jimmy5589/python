secretWord = 'apple' 
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
def getGuessedWord(secretWord, lettersGuessed):
	res=''
	for i in secretWord:
		if i not in lettersGuessed:
		   res+='_'
		else:
		   res+=i
	return res
	
print getGuessedWord(secretWord, lettersGuessed)
