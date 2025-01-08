import numpy as np

#shape(used to tell the number of elements in each dimension of the array)
np1=np.array([[1,2,3,4,5,6],[7,8,9,10,11,12]])
print(np1.shape) #output:(2,6)

#reshape(used to change the shape of an array)
np2=np1.reshape(-1) #reduces the array by one dimension
print(np2)

np3=np1.reshape(4,3)#converts into 4 rows and 3 columns
print(np3)

np4=np1.reshape(2,3,2)#converts into a 3d array of certain rows and columns(will study this during neural networks)
print(np4)