# Purpose: Demonstrate booleans, comparison operators, and flow control

age = 16
has_permission = True     # Boolean value
is_weekend = False        # Boolean value

# Flow control starts here using if, elif, else
if age > 17 and has_permission:   # Uses > and boolean AND
    print("You can drive alone.")

elif age >= 16 and has_permission:  # Uses >=
    print("You can drive with supervision.")

elif age < 16 or not has_permission:  # Uses <, OR, and NOT
    print("You cannot drive yet.")

else:
    print("Driving status unclear.")

# Showing all comparison operators
x = 5
y = 10

print(x == y)   # equal to
print(x != y)   # not equal to
print(x > y)    # greater than
print(x < y)    # less than
print(x >= y)   # greater or equal
print(x <= y)   # less or equal
