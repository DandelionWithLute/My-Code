import array
numbers = array.array('h', [-2, -1, 0, 1, 2])
memv = memoryview(numbers)
print(len(memv))
print(memv[0])
memv_oct = memv.cast('B')
print(memv_oct.tolist())

memv_oct[5] = 4
print(numbers)
# ❶ 利用含有 5 个短整型有符号整数的数组（类型码是 'h'）创建一个memoryview。
# ❷ memv 里的 5 个元素跟数组里的没有区别。
# ❸ 创建一个 memv_oct，这一次是把 memv 里的内容转换成 'B' 类型，
# 也就是无符号字符。
# ❹ 以列表的形式查看 memv_oct 的内容。
# ❺ 把位于位置 5 的字节赋值成 4。
# ❻ 因为我们把占 2 个字节的整数的高位字节改成了 4，所以这个有符号
# 整数的值就变成了 1024。