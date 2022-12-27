因为 Unicode 有组合字符（变音符号和附加到前一个字符上的记号，打
印时作为一个整体），所以字符串比较起来很复杂。
例如，“café”这个词可以使用两种方式构成，分别有 4 个和 5 个码位，
但是结果完全一样：
>>> s1 = 'café'
>>> s2 = 'cafe\u0301'
>>> s1, s2
('café', 'café')
>>> len(s1), len(s2)
(4, 5)
>>> s1 == s2
False
U+0301 是 COMBINING ACUTE ACCENT，加在“e”后面得到“é”。在
Unicode 标准中，'é' 和 'e\u0301' 这样的序列叫“标准等价
物”（canonical equivalent），应用程序应该把它们视作相同的字符。但
是，Python 看到的是不同的码位序列，因此判定二者不相等。
这个问题的解决方案是使用 unicodedata.normalize 函数提供的
Unicode 规范化。这个函数的第一个参数是这 4 个字符串中的一
个：'NFC'、'NFD'、'NFKC' 和 'NFKD'。下面先说明前两个。
NFC（Normalization Form C）使用最少的码位构成等价的字符串，而
NFD 把组合字符分解成基字符和单独的组合字符。这两种规范化方式都
能让比较行为符合预期：
>>> from unicodedata import normalize
>>> s1 = 'café' # 把"e"和重音符组合在一起
>>> s2 = 'cafe\u0301' # 分解成"e"和重音符
>>> len(s1), len(s2)
(4, 5)
>>> len(normalize('NFC', s1)), len(normalize('NFC', s2))
(4, 4)
>>> len(normalize('NFD', s1)), len(normalize('NFD', s2))
(5, 5)
>>> normalize('NFC', s1) == normalize('NFC', s2)
True
>>> normalize('NFD', s1) == normalize('NFD', s2)
True
西方键盘通常能输出组合字符，因此用户输入的文本默认是 NFC 形
式。不过，安全起见，保存文本之前，最好使用 normalize('NFC',
user_text) 清洗字符串。NFC 也是 W3C 的“Character Model for the
World Wide Web: String Matching and Searching”规范
（https://www.w3.org/TR/charmod-norm/）推荐的规范化形式。
使用 NFC 时，有些单字符会被规范成另一个单字符。例如，电阻的单
位欧姆（Ω）会被规范成希腊字母大写的欧米加。这两个字符在视觉上
是一样的，但是比较时并不相等，因此要规范化，防止出现意外：
>>> from unicodedata import normalize, name
>>> ohm = '\u2126'
>>> name(ohm)
'OHM SIGN'
>>> ohm_c = normalize('NFC', ohm)
>>> name(ohm_c)
'GREEK CAPITAL LETTER OMEGA'
>>> ohm == ohm_c
False
>>> normalize('NFC', ohm) == normalize('NFC', ohm_c)
True
在另外两个规范化形式（NFKC 和 NFKD）的首字母缩略词中，字母 K
表示“compatibility”（兼容性）。这两种是较严格的规范化形式，对“兼
容字符”有影响。虽然 Unicode 的目标是为各个字符提供“规范的”码位，
但是为了兼容现有的标准，有些字符会出现多次。例如，虽然希腊字母
表中有“μ”这个字母（码位是 U+03BC，GREEK SMALL LETTER MU），
但是 Unicode 还是加入了微符号 'µ'（U+00B5），以便与 latin1 相互
转换。因此，微符号是一个“兼容字符”。
在 NFKC 和 NFKD 形式中，各个兼容字符会被替换成一个或多个“兼容
分解”字符，即便这样有些格式损失，但仍是“首选”表述——理想情况
下，格式化是外部标记的职责，不应该由 Unicode 处理。下面举个例
子。二分之一 '½'（U+00BD）经过兼容分解后得到的是三个字符序列
'1/2'；微符号 'µ'（U+00B5）经过兼容分解后得到的是小写字母
'μ'（U+03BC）。
微符号是“兼容字符”，而欧姆符号不是，这还真是奇怪。因此，NFC 不会改动微符号，但是
会把欧姆符号改成大写的欧米加；而 NFKC 和 NFKD 会把欧姆和微符号都改成其他字符。
下面是 NFKC 的具体应用：
>>> from unicodedata import normalize, name
>>> half = '½'
>>> normalize('NFKC', half)
'1⁄2'
>>> four_squared = '4²'
>>> normalize('NFKC', four_squared)
'42'
>>> micro = 'μ'
>>> micro_kc = normalize('NFKC', micro)
>>> micro, micro_kc
('μ', 'μ')
>>> ord(micro), ord(micro_kc)
(181, 956)
>>> name(micro), name(micro_kc)
('MICRO SIGN', 'GREEK SMALL LETTER MU')
使用 '1/2' 替代 '½' 可以接受，微符号也确实是小写的希腊字母
'µ'，但是把 '4²' 转换成 '42' 就改变原意了。某些应用程序可以把
'4²' 保存为 '4<sup>2</sup>'，但是 normalize 函数对格式一无所
知。因此，NFKC 或 NFKD 可能会损失或曲解信息，但是可以为搜索和
索引提供便利的中间表述：用户搜索 '1 / 2 inch' 时，如果还能找到
包含 '½ inch' 的文档，那么用户会感到满意。
使用 NFKC 和 NFKD 规范化形式时要小心，而且只能在特
殊情况中使用，例如搜索和索引，而不能用于持久存储，因为这两
种转换会导致数据损失。
为搜索或索引准备文本时，还有一个有用的操作，即下一节讨论的大小
写折叠。
