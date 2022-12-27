from random import randint
def d6():
    return randint(1, 6)
d6_iter = iter(d6, 1)
print(randint(1,4))
print(d6_iter)
for roll in d6_iter:
    print(roll)
print('///')
print(iter(5,1))
# Traceback (most recent call last):
#   File "c:\Users\123\Desktop\Code\Python3\Fluent Python\P643�������iter����.py", line 10, in <module>
#     print(iter(5,1))
# TypeError: iter(v, w): v must be callable