import math
def answer(n):
    # p = int(float(n)
    p = int(n)
    s = 0

    # z = round(math.log(p, 2), 0)
    # s = int(abs(p - 2**z) + z)
  
    while p != 1:
        if p & 1 == 0:
            z = math.log(p, 2)
            if z % 1 == 0:
                s += z - 1
                p = 1
            else:
                p = p / 2
        elif p == 3:
            p -= 1
        elif ((p - 1) & (p - 2)) < (p & (p + 1)):
            p -= 1
        else:
            p += 1
        s += 1
 
    return int(s)