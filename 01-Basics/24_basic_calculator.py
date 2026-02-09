a=float(input("enter first number:"))
op=input("enter operator(+ - * /):")
b=float(input("enter second number:"))
if op=='+':
    print("result:",a+b)
elif op=='-':
    print("result:",a-b)
elif op=='*':
    print("result:",a*b)
elif op=='/':
    if b==0:
        print("invalid")
    else:
        print("result:",a/b)
else:
    print("invalid")
