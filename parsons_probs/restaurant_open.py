def restaurant_open(hour):
    """ Returns whether a restaurant is open based on the hour (24-hour time).
    Open during lunch (11-14) OR dinner (17-21).

    >>> restaurant_open(12)
    'We are open!'
    >>> restaurant_open(11)
    'We are open!'
    >>> restaurant_open(14)
    'We are open!'
    >>> restaurant_open(18)
    'We are open!'
    >>> restaurant_open(17)
    'We are open!'
    >>> restaurant_open(21)
    'We are open!'
    >>> restaurant_open(15)
    'Sorry, we are closed.'
    >>> restaurant_open(9)
    'Sorry, we are closed.'
    >>> restaurant_open(23)
    'Sorry, we are closed.'
    """
