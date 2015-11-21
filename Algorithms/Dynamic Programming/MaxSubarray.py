#using Kadane method
#keep track of current and max sums

#get max for contiguous
def kadane(lst):
    maxSum = 0
    curSum = 0   
    smallestNeg = None
    for i in lst:
        if (curSum + i > 0):
            curSum = curSum + i
            if (curSum > maxSum):
                maxSum = curSum
        else:
            curSum = 0
            if (smallestNeg == None):
                smallestNeg = i
            elif (smallestNeg < i):
                smallestNeg = i
    return maxSum if maxSum > 0 else smallestNeg

# max for noncontiguous
def sortedmax(lst):
    return kadane(sorted(lst))
T = input()
for _ in xrange(T):
    N = input()
    lst = map(lambda x: int(x),raw_input().split(" "))
    print kadane(lst), sortedmax(lst)

#print kadane([1,2,3,4])
#print kadane([2,-1,2,3,4,-5])
#print kadane([10,1,-11,1,2,3,4])
#print kadane([])
#print kadane([-1,-2,-3,-4])
