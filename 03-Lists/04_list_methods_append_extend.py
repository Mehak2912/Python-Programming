#list methods append and extend

list=input("enter initial list separated by space:").split()
item=input("enter item to append:")
list.append(item)
print("after append:",list)
more_items=input("enter items to extend separated by spaces:").split()
list.extend(more_items)
print("after extend:",list)
