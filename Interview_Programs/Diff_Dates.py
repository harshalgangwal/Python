import pandas as pd

d1 = "2001-10-11"
d2 = "2023-09-10"

date1 = pd.to_datetime(d1)
date2 = pd.to_datetime(d2)

difference = date2 - date1

print("Difference:", difference)
print("Days:", difference.days)
