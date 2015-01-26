balance=4213
annualInterestRate=0.2
monthlyPaymentRate=0.04

def bal(balance, annualInterestRate, monthlyPaymentRate):
    interest=0
    total=0
    for i in range(12):
        lastBalance=balance
        minPayment=lastBalance*monthlyPaymentRate
        monthlyUnpaid=lastBalance-minPayment
        balance=monthlyUnpaid*(1+annualInterestRate/12)
#        print "Month: "+str(i+1)
#        print "Minimum monthly payment: %.2f"%minPayment
#        print "Remaining balance: %.2f"%balance
        total+=minPayment
    print "Total paid: %.2f"%total
    print "Remaining balance: %.2f"%balance
    return balance
    
for i in range(1000):
    mybal=bal(balance, annualInterestRate, monthlyPaymentRate+0.01*i)
    print str(mybal)
    print str(abs(mybal-balance))
    if abs(mybal-balance) < 0.1 and mybal < balance:
        print "res:"+str(0.01*i)
        break