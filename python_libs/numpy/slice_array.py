import numpy as np

#slicing numpy arrays
np1=np.array([1,2,3,4,5,6])

#return 2,3,4,5
print(np1[1:5])

#slicing 2 D arrays(tables)
np2=np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(np2[0:,1:3]) #remember here that the first arguement of array stands for columns and 2nd for rows

#3D arrays are not tables(used in nlp,ann,etc.) will learn later