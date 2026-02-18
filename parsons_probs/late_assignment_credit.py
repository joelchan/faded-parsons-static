def late_assignment_credit(submission_date, target_date):
    """ Returns the credit percentage for a late assignment.
    On time: 100%, up to 1 week late: 85%, up to 2 weeks late: 70%, later: 0%.

    >>> late_assignment_credit(35, 36)
    100
    >>> late_assignment_credit(36, 36)
    100
    >>> late_assignment_credit(40, 36)
    85
    >>> late_assignment_credit(43, 36)
    85
    >>> late_assignment_credit(45, 36)
    70
    >>> late_assignment_credit(50, 36)
    70
    >>> late_assignment_credit(51, 36)
    0
    >>> late_assignment_credit(60, 36)
    0
    """
