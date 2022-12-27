promos = [fidelity_promo, bulk_item_promo, large_order_promo]
def best_promo(order):
    '''选择可用的最佳折扣
    '''
    return max(promo(order) for promo in promos)