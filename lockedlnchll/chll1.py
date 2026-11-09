banks_total_deposit = 100000
def Create_Account():
    initial_bal = 20000
    def Accept_Deposit(amount):
        nonlocal initial_bal
        initial_bal += amount
        update_total(amount)
        return initial_bal
    def update_total(amount):
        global banks_total_deposit
        banks_total_deposit += amount
    return Accept_Deposit


account = Create_Account()
print(account(5000))