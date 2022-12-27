from unicodedata import normalize
s1 = 'café' # 把"e"和重音符组合在一起
s2 = 'cafe\u0301'    # 分解成"e"和重音符
print(len(s1), len(s2))
print(len(normalize('NFC', s1)), len(normalize('NFC', s2)))
print(normalize('NFC', s1) == normalize('NFC', s2))
print(normalize('NFD', s1) == normalize('NFD', s2))