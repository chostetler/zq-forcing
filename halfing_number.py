import math
def halfing_number(n):
    """
    halfing_number refers to the number of tokens spent in a caterpillar graph when n=2 and the ends
    are colored to color all the center vertices
    """
    if n<=2:
        return 0
    #we remove one vertex(center) and take the lower half. 
    next = n - 1 - math.floor((n-1)/2)
    return 1 + halfing_number(next)


print([(f(x)) for x in range(1, 100)])