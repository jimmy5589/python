lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's','z']
def getAvailableLetters(lettersGuessed):
	import string
	res=string.ascii_lowercase
	for i in lettersGuessed:
                l=res.find(i)
		res=res[:l]+res[l+1:]		
	return res
	
print getAvailableLetters(lettersGuessed)
