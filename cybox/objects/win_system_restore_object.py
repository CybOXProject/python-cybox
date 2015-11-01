# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from mixbox import entities
from mixbox import fields

import cybox.bindings.win_system_restore_object as win_system_restore_binding
from cybox.common import String, Long, DateTime, ObjectProperties


class HiveList(entities.EntityList):
    _binding = win_system_restore_binding
    _binding_class = win_system_restore_binding.HiveListType
    _namespace = "http://cybox.mitre.org/objects#WinSystemObject-2"
    hive = fields.TypedField("Hive", String, multiple=True)


class WinSystemRestore(ObjectProperties):
    _binding = win_system_restore_binding
    _binding_class = win_system_restore_binding.WindowsSystemRestoreObjectType
    _namespace = "http://cybox.mitre.org/objects#WinSystemRestoreObject-2"
    _XSI_NS = "WinSystemRestoreObj"
    _XSI_TYPE = "WindowsSystemRestoreObjectType"

    restore_point_description = fields.TypedField("Restore_Point_Description", String)
    restore_point_full_path = fields.TypedField("Restore_Point_Full_Path", String)
    acl_change_username = fields.TypedField("ACL_Change_Username", String)
    restore_point_name = fields.TypedField("Restore_Point_Name", String)
    restore_point_type = fields.TypedField("Restore_Point_Type", String)
    backup_file_name = fields.TypedField("Backup_File_Name", String)
    acl_change_sid = fields.TypedField("ACL_Change_SID", String)
    changelog_entry_flags = fields.TypedField("ChangeLog_Entry_Flags", String)
    changelog_entry_sequence_number = fields.TypedField("ChangeLog_Entry_Sequence_Number", Long)
    created = fields.TypedField("Created", DateTime)

    file_attributes = fields.TypedField("File_Attributes", String)
    new_file_name = fields.TypedField("New_File_Name", String)
    original_file_name = fields.TypedField("Original_File_Name", String)
    original_short_file_name = fields.TypedField("Original_Short_File_Name", String)
    process_name = fields.TypedField("Process_Name", String)

    change_event = fields.TypedField("Change_Event", String)
    changelog_entry_type = fields.TypedField("ChangeLog_Entry_Type", String)

    registry_hive_list = fields.TypedField("Registry_Hive_List", HiveList)
