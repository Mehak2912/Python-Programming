#tuple_operations

tup1=tuple(input("enter first tuple items separated by space:").split())
tup2=tuple(input("enter second tuple items separated by space:").split())
concatenated=tup1+tup2
print("Concatenated:",concatenated)
n=int(input("enter a repetition factor: "))
repetition=tup1*n
print("Repetition:",repetition)
