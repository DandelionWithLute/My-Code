class LineItem:
    def __init__(self, description, weight, price):
        self.description = description
        self.weigh = weight
        self.price = price

    def subtotal(self):
        return self.weigh * self.price

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, value):
        if value > 0:
            self.__weight = value
        else:
            raise ValueError('value must be > 0')
walnuts = LineItem('walnuts', 0, 10.00)
print(walnuts)

# 注意，现在不能创建重量为无效值的 LineItem 对象：
# >>> walnuts = LineItem('walnuts', 0, 10.00)
# Traceback (most recent call last):
# ...
# ValueError: value must be > 0
# 现在，我们禁止用户为 weight 属性提供负值或零。虽然买家通常不能
# 设置商品的价格，但是工作人员可能犯错，应用程序也可能有缺陷，从
# 而导致 LineItem 对象的 price 属性为负值。为了防止出现这种情况，
# 我们也可以把 price 属性变成特性，但是这样我们的代码中就存在一
# 些重复。
# 还记得第 14 章引述 Paul Graham 的那句话吗？他说：“当我在自己的程
# 序中发现用到了模式，我觉得这就表明某个地方出错了。”去除重复的
# 方法是抽象。抽象特性的定义有两种方式：使用特性工厂函数，或者使
# 用描述符类。后者更灵活，第 20 章会全面讨论。其实，特性本身就是
# 使用描述符类实现的。不过，这里我们要继续探讨特性，实现一个特性
# 工厂函数。
# 但是，在实现特性工厂函数之前，我们要深入理解特性