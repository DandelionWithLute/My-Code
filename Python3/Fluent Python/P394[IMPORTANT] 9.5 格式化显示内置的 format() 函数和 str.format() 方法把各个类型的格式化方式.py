brl = 1/2.43 # BRL到USD的货币兑换比价
print(brl)
print(format(brl, '0.4f'))
print('1 BRL = {rate:0.2f} USD'.format(rate=brl))
# 格式规范微语言为一些内置类型提供了专用的表示代码。比如，b 和 x
# 分别表示二进制和十六进制的 int 类型，f 表示小数形式的 float 类
# 型，而 % 表示百分数形式：
print(format(42, 'b'))
print(format(2/3, '.1%'))