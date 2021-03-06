# Dan Yee
# CINF 108 - Programming for Problem Solving
# Assignment #2 - Compound Interest Calculator with Incentives 

principalAmount = float(input("Enter the principal balance: "))                                                                     # prompt the user for the principal balance and stores it in a variable
interestRate = float(input("Enter the interest rate as a percent: "))                                                               # prompt the user for the interest rate and stores it in a variable
compoundFrequency = float(input("How many times per year is the interest compounded? "))                                            # prompt the user for the compound frequency and stores it in a variable
compoundYears = float(input("How many years will the account earn interest? "))                                                     # prompt the user for the interest time and stores it in a variable

incentiveRate = 0                                                                                                                   # default extra rate is 0
if principalAmount >= 5100 and principalAmount <= 11000:                                                                            
    incentiveRate = (0.5 / 100)                                                                                                     # extra 0.5% if 5100 <= principal <= 11000
elif principalAmount >= 11001 and principalAmount <= 60000:
    incentiveRate = (0.75 / 100)                                                                                                    # extra 0.75% if 11001 <= principal <= 60000
elif principalAmount > 60000:
    incentiveRate = (1.25 / 100)                                                                                                    # extra 1.25% if principal > 60000

# calculates and stores the accumulated balance after compound interest and any extra incentive rates
accumulatedValue = principalAmount * ((1 + ((interestRate / 100) + incentiveRate) / compoundFrequency) ** (compoundFrequency * compoundYears))

bonus = 0                                                                                                                           # default bonus given is 0
if compoundYears >= 12 and interestRate >= 6:                                                                                       
    bonus = (principalAmount * 0.01) * compoundYears                                                                                # bonus of 1% of principal times number of years compounded if compoundYear >= 12 and interestRate >= 6

accumulatedValue += bonus                                                                                                           # adds bonus to final accumulated bonus
if(interestRate > 11):
    accumulatedValue += 75                                                                                                          # adds 75 to final accumulated value if original rate > 11

print("\nAt the end of ", compoundYears, " years, you will have $", format(accumulatedValue, ",.2f"), sep = "")                     # display the accumulated value after compound interest rounded to 2 decimal places