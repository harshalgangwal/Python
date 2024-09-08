Monthly_Income = float(input("Enter Monthly income: "))
Monthly_Expenses = float(input("Enter Total monthly expenses including all expenses: "))

Total_Savings = Monthly_Income - Monthly_Expenses
print("Total Savings of a person is: ", Total_Savings)

Percentage_of_Savings = (Total_Savings/Monthly_Income)*100
print("Percentage of income saved by a person in a month is: ",Percentage_of_Savings,"%")

Percentage_of_Expenses = 100 - Percentage_of_Savings
print("Percentage of income spent by a person in a month is: ",Percentage_of_Expenses,"%")