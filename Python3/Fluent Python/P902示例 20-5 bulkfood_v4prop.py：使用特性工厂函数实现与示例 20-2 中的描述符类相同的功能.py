def quantity():
    try:
        quantity.counter += 1
    except AttributeError:
        quantity.counter = 0
    storage_name = '_{}:{}'.format('quantity', quantity.counter)

    def qty_getter(instance):
        return getattr(instance, sotrage_name)

    def qty_setter(instance, value):
        if value > 0:
            setattr(instance, storage_name, value)
        else:
            raise ValueError('value must be > 0')

    return property(qty_getter, qty_getter)

# ❶ 没有 storage_name 参数。
# ❷ 不能依靠类属性在多次调用之间共享 counter，因此把它定义
# 为 quantity 函数自身的属性。
# ❸ 如果 quantity.counter 属性未定义，把值设为 0。
# ❹ 我们也没有实例变量，因此创建一个局部变量 storage_name，
# 借助闭包保持它的值，供后面的 qty_getter 和 qty_setter 函数
# 使用。
# ❺ 余下的代码与示例 19-24 一样，不过这里可以使用内置的
# getattr 和 setattr 函数，而不用处理 instance.__dict__ 属
# 性。
