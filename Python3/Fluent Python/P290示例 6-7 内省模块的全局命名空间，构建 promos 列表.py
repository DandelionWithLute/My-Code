promos = [globals()[name] for name in globals()
            if name.endswith('_promo')
            and name != 'best_promo']

def best_promo(order):
    '''选择可用的最佳折扣
    '''
    return max(promo(order) for promo in promos)