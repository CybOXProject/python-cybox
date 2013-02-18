import cybox.bindings.cybox_common_types_1_0 as common_binding

class DateRange(object):
    def __init__(self):
        pass

    @classmethod
    def object_from_dict(cls, daterange_dict):
        """Create the DateRange object representation from an input dictionary"""
        daterange_obj = common_binding.DateRangeType()
        for date_key, date_value in daterange_dict.items():
            if date_key == 'start_date' : daterange_obj.set_start_date(date_value)
            if date_key == 'end_date' : daterange_obj.set_end_date(date_value)
        return daterange_obj

    @classmethod
    def dict_from_object(cls, daterange_obj):
        """Parse and return a dictionary for a DateRange object"""
        pass
