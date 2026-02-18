def graduation_check(num_credits, gpa):
    """ Returns "Graduate!" if credits >= 120 AND gpa >= 2.0,
    "Need to do more" otherwise.

    >>> graduation_check(120, 3.5)
    'Graduate!'
    >>> graduation_check(130, 2.0)
    'Graduate!'
    >>> graduation_check(110, 3.5)
    'Need to do more'
    >>> graduation_check(120, 1.5)
    'Need to do more'
    >>> graduation_check(100, 1.5)
    'Need to do more'
    """
