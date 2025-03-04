import pandas as pd
data = pd.read_csv('weather_data.csv')
# # print(data)
#
# # to convert data into dictionary
# Dict = data.to_dict()
# """print(Dict)"""
#
# # stored all temp values in list
# """List = data["temp"].to_list()
# print(List)"""
#
# # now find out average of temp
# """Sum = 0
# avg_temp = 0
# for i in List:
#     Sum+=i
# avg_temp = Sum / len(List)
# print(avg_temp)"""
#
# """Average_Temp = sum(List) / len(List)
# print(Average_Temp)"""
#
# print("average of temperature is : ", data["temp"].mean())
#
# #  find out maximum temp
#
# print("maximum temperature is : ", data["temp"].max())
#
# #  find out minimum temp
#
# print("minimum temperature is : ", data["temp"].min(3))

# Get Data in columns
print(data["condition"])
print(data.condition)

# Get data in rows
print(data[data.day == "Monday"])

# Get a row with the highest temp
print(data[data.temp == data["temp"].max()])




