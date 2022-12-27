def pw(a, pow):
    pow = pow + 1
    result = 1
    while pow > 1:
        pow = pow - 1
        result = result * a
    return result
print(pw(5, 2))