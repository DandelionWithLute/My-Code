>>> import numpy ➊
>>> a = numpy.arange(12) ➋
>>> a
array([ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
>>> type(a)
<class 'numpy.ndarray'>
>>> a.shape ➌
(12,)
>>> a.shape = 3, 4 ➍
>>> a
array([[ 0, 1, 2, 3],
[ 4, 5, 6, 7],
[ 8, 9, 10, 11]])
>>> a[2] ➎
array([ 8, 9, 10, 11])
>>> a[2, 1] ➏
9
>>> a[:, 1] ➐
array([1, 5, 9])
>>> a.transpose() ➑
array([[ 0, 4, 8],
[ 1, 5, 9],
[ 2, 6, 10],
[ 3, 7, 11]])
