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
    'K': 80,
    'L': 90,
    'M': 15,
    'N': 40,
    'O': 10,
    'P': 50,
    'Q': 30,
    'R': 50,
    'S': 30,
    'T': 20,
    'U': 40,
    'V': 50,
    'W': 20,
    'X': 90,
    'Y': 10,
    'Z': 50
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
    ("multi-buy", 'H', 10, 80),
    ("multi-buy", 'H', 5, 45),
    ("multi-buy", 'K', 2, 150),
    ("multi-buy", 'P', 5, 200),
    ("multi-buy", 'Q', 3, 80),
    ("multi-buy", 'V', 3, 130),
    ("multi-buy", 'V', 2, 90),
]

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    # Check invalid input
    if not sku_set.issuperset(skus):
        return -1

    # Get basket information
    basket = {item: skus.count(item) for item in sku_set}
    
    checkout_value = 0
    for offer_rule in offers:
        match offer_rule[0]:
            case "cross-bundle":
                basket[offer_rule[3]] = max(0, basket[offer_rule[3]] - basket[offer_rule[1]] // offer_rule[2])
            case "single-bundle":
                basket[offer_rule[1]] = basket[offer_rule[1]] % 3 + basket['F'] // 3 * 2

    # Special offer for item A
    checkout_value += basket['A'] // 5 * 200
    basket['A'] = basket['A'] % 5
    checkout_value += basket['A'] // 3 * 130
    basket['A'] = basket['A'] % 3

    # Special offer for item B (including D and E combination)
    basket['B'] = max(0, basket['B'] - basket['E'] // 2)
    checkout_value += basket['B'] // 2 * 45
    basket['B'] = basket['B'] % 2

    # Special offer for item F
    basket['F'] = basket['F'] % 3 + basket['F'] // 3 * 2

    # Calculate checkout value
    for item in basket:
        checkout_value += basket[item] * prices[item]
    return checkout_value






