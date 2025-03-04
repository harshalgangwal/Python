import pandas as pd

data = pd.read_csv('Squirrel_Census_date.csv')
gray_Squirrel_count = len(data[data["Primary Fur Color"] == "Gray"])
print(gray_Squirrel_count)

red_Squirrel_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
print(red_Squirrel_count)

black_Squirrel_count = len(data[data["Primary Fur Color"] == "Black"])
print(black_Squirrel_count)

data_dict = {
    "For color":["Gray","Cinnamon","Black"],
    "Count":[gray_Squirrel_count,red_Squirrel_count,black_Squirrel_count]
}

df = pd.DataFrame(data_dict)
df.to_csv('Squirrel_count.csv')