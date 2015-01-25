def oddTuples(aTup):
    res = ()
    for i in range(0,len(aTup),2):
        res+=(aTup[i],)
    return res
    
x=('I', 'am', 'a', 'test', 'tuple')
y=oddTuples(x)
print y

