import pandas as pd
import matplotlib.pyplot as plt


#Open_file
df = pd.read_csv(filepath_or_buffer='wine.data',header=0)

#Set_column to dataset
df.columns = ['class', 'Alcohol', 'Malic_Acid', 'Ash', 'Alcalinity of Ash',
              'Magnesium', 'Total Phenols', 'Flavanoids', 'Nonflavanoid Phenols', 'Proanthocyanins',
              'Colour Intensity', 'Hue', 'OD280/OD315 of diluted wines', 'Proline']
plt.style.use('ggplot')
#creating mulitiple scatter plots on same figure
#fig,axes = plt.subplots(1, 1, figsize=(5,5))
#axes.scatter(df['Alcohol'], df['Malic_Acid'], s=8, label='Alc_Mali_Ash', color='Blue', marker='^')
#axes.set_title('Alco vs Malic_Acid')
#axes.set_xlabel('Alcohol')
#axes.set_ylabel('Malic_Acid')
#axes.legend()

#creating multipe plots on the same axes
fig, axes = plt.subplots(1, 1, figsize=(5, 5))
axes.scatter(df['Malic_Acid'], df['Ash'], alpha=0.9, label='Ash')
axes.scatter(df['Malic_Acid'], df['Alcalinity of Ash'], alpha=0.9, label='Alcalinity of Ash')
axes.scatter(df['Malic_Acid'], df['Magnesium'], alpha=0.9, label='Magnesium')
axes.scatter(df['Malic_Acid'], df['Alcohol'], alpha=0.9, label='Alcohol')


axes.set_title(f'Malic_Acid_comparsion')
axes.set_xlabel('Malic_Acid')
axes.set_ylabel('Ash/Alcalinity of Ash/Magnesium/Alcohol')
axes.legend()
plt.tight_layout()




plt.show()

plt.close()








