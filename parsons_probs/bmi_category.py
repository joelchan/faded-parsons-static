def bmi_category(bmi):
    """ Returns the BMI category for the given BMI value.
    Under 18.5: "Underweight", 18.5-24.9: "Normal weight",
    25.0-29.9: "Overweight", 30+: "Obese"

    >>> bmi_category(16)
    'Underweight'
    >>> bmi_category(18.4)
    'Underweight'
    >>> bmi_category(18.5)
    'Normal weight'
    >>> bmi_category(22.5)
    'Normal weight'
    >>> bmi_category(24.9)
    'Normal weight'
    >>> bmi_category(25.0)
    'Overweight'
    >>> bmi_category(29.9)
    'Overweight'
    >>> bmi_category(30.0)
    'Obese'
    >>> bmi_category(35)
    'Obese'
    """
