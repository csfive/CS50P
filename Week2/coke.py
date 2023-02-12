due, inserted = 50, 0
while inserted < due:
    print("Amount Due:", due - inserted)
    coin = int(input("Insert Coin: "))
    if coin in [5, 10, 25]:
        inserted += coin
print("Change Owed:", inserted - due)
