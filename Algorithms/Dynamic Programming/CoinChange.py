#soln does not work yet
def coinChange(N,coins):
    map = {}
    for i in xrange(N+1):
        map[i] = []
        for c in coins:
            if i >= c:
                if (i-c == 0):
                    if not i in map:
                        map[i] = [[c],]
                    else:
                        map[i].append([c])
                else:
                    for l in map[i-c]:
                        k = sorted(l+[c])
                        if not k in map[i]:
                            map[i].append(k)
        print map[i]
    return len(map[N])

N = int(raw_input().split()[0])
lst = map(lambda x: int(x), raw_input().split())
print coinChange(N,lst)
#print coinChange(4,[1,2,3])
#print coinChange(10,[2,5,3,6])
