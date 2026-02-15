#pop_clear

list=input("enter list separated by space:").split()
index=int(input("enter index to pop:"))
if 0<=index<len(list):
    popped=list.pop(index)
    print("popped:",popped)
    print("list after pop:",list)
else:
    print("invalid index")
choice=input("clear list? (yes/no): ").lower()
if choice=="yes":
    list.clear()
    print("list cleared:",list)
