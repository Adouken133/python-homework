import pandas as pd
import matplotlib.pyplot as plt


#Open_file
wine = pd.read_csv(filepath_or_buffer='wine.data',header=0)

#Set_column to dataset
wine.columns = ['class', 'Alcohol', 'Malic_Acid', 'Ash', 'Alcalinity of Ash', 'Magnesium', 'Total Phenols', 'Flavanoids',
                'Nonflavanoid Phenols', 'Proanthocyanins', 'Colour Intensity', 'Hue', 'OD280/OD315 of diluted wines', 'Proline']

Alcohol = wine['Alcohol']
Hue = wine['Hue']
malic_acid = wine['Malic_Acid']
ash = wine['Ash']
#creating mulitiple plots on same figure
fig,axes = plt.subplots(1,1, figsize=(5,5))
axes[0][0].plot(Alcohol)
axes[0][1].plot(Hue)
axes[1][0].plot(malic_acid)
axes[1][1].plot(ash)

plt.show()
