"""Common utility methods"""

def test_value(value):
    """
    Test if a dictionary contains a "value" key whose value is not None
    and has a length greater than 0.

    We explicitly want to return True even if the value is False or 0, since
    some parts of the standards are boolean or allow a 0 value, and we want to
    distinguish the case where the "value" key is omitted entirely.
    """
    v = value.get('value', None)
    return (v is not None) and (len(str(v)) > 0)
