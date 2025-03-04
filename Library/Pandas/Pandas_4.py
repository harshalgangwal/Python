import pandas as pd

data_dict = {
    "studnets" : ["harshal","Harry","harshu"],
    "scores" : [76,56,65]
}

data = pd.DataFrame(data_dict)
data.to_csv('new_data.csv')