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