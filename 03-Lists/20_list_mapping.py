#list_mapping

nums=input("enter numbers separated by space:").split()
nums=[int(x) for x in nums]
squares=[x**2 for x in nums]
print("Squares:",squares)
