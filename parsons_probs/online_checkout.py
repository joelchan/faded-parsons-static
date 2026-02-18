def online_checkout(logged_in, items_in_cart):
    """ Returns the checkout status message.
    If logged in and items in cart: "Proceeding to checkout"
    If logged in but empty cart: "Your cart is empty"
    If not logged in: "Please log in first"

    >>> online_checkout(True, 3)
    'Proceeding to checkout'
    >>> online_checkout(True, 1)
    'Proceeding to checkout'
    >>> online_checkout(True, 0)
    'Your cart is empty'
    >>> online_checkout(False, 3)
    'Please log in first'
    >>> online_checkout(False, 0)
    'Please log in first'
    """
