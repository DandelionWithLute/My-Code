print(open('cafe.txt', 'w', encoding='utf-8').write('café'))
print(open('cafe.txt').read())
# 问题是：写入文件时指定了 UTF-8 编码，但是读取文件时没有这么做，
# 因此 Python 假定要使用系统默认的编码（Windows 1252），于是文件的
# 最后一个字节解码成了字符 'Ã©'，而不是 'é'。

# 我是在 Windows 7 中运行示例 4-9 的。在新版 GNU/Linux 或 Mac OS X
# 中运行同样的语句不会出问题，因为这几个操作系统的默认编码是
# UTF-8，让人误以为一切正常。如果打开文件是为了写入，但是没有指
# 定编码参数，会使用区域设置中的默认编码，而且使用那个编码也能正
# 确读取文件。但是，如果脚本要生成文件，而字节的内容取决于平台或
# 同一平台中的区域设置，那么就可能导致兼容问题。


#Unicode Sandwich

# byte -> str
# 100%str
# str -> byte