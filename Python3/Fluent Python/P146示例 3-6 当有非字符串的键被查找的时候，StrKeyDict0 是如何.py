Tests for item retrieval using `d[key]` notation::
d = StrKeyDict0([('2', 'two'), ('4', 'four')])
    print(d['2'])
#'two'
    print(d[4])
#'four'
    print(d[1])
#Traceback (most recent call last):
#...
KeyError: '1'
Tests for item retrieval using `d.get(key)` notation::
    print(d.get('2'))
#'two'
    print(d.get(4))
#'four'
    print(d.get(1, 'N/A'))
#'N/A'
Tests for the `in` operator::
    print(2 in d)
#True
    print(1 in d)
#False
