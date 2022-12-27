from unicodedata import normalize, name
half = '½'
#print('NFKC', half)
four_squared = '4²'
print(normalize('NFKC', four_squared))
micro = ''
micro = 'μ'
micro_kc = normalize('NFKC', micro)
print(micro, micro_kc)
print(ord(micro), ord(micro_kc))
print(name(micro), name(micro_kc))
