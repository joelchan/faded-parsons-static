def polling_booth(registration_here, need_assistance):
    """ Returns directions for a voter at a polling station.
    If registered here and needs assistance: "Go to the assisted booth"
    If registered here and no assistance needed: "Go to the normal booth"
    If not registered here: "Go away and register"

    >>> polling_booth(True, True)
    'Go to the assisted booth'
    >>> polling_booth(True, False)
    'Go to the normal booth'
    >>> polling_booth(False, True)
    'Go away and register'
    >>> polling_booth(False, False)
    'Go away and register'
    """
