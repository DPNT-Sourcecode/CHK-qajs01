

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    sku_set = {'A', 'B', 'C', 'D', 'E'}
    if not sku_set.issuperset(skus):
        return -1
    checkout_value = skus.count('A') * 50 - skus.count('A') // 3 * 20 \
        + skus.count('B') * 30 - skus.count('B') // 2 * 15 \
        + skus.count('C') * 20 \
        + skus.count('D') * 15 \
        + skus.count('E') * 40 - min(skus.count('E') // 2, skus.count('B')) * 30
    return checkout_value




