def shopping_decision(on_sale, price, money):
    """ Returns "Buy it!" if the item is on sale AND you have enough money,
    "Maybe next time." otherwise.

    >>> shopping_decision(True, 25, 30)
    'Buy it!'
    >>> shopping_decision(True, 25, 25)
    'Buy it!'
    >>> shopping_decision(True, 25, 20)
    'Maybe next time.'
    >>> shopping_decision(False, 25, 30)
    'Maybe next time.'
    """
