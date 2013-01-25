#Common utility methods

#Test if a value is not None and has a length greater than 0
def test_value(value):
    if value is not None and len(str(value)) > 0:
        return True
    else:
        return False
