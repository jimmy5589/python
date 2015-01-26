secretWord = 'durian' 
lettersGuessed = []
def isWordGuessed(secretWord, lettersGuessed):
	res=True
	for i in secretWord:
		if i not in lettersGuessed:
		   res=False
		   break
	return res
	
print isWordGuessed(secretWord, lettersGuessed)
