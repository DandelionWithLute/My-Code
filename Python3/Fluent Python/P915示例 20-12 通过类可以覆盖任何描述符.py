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
Managed.over = 1
Managed.over_no_get = 2
Managed.non_over = 3
print(obj.over, obj.over_no_get, obj.non_over)