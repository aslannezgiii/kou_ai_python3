
import pandas as pd

data = pd.read_csv('top50.csv')

df = pd.DataFrame(data)
#print(df)

result  = df.groupby("Genre").groups

print(result)
