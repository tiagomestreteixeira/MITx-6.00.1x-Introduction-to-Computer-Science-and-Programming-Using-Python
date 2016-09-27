balance = 3926
annualInterestRate = 0.2

rate = annualInterestRate / 12.0
payment = 10

while True:
    previous_balance = balance
    for idx in range(1, 13):
        monthly_unpaid_balance = balance - payment
        balance = monthly_unpaid_balance + rate * monthly_unpaid_balance
    if balance < 0:
        break
    payment += 10
    balance = previous_balance

print("Lowest Payment: " + str(round(payment, 2)))
