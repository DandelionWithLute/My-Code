# 弱引用不会增加对象的引用数量。引用的目标对象称为所指对象
# （referent）。因此我们说，弱引用不会妨碍所指对象被当作垃圾回收。
import weakref
a_set = {0, 1}
wref = weakref.ref(a_set)
print(wref)
print(wref())
a_set = {2, 3, 4}
print(wref())
print(wref() is None)
