total = int(input('How much money do you have in your pocket?\n'))

# YOUR CODE HERE

if total >= 100:
    print("Give me your money!")
elif total in range(51,99):
    print("Buy me some coffe you cheap!")
else:
    print("You are a poor guy, go away!")