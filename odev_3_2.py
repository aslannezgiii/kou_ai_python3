
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data = pd.read_csv('top50.csv')

df = pd.DataFrame(data)
#print(df)

#veri tipinin floata çevrilmesi
df['Danceability'] = df['Danceability'].astype('float')

#ilk 5 verinin gösterilmesi
print(df.head())
plt.figure(figsize=(12,6))

x = np.arange(0.,50.,1.)
x = list(x)

plt.plot(x,df.Danceability,"-p", color="red")

plt.title("Şarkıların Danceability Değerleri")
plt.xlabel("Şarkı numarası")
plt.ylabel("Danceability")
plt.xlim(0,50)
plt.legend('Danceability')
#plt.axis("scaled")
plt.grid(color = 'black', linestyle = '--', linewidth = 0.5)
plt.show()
