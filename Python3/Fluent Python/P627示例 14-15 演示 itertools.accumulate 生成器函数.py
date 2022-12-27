# 表14-2：用于映射的生成器函数
# 模块 函数 说明
# itertools
#########################
# accumulate(it,
# [func])
#########################
# 产出累积的总和；如果提供了 func，那么把前两个
# 元素传给它，然后把计算结果和下一个元素传给
# 它，以此类推，最后产出结果
#########################
# （内置） enumerate(iterable,
# start=0)
#########################
# 产出由两个元素组成的元组，结构是 (index,
# item)，其中 index 从 start 开始计数，item 则从
# iterable 中获取
# （内置） map(func, it1,
# [it2, ..., itN])
# 把 it 中的各个元素传给func，产出结果；如果传入
# N 个可迭代的对象，那么 func 必须能接受 N 个参
# 数，而且要并行处理各个可迭代的对象
# itertools starmap(func, it)
# 把 it 中的各个元素传给 func，产出结果；输入的
# 可迭代对象应该产出可迭代的元素 iit，然后以
# func(*iit) 这种形式调用 func
sample = [5, 4, 2, 8, 7, 6, 3, 0, 9, 1]
import itertools
print(list(itertools.accumulate(sample)))
print(list(itertools.accumulate(sample, min)))
print(list(itertools.accumulate(sample, max)))
import operator
print(list(itertools.accumulate(sample, operator.mul)))
print(list(itertools.accumulate(range(1, 11), operator.mul)))