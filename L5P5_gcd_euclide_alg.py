def recurPower(base, exp):
    if exp==0:
        return 1
    else:
        return base*recurPower(base, exp-1)
        
def gcdRecur(a, b):
    """ Euclide Algorithm """
    if b==0:
        return a
    else:
        return gcdRecur(b, a%b)

print str(gcdRecur(9,6))

