"""4. Swap Two Variables

Without using a third variable, swap:

a = 5
b = 10

Expected Output

a = 10
b = 5   """
a = 5
b = 10
a, b = b, a
print("a =", a)
print("b =", b)