def water_state(temp_c):
    """ Returns the state of water at the given temperature in Celsius.
    0 or below: "Solid (ice)", above 100: "Gas (steam)",
    otherwise: "Liquid (water)"

    >>> water_state(-5)
    'Solid (ice)'
    >>> water_state(0)
    'Solid (ice)'
    >>> water_state(50)
    'Liquid (water)'
    >>> water_state(100)
    'Liquid (water)'
    >>> water_state(105)
    'Gas (steam)'
    """
