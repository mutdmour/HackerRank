#soln is bad
def candies(lst, c = None, i=0):
    if c==None:
        c = [1]*len(lst)
    if (i >= len(lst)):
        return c
        #return sum(lst)
    if (i >= 0):
        #print "yo", i
        if (i+1 < len(lst)):
            if (lst[i] > lst[i+1] and c[i] <= c[i+1]):
                #print "hey"
                if (i > 0 and c[i+1] <= c[i-1]):
                    c[i] = min(c[i-1],c[i+1]) + 1
                    print "lol"
                    if (lst[i] < lst[i-1] and not (c[i] < c[i-1])):
                        #print "damn",c
                        return candies(lst,c, i-1)
                else:
                    #print "more", i
                    c[i] = c[i+1] + 1
                    #if (lst[i] < lst[i-1] and c[i] >= c[i-1]):
                        #return candies(lst,c, i-1)
            elif (lst[i] > lst[i-1] and i > 0):
                #print "so"
                c[i] = c[i-1] + 1
        elif (i+1 == len(lst)):
            if (lst[i] > lst[i-1]): #and c[i] <= c[i-1]
                c[i] = c[i-1] + 1
    #print "k"
    return candies(lst,c,i+1)
        
if __name__ == '__main__':
    assert(candies([])==[])
    assert(candies([1])==[1])
    assert(candies([1,1])==[1,1])
    assert(candies([1,2])==[1,2])
    assert(candies([2,1])==[2,1])
    assert(candies([2,2])==[1,1])
    assert(candies([1,1,2])==[1,1,2])
    assert(candies([1,2,1])==[1,2,1])
    assert(candies([2,1,1])==[2,1,1])
    assert(candies([1,2,2])==[1,2,1])
    assert(candies([2,2,1])==[1,2,1])
    assert(candies([2,1,2])==[2,1,2])
    assert(candies([2,2,2])==[1,1,1])
    assert(candies([4,3,2])==[3,2,1])
    assert(candies([2,3,4])==[1,2,3])
    assert(candies([2,3,4,5])==[1,2,3,4])
    assert(candies([2,3,1,4,5])==[1,2,1,2,3])
    assert(candies([2,5,3,1,4,5])==[1,3,2,1,2,3])
    print (candies([2,5,3,1,4,5,3,4]))
    assert(candies([2,5,3,1,4,5,3,4])==[1,3,2,1,2,3,1,2])
