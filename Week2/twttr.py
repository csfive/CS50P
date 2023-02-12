s = input("Input: ")

ans = "".join([ch for ch in s if ch.lower() not in "aeiou"])
print("Output:", ans)
