balance = 320000
annualInterestRate = 0.2

rate = annualInterestRate / 12.0

lower_bound = balance / 12
upper_bound = (balance * (1 + rate) ** 12) / 12.0
epsilon = 0.01

while True:
    previous_balance = balance
    payment = (lower_bound + upper_bound) / 2.0
    for idx in range(1, 13):
        monthly_unpaid_balance = balance - payment
        balance = monthly_unpaid_balance + rate * monthly_unpaid_balance
    if abs(balance) <= epsilon:
        break
    if balance < 0:
        upper_bound = payment
    else:
        lower_bound = payment
    balance = previous_balance

print("Lowest Payment: " + str(round(payment, 2)))
