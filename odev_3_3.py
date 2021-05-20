import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
data = pd.read_csv('top50.csv')

df = pd.DataFrame(data)
#print(df)

result  = df.groupby(["Genre","Energy"]).groups
#print(result)

result  = df.groupby("Genre")["Energy"].mean() #her türün ort enerjisini aldık
#print(result)

#şimdi ortalama enerjiyi bulalım - > her türün ort bulduktan sonra bulalım ort
#çünkü diğer türlü bazı türlerin ort katkısı fazla olur.
result_2 = pd.DataFrame(result) #bunu görselleştirmemiz lazım
#print(result_2)

average  = result_2["Energy"].mean()
#print(average)

result_2.sort_values(by=['Energy'], inplace=True, ascending=True) #listeyi küçükten büyüğe sıraladık (enerjilerine göre)
print(result_2.head())
print("---------------------------------------------------------------")
print(result_2["Energy"][0])
#print(result_2.groupby("Genre")["Energy"])
colors = []
for x in result_2["Energy"]:
    if x < average:
        colors.append('r')
    elif x < average + 6:
        colors.append('b')
    else:
        colors.append('g')

result_2['Energy'].plot(kind='bar', color=colors)
plt.ylabel('Enerji Ortalamaları') #kırmızı -> düşük enerjili , mavi -> orta enerjili, yeşil -> yüksek enerjili
plt.show()
