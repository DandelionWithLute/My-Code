def entity(cls):
    for key, attr in cls.__dict__.items():
        if isinstance(attr, Validated):
            type_name = type(attr).__name__
            attr.storage_name = '_{}#{}'.format(type_name, key)
    return cls

@entity
class LineItem:
    description = entity.NonBlank()
    weight = entity.Quantity()
    price = entity.Quantity()

    def __init__(self) -> None:
        self.description = description
        self.weight = weight
        self.price = price

    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price
    def subtotal(self):
        return self.weight * self.price


# >>> raisins = LineItem('Golden raisins', 10, 6.95)
# >>> dir(raisins)[:3]
# ['_NonBlank#description', '_Quantity#price', '_Quantity#weight']
# >>> LineItem.description.storage_name
# '_NonBlank#description'
# >>> raisins.description
# 'Golden raisins'
# >>> getattr(raisins, '_NonBlank#description')
# 'Golden raisins'
