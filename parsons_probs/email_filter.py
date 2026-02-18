def email_filter(from_known_contact, contains_unsubscribe):
    """ Returns which folder an email should be sorted into.
    Known contact: "Inbox"
    Unknown + has unsubscribe link: "Promotions"
    Unknown + no unsubscribe link: "Unknown - review manually"

    >>> email_filter(True, False)
    'Inbox'
    >>> email_filter(True, True)
    'Inbox'
    >>> email_filter(False, True)
    'Promotions'
    >>> email_filter(False, False)
    'Unknown - review manually'
    """
