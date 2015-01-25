balance=999999
annualInterestRate=0.18

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

monthlyInterestRate=annualInterestRate/12
low=balance/12
upp=(balance*(1+monthlyInterestRate)**12)/12

while True:
   min=(low+upp)/2
   b=getBalance(min)
   if abs(b) < 0.1:
      break
   elif b > 0:
      low=min
   else:
      upp=min

print "Lowest Payment: %.2f"%min

