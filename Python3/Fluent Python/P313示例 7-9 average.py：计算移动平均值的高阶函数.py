def make_averager():
    series = []

    def averager(new_value):
        series.append(new_value)
        total = sum(series)
        return total/len(series)

    return averager

avg = make_averager()
print(avg(1))
print(avg(2))
print(avg(3))
print(avg(4))
print(avg(5))

