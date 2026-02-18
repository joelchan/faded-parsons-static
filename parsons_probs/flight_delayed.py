def flight_delayed(wind_speed, visibility, is_clear):
    """ Returns whether a flight is delayed.
    Delayed if wind > 40 mph OR (visibility < 3 miles AND conditions are not clear).

    >>> flight_delayed(45, 10, True)
    'Flight delayed.'
    >>> flight_delayed(45, 1, False)
    'Flight delayed.'
    >>> flight_delayed(20, 2, False)
    'Flight delayed.'
    >>> flight_delayed(20, 1, False)
    'Flight delayed.'
    >>> flight_delayed(20, 2, True)
    'Flight on time.'
    >>> flight_delayed(20, 10, True)
    'Flight on time.'
    >>> flight_delayed(20, 5, False)
    'Flight on time.'
    """
