#tuple_membership

my_tuple=tuple(input("enter items separated by space:").split())
item=input("Enter item to check: ")
print("In Tuple:",item in my_tuple)
print("Not in Tuple:",item not in my_tuple)
