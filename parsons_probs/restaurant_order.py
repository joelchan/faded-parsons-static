def restaurant_order(is_open, on_menu, in_stock):
    """ Returns the order status based on restaurant availability.

    >>> restaurant_order(True, True, True)
    'Order placed!'
    >>> restaurant_order(True, True, False)
    'Sorry, that item is sold out'
    >>> restaurant_order(True, False, True)
    "We don't serve that here"
    >>> restaurant_order(True, False, False)
    "We don't serve that here"
    >>> restaurant_order(False, True, True)
    "Sorry, we're closed"
    >>> restaurant_order(False, False, False)
    "Sorry, we're closed"
    """
