SEQUENCE = int(input("How many sequence entries would you like? "))

N1, N2 = 0, 1
COUNT = 0

print("Sequence:")
while COUNT < SEQUENCE:
    print(N1)
    NTH = N1 + N2
    N1 = N2
    N2 = NTH
    COUNT += 1
