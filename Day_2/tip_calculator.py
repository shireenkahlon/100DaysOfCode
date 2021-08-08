print("Welcome to the tip calculator!!")
print('--------------------------------------------')
#ask for the final bill
final_bill = float(input("What was the total bill?\n$ "))
#how many people to divide the bill
divide_bill = int(input('How many people to split the bill?\n '))
#percentage of tip
tip = int(input('What percentage of tip would you like to give? Example: 15, 20, 25\n '))
#convert the tip to a percent, multiply and add it to the bill to get the final bill with tip
tip_bill = tip/100 * final_bill + final_bill
#divide the bill including tip with the number of people
results = tip_bill / divide_bill
#print statement
print(f'Each person should pay ${results:.2f}')