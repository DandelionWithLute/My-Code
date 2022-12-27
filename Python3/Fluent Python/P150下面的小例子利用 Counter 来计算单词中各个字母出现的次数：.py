import collections
ct = collections.Counter('abracadabbra')
print(ct)
ct.update('aaaaazzz')
print(ct)
print(ct.most_common(2))