def __eq__(self, other):
    if len(self) != len(other):
        return False
    for a,b in zip(self, other):
        if a != b:
            return False
    return True