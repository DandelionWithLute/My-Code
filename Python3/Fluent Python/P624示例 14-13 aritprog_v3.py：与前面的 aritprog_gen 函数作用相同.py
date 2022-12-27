import itertools

def aritprog_gen(begin, step, end=None):
    first = type(begin + step)(begin)
    ap_gen = itertools.count(first, step)
    if end is not None:
        ap_gen = itertools.takewhile(lambda n : n < end, ap_gen)
    return ap_gen

# 注意，示例 14-13 中的 aritprog_gen 不是生成器函数，因为定义体中
# 没有 yield 关键字。但是它会返回一个生成器，因此它与其他生成器
# 函数一样，也是生成器工厂函数。
# 示例 14-13 想表达的观点是，实现生成器时要知道标准库中有什么可
# 用，否则很可能会重新发明轮子。鉴于此，下一节会介绍一些现成的生
# 成器函数。