#tuple_methods

items=input("enter items separated by space:").split()
my_tuple=tuple(items)
item=input("enter item to count or index: ")
counted=my_tuple.count(item)
print("Count:",counted)
if item in my_tuple:
    index=my_tuple.index(item)
    print("Index:",index)
else:
    print("Item not found")
