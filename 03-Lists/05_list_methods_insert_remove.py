#list methods insert and remove

list=input("enter initial list separated by space:").split()
index=int(input("enter index to insert:"))
item=input("enter item to insert:")
list.insert(index,item)
print("after insert:",list)
item_remove=input("enter item to remove:")
if item_remove in list:
    list.remove(item_remove)
    print("after remove:",list)
else:
    print("item not found")
