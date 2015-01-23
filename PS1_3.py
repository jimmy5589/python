s = 'abcbacde'

result=s[0]
current=s[0]
for i in range(len(s)-1):
        if s[i]<=s[i+1]:
            current += s[i+1]
        elif len(current) > len(result):
            result = current
            current=s[i+1]
        else:
            current=s[i+1]
if len(current) > len(result):
    result = current        

print "Longest substring in alphabetical order is: "+result
