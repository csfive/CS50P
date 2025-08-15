def compute(m, c=300000000):
    return m * (c ^ 2)


print("E:", compute(int(input("m: "))))
