# 0, 1
# Tn + Tn+1**2 = Tn+2
# A + B**2

def modfib(A,B,n,c=2):
    if (c == n):
        return B
    return modfib(B,A+B**2, n, c+1)

A,B,n = map(lambda x: int(x),raw_input().split(" "))
print modfib(A,B,n)
