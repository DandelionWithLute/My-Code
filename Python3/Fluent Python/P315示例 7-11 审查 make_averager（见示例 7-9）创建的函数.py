def make_averager():
    series = []
    def averager(new_value):
        series.append(new_value)
        total = sum(series)
        return total/len(series)
    return averager
avg = make_averager()
print(avg.__code__.co_freevars)
print(avg.__closure__)
print(avg.__closure__[0].cell_contents)