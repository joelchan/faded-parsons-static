def ticket_price(age, theater_staff):
    """ Returns the ticket price based on age and staff status.
    Children under 5 and seniors 65+ get in free (0).
    Theater staff pay 7.50.
    Everyone else pays 15.

    >>> ticket_price(3, False)
    0
    >>> ticket_price(65, False)
    0
    >>> ticket_price(70, True)
    0
    >>> ticket_price(30, True)
    7.5
    >>> ticket_price(30, False)
    15
    >>> ticket_price(20, False)
    15
    """
