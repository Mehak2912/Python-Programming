#copy_shallow deep

import copy
my_list=input("enter list separated by space:").split()
shallow_copy=my_list.copy()
deep_copy=copy.deepcopy(my_list)
print("original:",my_list)
print("shallow_copy:",shallow_copy)
print("deep copy:",deep_copy)
