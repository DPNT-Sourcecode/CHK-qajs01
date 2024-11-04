

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    sku_set = {"A", "B", "C", "D"}
    if !sku_set.issuperset(skus):
        return -1
    checkout_value = skus.count('A') * 50 - skus.count('A') // 3 * 20 \
        + skus.count('B') * 30 - skus.count('B') // 2 * 15 \
        + skus.count('C') * 20 \
        + skus.count('D') * 15
    return checkout_value

