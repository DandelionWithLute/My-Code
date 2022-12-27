a = [1, 2, 3]
b = a
a.append(4)
print(b)
class Gizmo:
    def __init__(self):
        print('Gizmo id: %d' % id(self))
    try:
        x = Gizmo()
        y = Gizmo() * 10
    except Exception:
        pass
print(dir())


#print('(%g,%g)' % (blank.x,blank.y))
#https://stackoverflow.com/questions/20450531/python-operator-in-print-statement
