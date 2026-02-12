#menu driven program

print("1. Add\n2. Subtract")
choice=int(input("Enter your choice: "))
a=int(input("enter a:"))
b=int(input("enter b:"))
if choice==1:
    print(a+b)
elif choice==2:
    print(a-b)
