def can_register(has_prereq, credits):
    """ Returns whether a student can register for a class.
    Must have the prerequisite AND be at least a junior (60+ credits).

    >>> can_register(True, 60)
    'You can register!'
    >>> can_register(True, 90)
    'You can register!'
    >>> can_register(True, 75)
    'You can register!'
    >>> can_register(False, 60)
    'You cannot register.'
    >>> can_register(False, 90)
    'You cannot register.'
    >>> can_register(True, 59)
    'You cannot register.'
    >>> can_register(False, 30)
    'You cannot register.'
    """
