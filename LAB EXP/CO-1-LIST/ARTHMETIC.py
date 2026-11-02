from itertools import permutations

letters = "SENDMORY"
digits = "0123456789"

def solve_cryptarithm():
    for p in permutations(digits, len(letters)):
        d = dict(zip(letters, p))

        if d["S"] == "0" or d["M"] == "0":
            continue

        send = int("".join(d[x] for x in "SEND"))
        more = int("".join(d[x] for x in "MORE"))
        money = int("".join(d[x] for x in "MONEY"))

        if send + more == money:
            return send, more, money, d

result = solve_cryptarithm()

if result:
    send, more, money, mapping = result
    print("Crypt-Arithmetic Solution")
    print("SEND =", send)
    print("MORE =", more)
    print("MONEY =", money)
    print(send, "+", more, "=", money)
else:
    print("No solution found.")
