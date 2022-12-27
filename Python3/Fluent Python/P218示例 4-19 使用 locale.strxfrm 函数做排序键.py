import locale
print(locale.setlocale(locale.LC_COLLATE, 'pt_BR.UTF-8'))
fruit = ['caju', 'atemonia', 'caja', 'acai', 'acerola']
sorted_fruits = sorted(fruit, key=locale.strxfrm)
print(sorted_fruits)
