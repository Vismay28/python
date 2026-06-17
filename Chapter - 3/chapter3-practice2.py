# Question on slicing
# Print middle 3 characters
# Print last 2 characters

str = input("Enter a string: ")
mid = len(str)//2
mid3 = str[mid-1 : mid+1]
print(mid3)

last2 = str[-2:]
print(last2)