# 使用Unicode排序算法排序
# James Tauber，一位高产的 Django 贡献者，他一定是感受到了这一痛
# 点，因此开发了 PyUCA 库（https://pypi.python.org/pypi/pyuca/），这是
# Unicode 排序算法（Unicode Collation Algorithm，UCA）的纯 Python 实
# 现。示例 4-20 展示了它的简单用法。


import pyuca
coll = pyuca.Collator()
fruits = ['caju', 'atemoia', 'caja', 'acai', 'acerola']
sorted_fruits = sorted(fruits, key=coll.sort_key)
print(sorted_fruits)