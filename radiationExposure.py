def f(x):
    import math
    return 10*math.e**(math.log(0.5)/5.27 * x)

def radiationExposure(start, stop, step):
	res=0.0
        i=0.0
        i+=start
        while i < stop:
		res+=f(i)*step
		i+=step
	return res

print str(radiationExposure(0, 5, 1))
print str(radiationExposure(5, 11, 1))
print str(radiationExposure(0, 11, 1))
print str(radiationExposure(40, 100, 1.5))
