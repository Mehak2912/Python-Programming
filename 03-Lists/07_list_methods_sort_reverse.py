#sort_reverse

l=input("enter numbers separated by space:").split()
l=[int(x) for x in l]
l.sort()
print("sorted:",l)
l.reverse()
print("reversed:",l)
