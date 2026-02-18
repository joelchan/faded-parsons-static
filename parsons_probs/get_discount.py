def get_discount(is_student, age):
    """ Returns whether someone gets a discount.
    Eligible if they are a student OR a senior (age 65 or older).

    >>> get_discount(True, 20)
    'You get a discount!'
    >>> get_discount(True, 70)
    'You get a discount!'
    >>> get_discount(False, 65)
    'You get a discount!'
    >>> get_discount(False, 70)
    'You get a discount!'
    >>> get_discount(False, 30)
    'No discount available.'
    >>> get_discount(False, 64)
    'No discount available.'
    """
