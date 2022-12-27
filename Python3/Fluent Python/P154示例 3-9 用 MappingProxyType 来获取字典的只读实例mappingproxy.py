from types import MappingProxyType
d = {1:'A'}
d_proxy = MappingProxyType(d)
print(d_proxy)#New Verion Now,it's {1:'A'} but not MappingProxy({1:'A'})
print(d_proxy[1])