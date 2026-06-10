#Tuple_immutability

items=input("enter items separated by space:").split()
my_tuple=tuple(items)
try:
    my_tuple[0]="new_item"
except TypeError as e:
    print("Tuple is immutable:", e)
