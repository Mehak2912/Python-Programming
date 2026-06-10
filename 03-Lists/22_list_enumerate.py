#list_enumerate

my_list=input("enter list separated by space: ").split()
for index, item in enumerate(my_list):
    print(f"Index {index}:{item}")
