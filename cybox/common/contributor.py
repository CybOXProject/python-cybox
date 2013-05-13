# Copyright (c) 2013, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import cybox
import cybox.bindings.cybox_common as common_binding
from cybox.common import DateRange

class Contributor(cybox.Entity):
    def __init__(self):
        super(Contributor, self).__init__()
        self.role = None
        self.name = None
        self.email = None
        self.phone = None
        self.organization = None
        self.date = None
        self.contribution_location = None

    def to_obj(self):
        contributor_obj = common_binding.ContributorType()
        if self.role is not None : contributor_obj.set_Role(self.role)
        if self.name is not None : contributor_obj.set_Name(self.name)
        if self.email is not None : contributor_obj.set_Email(self.email)
        if self.phone is not None : contributor_obj.set_Phone(self.phone)
        if self.organization is not None : contributor_obj.set_Organization(self.organization)
        if self.date is not None : contributor_obj.set_Date(self.date.to_obj())
        if self.contribution_location is not None : contributor_obj.set_Contribution_Location(self.contribution_location)
        return contributor_obj

    def to_dict(self):
        contributor_dict = {}
        if self.role is not None : contributor_dict['role'] = self.role
        if self.name is not None : contributor_dict['name'] = self.name
        if self.email is not None : contributor_dict['email'] = self.email
        if self.phone is not None : contributor_dict['phone'] = self.phone
        if self.organization is not None : contributor_dict['organization'] = self.organization
        if self.date is not None : contributor_dict['date'] = self.date.to_obj()
        if self.contribution_location is not None : contributor_dict['contribution_location'] = self.contribution_location
        return contributor_dict

    @staticmethod
    def from_dict(contributor_dict):
        if not contributor_dict:
            return None
        contributor_ = Contributor()
        contributor_.role = contributor_dict.get('role')
        contributor_.name = contributor_dict.get('name')
        contributor_.email = contributor_dict.get('email')
        contributor_.phone = contributor_dict.get('phone')
        contributor_.organization = contributor_dict.get('organization')
        contributor_.date = DateRange.from_dict(contributor_dict.get('organization'))
        contributor_.contribution_location = contributor_dict.get('contribution_location')
        return contributor_

    @staticmethod
    def from_obj(contributor_obj):
        if not contributor_obj:
            return None
        contributor_ = Contributor()
        contributor_.role = contributor_obj.get_Role()
        contributor_.name = contributor_obj.get_Name()
        contributor_.email = contributor_obj.get_Email()
        contributor_.phone = contributor_obj.get_Phone()
        contributor_.organization = contributor_obj.get_Organization()
        contributor_.date = DateRange.from_obj(contributor_obj.get_Date())
        contributor_.contribution_location = contributor_obj.get_Contribution_Location()
        return contributor_