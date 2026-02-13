#list indexing

items=input("enter items separated by space:").split()
index=int(input("enter index:"))
if 0<=index<len(items):
    print("item at index:",items[index])
else:
    print("invalid index")
