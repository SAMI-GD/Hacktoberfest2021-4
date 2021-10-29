a, b, c, d = input().split()
# changing to integer
P = int(a)
Q = int(b)
N = int(c)
M = int(d)

S = 0
if (1 <= P <= 1000) and (0 <= Q <= 1000) and (N >= 1) and (M <= 1000000000):
    for i in range(1, N + 1):
        G = (P ** i) * (i ** Q)
        S = S + G

print(S % M)
