import pandas as pd
data = {
    'Name' : ['Alice','Bob','Charlie','David','Eve'],
    'Age' : [25,30,35,40,22],
    'city' : ['New York','los angels', 'chicago', 'houston', 'phoenix']
}
# Creating DataFrame
df = pd.DataFrame(data)
print(df)

# Adding New Column
df['score'] = [85,90,78,92,88]
print(df)

# Modifying the score column by adding 5 points
df['score'] = df['score'] + 5
print(df)

# Deleting a city column
df = df.drop('city', axis=1)
print(df)

# Sorting by age in ascending order
sorted_by_age = df.sort_values(by='Age')
print(sorted_by_age)

# Sorting by age in descending order
sorted_by_index = df.sort_index(ascending=False)
print(sorted_by_index)

# Renaming the column name
df = df.rename(columns ={'score': 'final_score'})
print(df)

# creating a dataframe with missing values
data_with_nan = {
    'Name' : ['Alice','Bob','Charlie','David','Eve'],
    'Age' : [25,None,35,None,22],
    'score' : [85,90,None,92,88]
}
# Creating DataFrame
df_nan = pd.DataFrame(data_with_nan)

# filling missing values in 'age' with the mean age
df_nan['Age'] = df_nan['Age'].fillna(df_nan['Age'].mean())
print(df_nan)

# filling missing values with fixed value
df_nan['score'] = df_nan['score'].fillna(0)
print(df_nan)

# dropping rows with any missing values
df_dropped = df_nan.dropna()
print(df_dropped)

# replacing specific values in the column
df_nan['Name'] = df_nan['Name'].replace({'Alice':'Alicia','Bob':'Robert'})
print(df_nan)

# replacing score 0 to N/A
df_nan['score'] = df_nan['score'].replace(0,'N/A')
print(df_nan)

# Indexing
df_new = df_nan.drop(df_nan.index[1:4])
print(df_new)

# indexing and selection
subset = df_nan.loc[1:2,['Name','score']]
print(subset)