def __eq__(self, other):
    return len(self) == len(other) and (a == b for a, b in zip(self, other))