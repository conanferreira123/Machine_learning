#use nditer() for numpy array iteration
import numpy as np

#iterate 1 D array
np1=np.array([1,2,3,4,5,6,7,8,9,10])
for i in np1:
    print(i)
#prints all elements of array(unlike java/C++ we dont use np1[i] to print elements,we use only i in python)

#iterate through 2 D array
np2=np.array([[1,2,3,4,5],[6,7,8,9,10]])
for i in np2:
    #print(i) #this prints only the rows(subarrays)
    for j in i:
        print(j)#prints individual elements in the subarrays
        
#iterate through 3 D array
np3 = np.array([[[1, 2], [3, 4], [5, 6]], [[7, 8], [9, 10],[11,12]]])
for i in np3:
    for j in i:
        for k in j:
            print(k)
            
#iterating using np.nditer()
for i in np.nditer(np3):
    print(i)

for i in np.nditer(np2):
    print(i)
    
