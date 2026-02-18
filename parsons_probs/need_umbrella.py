def need_umbrella(is_raining, rain_chance, has_rain_jacket):
    """ Returns whether you should bring an umbrella.
    Bring one if it's raining OR (rain chance > 50% AND you don't have a rain jacket).

    >>> need_umbrella(True, 0, False)
    'Bring an umbrella!'
    >>> need_umbrella(True, 0, True)
    'Bring an umbrella!'
    >>> need_umbrella(False, 80, False)
    'Bring an umbrella!'
    >>> need_umbrella(False, 80, True)
    'No umbrella needed.'
    >>> need_umbrella(False, 50, False)
    'No umbrella needed.'
    >>> need_umbrella(False, 30, False)
    'No umbrella needed.'
    """
