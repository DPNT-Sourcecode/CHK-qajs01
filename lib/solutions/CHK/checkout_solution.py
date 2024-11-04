

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    checkout_value = skus.count('A') * 50 + skus.count('B') * 30 + skus.count('C') * 20 + skus.count('D') * 15
    return checkout_value


