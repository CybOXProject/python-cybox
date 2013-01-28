#Common utility methods

#Test if a dictionary value is not None and has a length greater than 0
def test_value(value):
    if value.get('value') is not None:
        if value.get('value')  is not None and len(str(value.get('value'))) > 0:
            return True 
        else:
            return False
    else:
        return False
