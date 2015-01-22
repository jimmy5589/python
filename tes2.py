
print "Please think of a number between 0 and 100!",
a="k"
left=0
right=100
guess=50
while (a != 'c') :
    while a != 'l' and a != 'h' and a != 'c' : 
        a=raw_input("Is your secret number "+str(guess)+"?\nEnter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ",)
        if a != 'l' and a != 'h' and a != 'c' :
            print "Sorry, I did not understand your input."
    if a == 'h':
        right = guess
        a = 'n'
    elif a == 'l':
        left = guess
        a = 'n'
    if a != 'c':
        guess = (left+right)/2
print "Game over. Your secret number was: "+str(guess)
       
