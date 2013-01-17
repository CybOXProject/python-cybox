import cybox.bindings.cybox_common_types_1_0 as common_binding
import cybox.common.contributor as contributor

def create_from_dict(personnel):
    """Create the Personnel object representation from an input dictionary"""
    personnel_type = common_binding.PersonnelType()
    for contributor_dict in personnel:
        contributor_type = contributor.create_from_dict(contributor_dict)
        if contributor_type.hasContent_(): personnel_type.add_Contributor(contributor_type)
    return personnel_type

def parse_into_dict(element):
    """Parse and return a dictionary for a Personnel object"""
    pass
