N = int(input("N: "))
M = int(input("M: "))
for m in range (0, N):
    if m % 2 == 0:
        for i in range(0, M ):
            print(f"MOVE to {m},{i}")
    else:
        for i in range(M-1, -1, -1):
            print(f"MOVE to {m},{i}")    