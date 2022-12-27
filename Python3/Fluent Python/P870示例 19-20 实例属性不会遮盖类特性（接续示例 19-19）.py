class Class:
    data = 'the class data attr'
    @property
    def prop(self):
        return 'the prop value'

obj = Class()
print(vars(obj))
print(obj.data)
obj.data = 'bar'
print(vars(obj))
print(obj.data)
print(Class.data)

#❷ vars 函数返回 obj 的 __dict__ 属性，表明没有实例属性。
#❻ 现在读取 obj.data，获取的是实例属性的值。从 obj 实例中读取属
#性时，实例属性 data 会遮盖类属性 data。
# ❼ Class.data 属性的值完好无损。

print(Class.prop)
print(obj.prop)
#obj.prop = 'foo'
obj.__dict__['prop'] = 'foo'
print(vars(obj))
Class.prop = 'baz'
print(obj.prop)

# ❶ obj.data 获取的是实例属性 data。
# ❷ Class.data 获取的是类属性 data。
# ❸ 使用新特性覆盖 Class.data。
# ❹ 现在，obj.data 被 Class.data 特性遮盖了。
# ❺ 删除特性。
# ❻ 现在恢复原样，obj.data 获取的是实例属性 data。
# 本节的主要观点是，obj.attr 这样的表达式不会从 obj 开始寻找
# attr，而是从 obj.__class__ 开始，而且，仅当类中没有名为 attr
# 的特性时，Python 才会在 obj 实例中寻找。这条规则不仅适用于特性，
# 还适用于一整类描述符——覆盖型描述符（overriding descriptor）。第
# 20 章会进一步讨论描述符，那时你会发现，特性其实是覆盖型描述
# 符。
# 现在回到特性。各种 Python 代码单元（模块、函数、类和方法）都可以
# 有文档字符串。下一节说明如何把文档依附到特性上。