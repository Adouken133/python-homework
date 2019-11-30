import pandas as pd
from sklearn.datasets import load_wine


wine = pd.read_csv(filepath_or_buffer='wine.data',header=0)
df.columns=['class', 'Alcohol', 'Malic_Acid', 'Ash', 'Alcalinity of Ash', 'Magnesium',
            'Total Phenols', 'Flavanoids', 'Nonflavanoid Phenols', 'Proanthocyanins', 'Colour Intensity', 'Hue',
            'OD280/OD315 of diluted wines', 'Proline']
plt.style.use('ggplot')


# Plotting line chart
plt.plot(df['Ash'], color='blue')
plt.title('Ash by Index')
plt.xlabel('Index')
plt.ylabel('Ash')



#creating a Histogram plot
fig, axes = plt.subplots(1, 1, figsize=(5, 5))
axes.hist(df['Ash'], bins=30, color='g', label='Ash')
axes.set_title('Ash')
axes.set_xlabel('Index')
axes.set_ylabel('Ash')
axes.legend()

#creating mulitiple scatter plots on same figure
fig,axes = plt.subplots(1, 1, figsize=(5,5))
axes.scatter(df['Alcohol'], df['Malic_Acid'], s=8, label='Alc_Mali_Ash', color='Blue', marker='^')
axes.set_title('Alco vs Malic_Acid')
axes.set_xlabel('Alcohol')
axes.set_ylabel('Malic_Acid')
axes.legend()

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

#creating a Pie plot
fig, axes = plt.subplots(1, 1, figsize=(5, 5))
axes.pie(df['class'].value_counts(), labels=df['class'].value_counts().index.tolist(), autopct='%1.1f%%')
axes.set_title('class')
axes.legend()


#creating a Bar plot
fig, axes = plt.subplots(1, 1, figsize=(5, 5))
axes.bar(np.arange(0, len(df['Ash'])), df['Ash'], color='y', label='Ash')
axes.set_title('Ash')
axes.set_xlabel('Index')
axes.set_ylabel('Ash')
axes.legend()


#creating a Correlation Heatmap plot
fig, axes = plt.subplots(1, 1, figsize=(20, 20))
df['encoded_class']=df['class'].map({'B': 0, 'M': 1})
correlation = df.corr().round(2)
im = axes.imshow(correlation)
cbar = axes.figure.colorbar(im, ax=axes)
cbar.ax.set_ylabel('Correlation', rotation=-90, va="bottom")
numrows = len(correlation.iloc[0])
numcolumns = len(correlation.columns)
axes.set_xticks(np.arange(numrows))
axes.set_yticks(np.arange(numcolumns))
axes.set_xticklabels(correlation.columns)
axes.set_yticklabels(correlation.columns)
plt.setp(axes.get_xticklabels(), rotation=45, ha='right', rotation_mode='anchor')
for i in range(numrows):
    for j in range(numcolumns):
        text = axes.text(j, i, correlation.iloc[i, j], ha='center', va='center', color='w')
axes.set_title('Heatmap of Correlation of Dimensions')
fig.tight_layout()


# creating a 3D plot
c1 = df[df['class'] == 1]
c2 = df[df['class'] == 2]
fig = plt.figure()
axes = fig.add_subplot(1, 1, 1, projection='3d')
line1 = axes.scatter(c1['Alcohol'], c1['Malic_Acid'], c1['Ash'])
line2 = axes.scatter(c2['Alcohol'], c2['Malic_Acid'], c2['Ash'])
axes.legend((line1, line2), ('c1', 'c2'))
axes.set_xlabel('Alcohol')
axes.set_ylabel('Malic_Acid')
axes.set_zlabel('Ash')

plt.show()


plt.close()