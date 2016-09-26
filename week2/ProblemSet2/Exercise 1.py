# balance - the outstanding balance on the credit card
# annualInterestRate - annual interest rate as a decimal
# minimum_monthly_payment_rate - minimum monthly payment rate as a decimal
balance = 484
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

rate = annualInterestRate / 12.0
for idx in range(1, 13):
    payment = monthlyPaymentRate * balance
    monthly_unpaid_balance = balance - payment
    balance = monthly_unpaid_balance + rate * monthly_unpaid_balance
    # print("Month " + str(idx) + " Remaining balance: " + str(round(balance, 2)))
print("Remaining balance: " + str(round(balance, 2)))
