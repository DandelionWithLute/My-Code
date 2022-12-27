### 辅助函数，仅用于显示 ###
def cls_name(obj_or_cls):
    cls = type(obj_or_cls)
    if cls is type:
        cls = obj_or_cls
    return cls.__name__.split('.')[-1]

def display(obj):
    cls = type(obj)
    if cls is type:
        return '<class {}>'.format(obj.__name__)
    elif cls in [type(None), int]:
        return repr(obj)
    else:
        return '<{} object>'.format(cls_name(obj))

def print_args(name, *args):
    pseudo_args = ', '.join(display(x) for x in args)
    print('-> {}.__{}__({})'.format(cls_name(args[0]), name, pseudo_args))

### 对这个示例重要的类 ###

class Overriding:
    """也称数据描述符或强制描述符"""

    def __get__(self, instance, owner):
        print_args('get', self, instance, owner)

    def __set__(self, instance, value):
        print_args('set', self, instance, value)

class OverridingNoGet:
    """没有``__get__``方法的覆盖型描述符"""

    def __set__(self, instance, value):
        print_args('set', self, instance, value)

class NonOverriding:
    """没有``__get__``方法的覆盖型描述符"""

    def __get__(self, instance, owner):
        print_args('get', self, instance, owner)

class Managed:
    over = Overriding()
    over_no_get = OverridingNoGet()
    non_over = NonOverriding()

    def spam(self):
        print('-> Managed.spam({})'.format(display(self)))

obj = Managed()
print(obj.spam)
Managed.spam
obj.spam = 7
print(obj.spam)

# ❶ obj.spam 获取的是绑定方法对象。
# ❷ 但是 Managed.spam 获取的是函数。 IMPORTANT IMPORTANT IMPORTANT IMPORTANT IMPORTANT
# ❸ 如果为 obj.spam 赋值，会遮盖类属性，导致无法通过 obj 实例访
# 问 spam 方法。
