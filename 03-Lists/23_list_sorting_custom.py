#list_sorting_custom

words=input("Enter words separted by spaces: ").split()
sorted_words=sorted(words,key=len)
print("Sorted by length:",sorted)
