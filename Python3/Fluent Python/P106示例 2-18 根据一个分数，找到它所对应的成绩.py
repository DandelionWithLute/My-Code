import bisect
import sys
def grade(score, breakpoints = [60, 70, 80, 90], grades = 'FDCBA'):
    i = bisect.bisect(breakpoints, score)
    return grades[i]

print([grade(score) for score in [33, 99, 77, 70, 89, 90, 100]])




#Return the index where to insert item x in list a, assuming a is sorted.

#The return value i is such that all e in a[:i] have e <= x, and all e in
#a[i:] have e > x. So if x already appears in the list,
#  a.insert(i, x) will insert just after the rightmost x already there.
#Optional args lo (default 0) and
#  hi (default len(a)) bound the slice of a to be searched.