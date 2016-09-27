
#!/usr/bin/env python -tt
""" File: bankAccount.py """


"""Summary line: Computes the bank acount balance after calculating yearly interest.

Description: This program will takes in three int/float user inputs that represent 
    bank ststement values and return a yearly breakdown of the interest accumulated.
"""

print "This program calculates the future value of a 10-year investment.\n"


anualDeposit = raw_input('Enter the amount invested each year (for 100 dollars enter "100"): ')
anualRate    = raw_input('Enter the annual interest rate (for 1% enter ".01": ')
numberYears  = raw_input('Enter the number of years to compound (for 5 year input "5"): ')


balance_past = 0
for x in range(1, int(numberYears)+1):
    balance_future = (float(balance_past) + float(anualDeposit)) * (1 + float(anualRate))

    print 'year %d: balance of $%d, a gain of $%d' % (x, balance_future, balance_future - balance_past)

    balance_past = balance_future


