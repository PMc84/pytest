SEQUENCE = int(input("How many sequence entries would you like? "))

N1, N2 = 0, 1
COUNT = 0

if SEQUENCE <= 0:
    print("Must be greater than 0")
elif SEQUENCE == 1:
    print(" sequence upto",SEQUENCE,":")
    print(N1)
else:
    print("Sequence:")
    while COUNT < SEQUENCE:
        print(N1)
        NTH = N1 + N2
        N1 = N2
        N2 = NTH
        COUNT += 1
