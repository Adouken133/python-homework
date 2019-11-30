import pandas as pd
import matplotlib.pyplot as plt
import os
wine = pd.read_csv(filepath_or_buffer='wine.data',header=0)
to_wine = wine.to_string()
wine_DS = wine.describe()
wine_INFO = wine.info()
wine_cor = wine.corr()

#os.makedirs('plots')
# 1 Column by line chart
plt.plot(wine['Alcohol'], color='blue')
plt.title('Alcohol by Index')
plt.xlabel('Index')
plt.ylabel('Alcohol')
plt.savefig(f'plots/Alcohol_by_index_plot.png', format='png')
plt.clf()

#2 column by scatterplot
plt.scatter(wine['Alcohol'], wine['Malic Acid'], color='b')
plt.title('Alcohol to Malic Acid')
plt.xlabel('Malic Acid')
plt.ylabel('Alcohol')
plt.savefig(f'plots/Malic Acid_to_Alcohol.png', format='png')

plt.close()




#print(to_wine)
#print(wine_DS)
#print(wine_INFO)
#print(wine_cor)
