def minimize_cash_flow(transactions):
    balance = {}

    for giver, receiver, amount in transactions:
        balance[giver] = balance.get(giver, 0) - amount
        balance[receiver] = balance.get(receiver, 0) + amount

    debtors = []
    creditors = []

    for person, amt in balance.items():
        if amt < 0:
            debtors.append([person, -amt])
        elif amt > 0:
            creditors.append([person, amt])

    debtors.sort(key=lambda x: (-x[1], x[0]))
    creditors.sort(key=lambda x: (-x[1], x[0]))

    i, j = 0, 0
    result = []

    while i < len(debtors) and j < len(creditors):
        settle = min(debtors[i][1], creditors[j][1])

        result.append(f"{debtors[i][0]} pays {creditors[j][0]} ₹{settle}")

        debtors[i][1] -= settle
        creditors[j][1] -= settle

        if debtors[i][1] == 0:
            i += 1
        if creditors[j][1] == 0:
            j += 1

    return result


# ---------------- MAIN ----------------

if __name__ == "__main__":

    print("\n=== Expense Splitter ===")
    print("Enter transactions in this format:")
    print("Giver Receiver Amount")
    print("Example: A B 100  → means A gives ₹100 to B\n")

    # number of transactions
    while True:
        try:
            n = int(input("Enter number of transactions: "))
            if n <= 0:
                print("Number must be greater than 0.\n")
                continue
            break
        except:
            print("Please enter a valid integer.\n")

    transactions = []

    # input loop
    for i in range(n):
        while True:
            entry = input(f"Transaction {i+1}: ").strip().split()

            if len(entry) != 3:
                print("❌ Format: Name1 Name2 Amount (example: A B 100)\n")
                continue

            giver, receiver, amount = entry

            # validate names
            if not giver.isalpha() or not receiver.isalpha():
                print("❌ Names must contain only letters.\n")
                continue

            # validate amount
            try:
                amount = int(amount)
                if amount <= 0:
                    print("❌ Amount must be positive.\n")
                    continue
            except:
                print("❌ Amount must be a number.\n")
                continue

            transactions.append((giver, receiver, amount))
            break

    # debug print (so user sees what was entered)
    print("\nYou entered:")
    for t in transactions:
        print(f"{t[0]} gives ₹{t[2]} to {t[1]}")

    result = minimize_cash_flow(transactions)

    print("\nOptimized Transactions:")
    for r in result:
        print(r)