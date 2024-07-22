immutable_var = (1,2,'a','b')
print(immutable_var)
# immutable_var[0:4] = [3,2,1,0]  "TypeError: 'tuple' object does not support item assignment", кортеж не редактируется.
mutable_list = [1,2,'a','b']
print(mutable_list)
mutable_list [0:4] = [3,2,1,0]
print(mutable_list)