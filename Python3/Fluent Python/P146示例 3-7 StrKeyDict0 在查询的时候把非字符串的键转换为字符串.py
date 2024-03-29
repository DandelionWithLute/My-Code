class StrKeyDict0(dict):
    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str[key]]
    
    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default

    def __contains__(self, __o: object, key) -> bool:
        return key in self.keys() or str(key) in self.keys()


# print(StrKeyDict0(gdfdas))FAILED
# print(StrKeyDict0(123))FAILED
# print(StrKeyDict0('happy'))FAILED