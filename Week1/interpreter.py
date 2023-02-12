x, y, z = input("Expression: ").split()

x, z = int(x), int(z)
if y == "+":
    ans = x + z
elif y == "-":
    ans = x - z
elif y == "*":
    ans = x * z
else:
    ans = x / z

print(f"{ans:.1f}")
