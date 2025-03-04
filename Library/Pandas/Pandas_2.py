import pandas as pd
import numpy as np

month_names = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
Expenses_values = np.random.randint(300,400, size=12)

monthly_expenses = pd.Series(index=month_names,data=Expenses_values)
print(monthly_expenses)

# Basic Operations
Total_Expenses = monthly_expenses.sum()
print(f"Total sum is {Total_Expenses}")

Avg_Expenses = monthly_expenses.mean()
print(f"Total mean is {Avg_Expenses}")

min_Expenses = monthly_expenses.min()
print(f"minimum value is {min_Expenses}")

max_Expenses = monthly_expenses.max()
print(f"maximum value is {max_Expenses}")

print(monthly_expenses.iloc[2])

# indexing and slicing
print(monthly_expenses[0:3])

# filter
new_series = monthly_expenses > 350
for i in new_series:
    if i == True:


print(new_series)