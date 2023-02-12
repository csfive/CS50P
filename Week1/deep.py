s = (
    input(
        "What is the Answer to the Great Question of Life, the Universe, and Everything? "
    )
    .strip()
    .lower()
)

if s == "42" or s == "forty two" or s == "forty-two":
    print("Yes")
else:
    print("No")
