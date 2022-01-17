# You are in the restaurant, calculate the tip and split between members

print("Welcome to the tip calculator!\n")
name = input("what is youre name? ")
print("Hello"+" "+name)
total_bill = int(input("What is your total bill? "))
tip_percent = int(input("What perentage of tip would you like to give? "))
result_bill = total_bill + (tip_percent*total_bill)/100
split_members = int(input('How many people will split the bill? '))
bill_per_member = result_bill/split_members
print(f"Every member have to pay {bill_per_member}")
print("\n\n Thank You!")