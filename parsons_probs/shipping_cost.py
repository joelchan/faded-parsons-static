def shipping_cost(weight):
    """ Returns the shipping cost based on package weight in pounds.
    Under 1 lb: 3, 1-5 lbs: 7, over 5 lbs: 12.

    >>> shipping_cost(0.5)
    3
    >>> shipping_cost(1)
    7
    >>> shipping_cost(3.5)
    7
    >>> shipping_cost(5)
    7
    >>> shipping_cost(5.1)
    12
    >>> shipping_cost(10)
    12
    """
