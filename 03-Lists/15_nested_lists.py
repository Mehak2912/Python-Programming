#nested_lists

rows=int(input("enter number of rows:"))
nested_list=[]
for i in range(rows):
    row=input(f"enter row {i+1} separated by space:").split()
    nested_list.append(row)
print("nested_list:",nested_list)
