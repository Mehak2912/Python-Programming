#list_filtering

nums=input("enter numbers separated by space:").split()
nums=[int(x) for x in nums]
even_nums=[int(x) for x in nums if x%2==0]
print("even numbers:",even_nums)
