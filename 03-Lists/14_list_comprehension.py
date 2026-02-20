#list_comprehension

nums=input("enter numbers separated by spaces:").split()
nums=[int(x)for x in nums]
squares=[x**2 for x in nums]
print("Squares:",squares)
