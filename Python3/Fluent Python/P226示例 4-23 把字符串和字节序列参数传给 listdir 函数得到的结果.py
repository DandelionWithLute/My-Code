import os
print(os.listdir('.'))
#['abc.txt', 'digits-of-π.txt']

print(os.listdir(b'.'))
#[b'abc.txt', b'digits-of-\xcf\x80.txt']
