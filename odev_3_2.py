import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib.ticker as ticker

data = pd.read_csv('top50.csv')

df = pd.DataFrame(data)
#print(df)

#veri tipinin float'a çevrilmesi
df['Danceability'] = df['Danceability'].astype('float')
#ilk 5 verinin gösterilmesi
print(df.head())


x = np.arange(0, 50,1)

# Multiple Locator
fig, ax = plt.subplots(1, 1)
ax.plot(x,df.Danceability,"-p", color="red")
ax.xaxis.set_major_locator(ticker.MultipleLocator(1))

#plt.figure(figsize=(12,6))
#plt.plot(x,df.Danceability,"-p", color="red") # çalışıyor -onar onar artıyor
plt.title("Şarkıların Danceability Değerleri")
plt.xlabel("Şarkı numarası")
plt.ylabel("Danceability")
plt.xlim(0,50)
plt.legend('Danceability')
#plt.axis("scaled")
plt.grid(color = 'black', linestyle = '--', linewidth = 0.5)
plt.show()
