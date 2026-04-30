# Program takes total bill amount, and number of friends as input
# Calculate how much each person will pay
# Print datatype of each variable used

billAmount = float(input("Enter total bill amount: "))
numberOfFriends = float(input("Enter number of friends: "))
print("Bill amount type: ", type(billAmount))
print("Number of friends type: ", type(numberOfFriends))
splitPerPerson = billAmount / numberOfFriends
print("Each person will pay: ", splitPerPerson, "")
print("Split per person type: ", type(splitPerPerson), "")

x = 5
y = 2
print(x//y)
print(x**y)