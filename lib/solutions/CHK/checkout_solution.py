# Set up price list and sku set
prices = {
    'A': 50,
    'B': 30,
    'C': 20,
    'D': 15,
    'E': 40,
    'F': 10,
    'G': 20,
    'H': 10,
    'I': 35,
    'J': 60,
    'K': 70,
    'L': 90,
    'M': 15,
    'N': 40,
    'O': 10,
    'P': 50,
    'Q': 30,
    'R': 50,
    'S': 20,
    'T': 20,
    'U': 40,
    'V': 50,
    'W': 20,
    'X': 17,
    'Y': 20,
    'Z': 21
}
sku_set = set(prices.keys())

# Set up special offers
offers = [
    ("cross-bundle", 'E', 2, 'B'),
    ("cross-bundle", 'N', 3, 'M'),
    ("cross-bundle", 'R', 3, 'Q'),
    ("single-bundle", 'F', 3, 2),
    ("single-bundle", 'U', 4, 3),
    ("multi-buy", 'A', 5, 200),
    ("multi-buy", 'A', 3, 130),
    ("multi-buy", 'B', 2, 45),
    ("multi-buy", 'H', 10, 80),
    ("multi-buy", 'H', 5, 45),
    ("multi-buy", 'K', 2, 120),
    ("multi-buy", 'P', 5, 200),
    ("multi-buy", 'Q', 3, 80),
    ("multi-buy", 'V', 3, 130),
    ("multi-buy", 'V', 2, 90),
    ("group-buy", ['X', 'Y', 'T', 'S', 'Z'], 3, 45),
]

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    # Check invalid input
    if not sku_set.issuperset(skus):
        return -1

    # Get basket information
    basket = {item: skus.count(item) for item in sku_set}
    
    # Calculate special offers
    checkout_value = 0
    for offer_rule in offers:
        item = offer_rule[1]
        cond = offer_rule[2]
        promo = offer_rule[3]
        match offer_rule[0]:
            case "cross-bundle":
                basket[promo] = max(0, basket[promo] - basket[item] // cond)
            case "single-bundle":
                basket[item] = basket[item] % cond + \
                    basket[item] // cond * promo
            case "multi-buy":
                checkout_value += basket[item] // cond * promo
                basket[item] = basket[item] % cond
            case "group-buy":
                cnt = sum([basket[i] for i in item])
                checkout_value += cnt // cond * promo
                remaining = cnt % cond
                for i in item:
                    tmp = basket[i]
                    basket[i] = min(basket[i], remaining)
                    remaining = max(0, remaining - tmp)

    # Calculate checkout value
    for item in basket:
        checkout_value += basket[item] * prices[item]
    return checkout_value







