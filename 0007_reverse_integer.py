def reverse(x):
    y = 0        
    if x < 0:
        x *= -1
        negative = True
    else:
        negative = False
    while x > 0:
        y *= 10
        y += x % 10
        x //= 10
    if negative:
        y *= -1
    if y > 2**31 - 1 or y < -2**31:
        y = 0        
    return y
