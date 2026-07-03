"""Take an integer as input.

Store whether it is even in a Boolean variable.

Print the Boolean value."""

number = int(input("Enter an integer: "))
is_even = (number % 2 == 0)
is_odd = (number % 2 != 0)
print("Is the number even?", is_even)
print("Is the number odd?", is_odd)
print("Type of the variable is:", type(is_even))
print("Type of the variable is:", type(is_odd))