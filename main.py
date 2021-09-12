
import pandas as pd
from datetime import datetime

#start_time = datetime.now()

df = pd.read_csv('dataset.csv', error_bad_lines=False, names=["Age", "Condition", "Date", "Drug", "DrugId", "EaseofUse", "Effectiveness", "Reviews", "Satisfaction", "Sex", "Sides", "UsefulCount"])


rows_count = len(df.index)

print(rows_count)

df = df.iloc[:10]
print(df)
print()
print()
df = df.dropna(axis=0)
df = df.dropna(axis=1)
df = df.drop('DrugId',axis=1)
df = df.drop('Date',axis=1)
df = df.drop('UsefulCount',axis=1)
#df['UsefulCount'] = df['UsefulCount'].replace(df.at[0,'UsefulCount'], filter(str.isdigit, df.at[0,'UsefulCount']))
print(df)

#print('DELETE EMPTY ROWS')

#df = df.dropna(how="any", axis=0)
#print(df)

#file_data_location = 'C:\\Users\\user\Desktop\\thesis\\data.xlsx'
#dataset = pd.read_excel(file_data_location, engine='openpyxl')#, names=["Age", "Condition", "Date", "Drug", "DrugId", "EaseofUse", "Effectiveness", "Reviews", "Satisfaction", "Sex", "Sides", "UsefulCount"])
#print(dataset)

#print('print columns')

#dataset = dataset.iloc[:5]
#print(dataset)

#nan_value = float("NaN")
#dataset = dataset.replace("", nan_value, inplace=True)
#dataset = dataset.dropna(subset = ["Age"], inplace=True)
#print(dataset)


#end_time = datetime.now()

#print('Duration: {}'.format(end_time - start_time))

