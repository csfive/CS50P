list = {}
while True:
    try:
        item = input("").upper()
    except EOFError:
        print()
        break

    if item in list:
        list[item] += 1
    else:
        list[item] = 1

for item, cnt in sorted(list.items()):
    print(f"{cnt} {item}")
