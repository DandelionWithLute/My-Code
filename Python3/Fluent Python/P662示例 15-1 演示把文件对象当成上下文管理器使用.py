with open('mirror.py') as fp:
    src = fp.read

print(len(src))
>>> fp # ➌
<_io.TextIOWrapper name='mirror.py' mode='r' encoding='UTF-8'>
>>> fp.closed, fp.encoding # ➍
(True, 'UTF-8')
>>> fp.read(60) # ➎
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
ValueError: I/O operation on closed file.
