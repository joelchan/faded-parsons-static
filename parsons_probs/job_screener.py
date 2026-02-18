def job_screener(has_degree, years_experience):
    """ Returns the hiring decision based on degree and experience.
    With degree: 3+ years -> "Schedule an interview", else "Consider for junior position".
    Without degree: 5+ years -> "Schedule an interview", else "Does not meet requirements".

    >>> job_screener(True, 5)
    'Schedule an interview'
    >>> job_screener(True, 3)
    'Schedule an interview'
    >>> job_screener(True, 1)
    'Consider for junior position'
    >>> job_screener(False, 6)
    'Schedule an interview'
    >>> job_screener(False, 5)
    'Schedule an interview'
    >>> job_screener(False, 3)
    'Does not meet requirements'
    """
