# This is a simple Python project day 2.
# Tip Calculator

# Welcome to the tip calculator.
# What was the total bill?
# How many people to split the bill?
# What Percentage tip would you like to give? 10, 12, or 15?
# Each person should pay:
# Test Commit

print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
people = float(input("How many people to split the bill? "))
tip = float(input("What Percentage tip would you like to give? 10, 12, or 15? "))
result = round((bill / people) * (tip / 100 + 1), 2)
print(f"Each person should pay: {result}$")
