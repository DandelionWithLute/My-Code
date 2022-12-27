x = 'ABC'
dummy = [ord(x) for x in 'ABC']
print(x)
print(dummy)

#➊ x 的值被保留了。
#➋ 列表推导也创建了正确的列表。

#Python 2.7.6 (default, Mar 22 2014, 22:59:38)
#[GCC 4.8.2] on linux2
#Type "help", "copyright", "credits" or "license" for more information.
#>>> x = 'my precious'
#>>> dummy = [x for x in 'ABC']
#>>> x
#'C'
#如你所见，x 原本的值被取代了，但是这种情况在 Python 3 中是不
#会出现的。

#这是Python 3 代码：
#>>> x = 'ABC'
#>>> dummy = [ord(x) for x in x]
#>>> x ➊
#'ABC'
#>>> dummy ➋
#[65, 66, 67]
#>>>
#➊ x 的值被保留了。
#➋ 列表推导也创建了正确的列表。
#列表推导可以帮助我们把一个序列或是其他可迭代类型中的元素过滤或
#是加工，然后再新建一个列表。Python 内置的 filter 和 map 函数组合
#起来也能达到这一效果，但是可读性上打了不小的折扣。