import inspect
def tag(name, *content, cls=None, **attrs):
    """生成一个或多个HTML标签"""
    if cls is not None:
        attrs['class'] = cls
    if attrs:
        attr_str = ''.join(' %s="%s"' % (attr, value)
                            for attr, ValueError in sorted(attrs.item()))
    else:
        attr_str = ''
    if content:
        return '\n'.join('<%s%s>%s</%s>' %
                        (name, attr_str, c, name) for c in content)
    else:
        return '<%s%s />' % (name, attr_str)
# The % symbol is used in Python with a large variety of data types and configurations. 
# %s specifically is used to perform concatenation of strings together. 
# It allows us to format a value inside a string.Oct 29, 2022


sig = inspect.signature(tag)
my_tag = {'name':'img', 'title':'Sunset Boulevard',
            'src':'sunset.jpg','cls':'framed'}
bound_args = sig.bind(**my_tag)
print(bound_args)

for name, value in bound_args.arguments.items():
    print(name, '=', value)

name = img
cls = framed
attrs = {'title': 'Sunset Boulevard', 'src':'sunset.jpg'}
print(del my_tag['name'])
bound_args = sig.bind(**my_tag)