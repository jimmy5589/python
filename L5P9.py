def semordnilap(str1, str2):
    if len(str1)==1:
        return str1==str2
    elif str1[0]==str2[len(str2)-1]:
        print str1[1:]+" "+str2[:len(str2)-1] 
        return semordnilap(str1[1:],str2[:len(str2)-1])
    else:
        return False
    
print semordnilap("abc","cbf")
