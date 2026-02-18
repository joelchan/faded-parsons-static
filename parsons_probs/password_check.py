def password_check(password):
    """ Returns "Warning: password is too short!" if password is less than
    8 characters, None otherwise.

    >>> password_check("abc")
    'Warning: password is too short!'
    >>> password_check("short")
    'Warning: password is too short!'
    >>> password_check("longenough")
    >>> password_check("12345678")
    """
