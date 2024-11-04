

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    sku_set = {'A', 'B', 'C', 'D', 'E'}
    if not sku_set.issuperset(skus):
        return -1

    basket = {item: skus.count(item) for item in sku_set}
    prices = {
        'A': 50,
        'B': 30,
        'C': 20,
        'D': 15,
        'E': 40
    }
    checkout_value = 0

    checkout_value += basket['A'] // 5 * 200
    basket['A'] = basket['A'] // 5

    for item in basket:
        checkout_value += basket[item] * prices[item]
    return checkout_value

