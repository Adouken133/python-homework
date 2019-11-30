import pandas as pd
#question number 2
insurance = pd.read_csv(filepath_or_buffer='insurance.csv', sep=',', header=0)
open_dataframe = insurance.to_string()
datacolumn = insurance.columns
dataindex = insurance.index
datatypes = insurance.dtypes
datashape = insurance.shape
datainfo = insurance.info()
data_describe = insurance.describe()

#question number 3
column_age = insurance['age']

#question number 4
Mutli_column = insurance[['age','children','charges']]

#question number 5
First_5_age = insurance.iloc[0:5,0:1]
First_5_children = insurance.iloc[0:5,3:4]
First_5_charges = insurance.iloc[0:5,6:7]

#question number 6
charges_average = insurance['charges'].mean()
charges_min = insurance['charges'].min()
charges_max = insurance['charges'].max()

#question number 7
insurance_charge = insurance['charges'] == 10797.3362
info = insurance[insurance_charge]

#question number 8
max = insurance['charges'] == charges_max
max_info = insurance[max]

#question number 9
region = insurance['region'].value_counts()

#question number 10
children = insurance['children'].value_counts()

#question number 11
correlation_four = insurance.corr().to_string()

#question number 12
method_way = insurance.corr()


print(open_dataframe)
#print(datacolumn)
#print(dataindex)
#print(datatypes)
#print(datashape)
#print(datainfo)
#print(data_describe)
#print(column_age)
#print(Mutli_column)
#print(First_5_lines)
#print(First_5_children)
#print(First_5_charges)
#print(charges_average)
#print(charges_min)
#print(charges_max)
#print(info)
#print(max_info)
#print(region)
#print(children)
print(correlation_four)
#print(method_way)

