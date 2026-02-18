def time_greeting(hour):
    """ Returns a greeting based on the hour of the day (0-23).
    Before 12: "Good morning!", 12-16: "Good afternoon!",
    17-20: "Good evening!", after 20: "Good night!"

    >>> time_greeting(8)
    'Good morning!'
    >>> time_greeting(11)
    'Good morning!'
    >>> time_greeting(12)
    'Good afternoon!'
    >>> time_greeting(14)
    'Good afternoon!'
    >>> time_greeting(16)
    'Good afternoon!'
    >>> time_greeting(17)
    'Good evening!'
    >>> time_greeting(20)
    'Good evening!'
    >>> time_greeting(21)
    'Good night!'
    >>> time_greeting(23)
    'Good night!'
    """
