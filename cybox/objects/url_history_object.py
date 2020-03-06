# Copyright (c) 2020, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from mixbox import entities, fields

import cybox.bindings.url_history_object as url_binding
from cybox.common import (
    DateTime, NonNegativeInteger, ObjectProperties, String, ToolInformation
)
from cybox.objects.hostname_object import Hostname
from cybox.objects.uri_object import URI


class URLHistoryEntry(entities.Entity):
    _binding = url_binding
    _binding_class = url_binding.URLHistoryEntryType
    _namespace = "http://cybox.mitre.org/objects#URLHistoryObject-1"

    url = fields.TypedField("URL", URI)
    hostname = fields.TypedField("Hostname", Hostname)
    referrer_url = fields.TypedField("Referrer_URL", URI)
    page_title = fields.TypedField("Page_Title", String)
    user_profile_name = fields.TypedField("User_Profile_Name", String)
    visit_count = fields.TypedField("Visit_Count", NonNegativeInteger)
    manually_entered_count = fields.TypedField("Manually_Entered_Count", NonNegativeInteger)
    modification_datetime = fields.TypedField("Modification_DateTime", DateTime)
    expiration_datetime = fields.TypedField("Expiration_DateTime", DateTime)
    first_visit_datetime = fields.TypedField("First_Visit_DateTime", DateTime)
    last_visit_datetime = fields.TypedField("Last_Visit_DateTime", DateTime)


class URLHistory(ObjectProperties):
    _binding = url_binding
    _binding_class = url_binding.URLHistoryObjectType
    _namespace = "http://cybox.mitre.org/objects#URLHistoryObject-1"
    _XSI_NS = "URLHistoryObj"
    _XSI_TYPE = "URLHistoryObjectType"

    browser_information = fields.TypedField("Browser_Information", ToolInformation)
    url_history_entry = fields.TypedField("URL_History_Entry", URLHistoryEntry, multiple=True)
