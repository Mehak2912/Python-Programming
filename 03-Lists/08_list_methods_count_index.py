#count_index

l=input("enter numbers separated by space:").split()
item=input("enter item to count/index:")
count=l.count(item)
print("counted:",count)
if item in l:
    index=l.index(item)
    print("index:",index)
else:
    print("item not found")
