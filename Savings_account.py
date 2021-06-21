class SavingsAccount():
    def monthly_interest_calc(savings_balance, annual_Inter_rate):
        monthly_interest = (savings_balance)*(annual_Inter_rate)/12
        savings_balance += monthly_interest
        return savings_balance
        
 
saver1=SavingsAccount()
saver2=SavingsAccount()


saver1.savings_balance = float(input(f"Amount saver1 currently has in deposit: "))
saver2.savings_balance = float(input(f"Amount saver2 currently has in deposit: "))

annual_Inter_rate = float(input("Current Anual Interest Rate is: "))/100


Month1_inerest_saver1 = SavingsAccount.monthly_interest_calc(saver1.savings_balance, annual_Inter_rate)
Month1_inerest_saver2 = SavingsAccount.monthly_interest_calc(saver2.savings_balance, annual_Inter_rate)

print(f"Month1 savings balance of saver1 is {Month1_inerest_saver1}")
print(f"Month1 savings balance of saver2 is {Month1_inerest_saver2}")


modified_Inter_rate = float(input("Modified Anual Interest Rate is"))/100


print(f"Month2 savings balance of saver1 is {SavingsAccount.monthly_interest_calc(Month1_inerest_saver1, modified_Inter_rate)}")
print(f"Month2 savings balance of saver2 is {SavingsAccount.monthly_interest_calc(Month1_inerest_saver2, modified_Inter_rate)}")








    
