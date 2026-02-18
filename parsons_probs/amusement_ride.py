def amusement_ride(height, age):
    """ Returns whether someone can ride based on height (inches) and age.
    Must be at least 48 inches tall. Under 12 needs an adult.

    >>> amusement_ride(50, 15)
    'Enjoy the ride!'
    >>> amusement_ride(50, 10)
    'You need an adult with you'
    >>> amusement_ride(48, 12)
    'Enjoy the ride!'
    >>> amusement_ride(48, 11)
    'You need an adult with you'
    >>> amusement_ride(45, 15)
    "Sorry, you're too short for this ride"
    >>> amusement_ride(40, 8)
    "Sorry, you're too short for this ride"
    """
