from dis import dis
def f1(a):
    print(a)
    print(b)
def f2(a):
    print(a)
    print(b)
    b = 9

print(dis(f2))