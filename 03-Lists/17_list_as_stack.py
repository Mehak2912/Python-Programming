#list_as_stack

stack=[]
while True:
    action=input("Push, Pop, or Quit:").lower()
    if action=='push':
        item=input("enter item:")
        stack.append(item)
        print("Stack:",stack)
    elif action=='pop':
        if stack:
            popped=stack.pop()
            print("Popped:",popped)
            print("Stack:",stack)
        else:
            print("stack empty")
    elif action=='quit':
        break
