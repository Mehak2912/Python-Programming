#nested if

age=int(input("Enter age:"))
if age>=18:
    has_id=input("do you have ID?(yes/no):").lower()
    if has_id=="yes":
        print("access granted")
    else:
        print("access denied")
else:
    print("not adult")
