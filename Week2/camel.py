camel = input("camelCase: ").strip()

snake = "".join(["_" + ch.lower() if ch.isupper() else ch for ch in camel])
print("snake_case:", snake)
