balance=4213
annualInterestRate=0.2
monthlyPaymentRate=0.04

interest=0
total=0
for i in range(12):
        lastBalance=balance
        minPayment=lastBalance*monthlyPaymentRate
        monthlyUnpaid=lastBalance-minPayment
        balance=monthlyUnpaid*(1+annualInterestRate/12)
        print "Month: "+str(i+1)
        print "Minimum monthly payment: %.2f"%minPayment
        print "Remaining balance: %.2f"%balance
        total+=minPayment
print "Total paid: %.2f"%total
print "Remaining balance: %.2f"%balance
