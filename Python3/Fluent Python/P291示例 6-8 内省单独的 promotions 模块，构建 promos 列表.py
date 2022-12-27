promos = [func for name, func in
                inspect.getmembers(promotions, inspect.isfunction)]

def best_promo(order):
    '''选择可用的最佳折扣
    '''
    return max(promo(order) for promo in promos)
