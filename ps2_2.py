balance=3926
annualInterestRate=0.2

def getBalance(minPayment):
   global balance
   global annualInterestRate
   lbalance=balance
   interest=0
   total=0
   for i in range(12):
        lastBalance=lbalance
        monthlyUnpaid=lastBalance-minPayment
        lbalance=monthlyUnpaid*(1+annualInterestRate/12)
        total+=minPayment
   return lbalance

min=10
while True:
   b=getBalance(min)
   if b <= 0:
      break
   else:
      min += 10

print "Lowest Payment: "+str(min)

