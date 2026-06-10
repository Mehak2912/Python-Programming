#tuple_indexing_slicing

items=input("enter items separated by space:").split()
my_tuple=tuple(items)
print(my_tuple)
index=int(input("enter index: "))
if 0<=index<=len(my_tuple):
    print("Item at index: ",my_tuple[index])
else:
    print("Invalid index")
start=int(input("enter starting point:"))
end=int(input("enter ending point: "))
print("slice:",my_tuple[start:end])
