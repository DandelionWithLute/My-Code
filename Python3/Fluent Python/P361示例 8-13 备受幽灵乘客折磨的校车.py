class HauntedBus:
    """备受幽灵乘客折磨的校车"""
    def __init__(self, passengers=[]):
        self.passengers = passengers
    def pick(self, name):
        self.passengers.append(name)
    def drop(self, name):
        self.passengers.remove(name)

bus1 = HauntedBus(['Alice', 'Bill'])
print(bus1.passengers)
bus1.pick('Charlie')
bus1.drop('Alice')
print(bus1.passengers)
#Take care of the indentation! Don't let def share the same height with class.
bus2 = HauntedBus()
bus2.pick('Carrie')
print(bus2.passengers)
bus3 = HauntedBus()
print(bus3.passengers)
bus3.pick('Dave')
print(bus2.passengers)
print(bus2.passengers is bus3.passengers)
print(bus1.passengers)
# ❶ 目前没什么问题，bus1 没有出现异常。
# ❷ 一开始，bus2 是空的，因此把默认的空列表赋值给
# self.passengers。
# ❸ bus3 一开始也是空的，因此还是赋值默认的列表。
# ❹ 但是默认列表不为空！
# ❺ 登上 bus3 的 Dave 出现在 bus2 中。
# ❻ 问题是，bus2.passengers 和 bus3.passengers 指代同一个列
# 表。
# ❼ 但 bus1.passengers 是不同的列表。
# 问题在于，没有指定初始乘客的 HauntedBus 实例会共享同一个乘客列
# 表。
print(dir(HauntedBus.__init__))#doctest: +ELLIPSIS
print(HauntedBus.__init__.__defaults__)