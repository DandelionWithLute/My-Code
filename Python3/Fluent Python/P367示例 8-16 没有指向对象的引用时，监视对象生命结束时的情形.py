import weakref
s1 = {1, 2, 3}
s2 = s1
def bye():
    print('Gone     with the wind...')

ender = weakref.finalize(s1, bye)
print(ender.alive)

del s1
print(ender.alive)

print(s2 == 'spam')

print(ender.alive)

# 为了演示对象生命结束时的情形，示例 8-16 使用 weakref.finalize
# 注册一个回调函数，在销毁对象时调用。


# ❶ s1 和 s2 是别名，指向同一个集合，{1, 2, 3}。
# ❷ 这个函数一定不能是要销毁的对象的绑定方法，否则会有一个指向
# 对象的引用。
###
# ❸ 在 s1 引用的对象上注册 bye 回调。
###
# ❹ 调用 finalize 对象之前，.alive 属性的值为 True。
###
# ❺ 如前所述，del 不删除对象，而是删除对象的引用。
###
# ❻ 重新绑定最后一个引用 s2，让 {1, 2, 3} 无法获取。对象被销毁
# 了，调用了 bye 回调，ender.alive 的值变成了 False。

