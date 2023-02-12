s = (
    input(
        "What is the Answer to the Great Question of Life, the Universe, and Everything? "
    )
    .strip()
    .lower()
)

if s in ["42", "forty two", "forty-two"]:
    print("Yes")
else:
    print("No")
