user_input = int(input('How many people are coming to your wedding?\n'))

if user_input <= 50:
    price = 4,000
elif user_input in range(51,100):
    price = 10,000
elif user_input in range(101,200):
    price = 15,000
else:
    price = 20,000

print('Your wedding will cost '+str(price)+' dollars')