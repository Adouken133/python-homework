import numpy as np
#Number 2 question
list = [1,22,4,5,35,4,6,7,3,8,40]
first_array = np.array(list)
first_ndim = first_array.ndim
first_shape = first_array.shape
first_size = first_array.size
first_type = first_array.dtype

#Number 3 question
list2 = [['a', 'b'],['c', 'd'],[3, 3]]
first_matrix = np.matrix(list2)
ndim_matrix = first_matrix.ndim
shape_matrix = first_matrix.shape
size_matrix = first_matrix.size
type_matrix = first_matrix.dtype

#number 4 question
numpy1_arange = np.arange(1,15)
numpy1_rand = np.random.randint(numpy1_arange)

#number 5 question
numpy2_zero = np.zeros([3,5])
numpy2_rand = np.random.randint([3,5])

#nuumber 6 question
Arra = np.array([7,7]*10)
Rearra = Arra.reshape(4,5)

#number 7 question
int_array = np.array([36,36]*18)
reshape_matrix = int_array.reshape(6,6)
first_element = reshape_matrix.shape[0]
first_two_rows = reshape_matrix[0:2,:]
last_two_rows = reshape_matrix[4:6,:]
mid_two_rows = reshape_matrix[3:5,:]
last_column = reshape_matrix[:,5:6]
two_mid_columns = reshape_matrix[3:5,3:5]
average = reshape_matrix.mean()
min = reshape_matrix.min()
max = reshape_matrix.max()
std = reshape_matrix.std()


#print(first_array)
#print(first_ndim)
#print(first_shape)
#print(first_size)
#print(first_type)
#print(first_matrix)
#print(ndim_matrix)
#print(shape_matrix)
#print(size_matrix)
#print(type_matrix)
#print(numpy1_arange)
#print(numpy1_rand)
#print(numpy2_zero)
#print(numpy2_rand)
#print(Arra)
#print(Rearra)
#print(first_element)
#print(first_two_rows)
#print(last_two_rows)
#print(mid_two_rows)
#print(last_column)
#print(two_mid_columns)
#print(average)
#print(min)
#print(max)
#print(std)