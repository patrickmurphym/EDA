def resta(a,b):
    if (b == 0):
        return a
    if (b < 0):
        return resta(a+1,b+1)
    if (b > 0):
        return resta(a-1,b-1)

def mult(a,b):
    if (b==0):
        return 0
    x=a + mult(a,b-1)
    return x


def mod(a,b):
    if (a < b):
        return a
    x = mod(a-b,b)
    return x
