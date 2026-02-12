#continue statement

n=int(input("Enter n:"))
for i in range(1,11):
    if i==n:
        continue  #skips the n
    print(i)
