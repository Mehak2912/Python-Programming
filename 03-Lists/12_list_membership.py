#list_membership 

my_list=input("enter list separated by space:").split()
item=input("enter item to check:")
print("In list:",item in my_list)
print("Not in list:",item not in my_list)
