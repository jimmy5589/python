def isIn(char, aStr):
    if len(aStr)==0:
        return False
    if char==aStr[len(aStr)/2]:
        return True
    elif char > aStr[len(aStr)/2] and len(aStr)/2 > 0:
        return isIn(char, aStr[(len(aStr)/2)+1:])
    elif char < aStr[len(aStr)/2] and len(aStr)/2 > 0:
        return isIn(char, aStr[:(len(aStr)/2)])
    else:
        return False
        
s='abcdefghij'

print isIn('i',s)
