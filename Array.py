# Arrays in Python
# https://www.geeksforgeeks.org/array-python-set-1-introduction-functions/

import array as arr

# 1. array(data type, value list) :- This function is used to create an array with data type and value list specified in its arguments.
ar = arr.array('i',[1,2,3])
for i in range (0, 3):
    print (ar[i])

# 2. append() :- This function is used to add the value mentioned in its arguments at the end of the array.
# 3. insert(i,x) :- This function is used to add the value at the position specified in its argument.

# using append() to insert new value at end
ar.append(4)
print(ar)

# using insert() to insert value at specific position
# inserts 5 at 2nd position
ar.insert(2, 5)

print(ar)
