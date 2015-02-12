# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import cybox
import cybox.bindings.win_system_restore_object as win_system_restore_binding
from cybox.objects.system_object import System
from cybox.common import String, HexBinary, Long, DateTime, ObjectProperties


class HiveList(cybox.EntityList):
    _binding = win_system_restore_binding
    _binding_class = win_system_restore_binding.HiveListType
    _binding_var = "Hive"
    _contained_type = String
    _namespace = "http://cybox.mitre.org/objects#WinSystemObject-2"


class WinSystemRestore(ObjectProperties):
    _binding = win_system_restore_binding
    _binding_class = win_system_restore_binding.WindowsSystemRestoreObjectType
    _namespace = "http://cybox.mitre.org/objects#WinSystemRestoreObject-2"
    _XSI_NS = "WinSystemRestoreObj"
    _XSI_TYPE = "WindowsSystemRestoreObjectType"

    restore_point_description = cybox.TypedField("Restore_Point_Description", String)
    restore_point_full_path = cybox.TypedField("Restore_Point_Full_Path", String)
    acl_change_username = cybox.TypedField("ACL_Change_Username", String)
    restore_point_name = cybox.TypedField("Restore_Point_Name", String)
    restore_point_type = cybox.TypedField("Restore_Point_Type", String)
    backup_file_name = cybox.TypedField("Backup_File_Name", String)
    acl_change_sid = cybox.TypedField("ACL_Change_SID", String)
    changelog_entry_flags = cybox.TypedField("ChangeLog_Entry_Flags", String)
    changelog_entry_sequence_number = cybox.TypedField("ChangeLog_Entry_Sequence_Number", Long)
    created = cybox.TypedField("Created", DateTime)
    
    file_attributes = cybox.TypedField("File_Attributes", String)
    new_file_name = cybox.TypedField("New_File_Name", String)
    original_file_name = cybox.TypedField("Original_File_Name", String)
    original_short_file_name = cybox.TypedField("Original_Short_File_Name", String)
    process_name = cybox.TypedField("Process_Name", String)
    
    change_event = cybox.TypedField("Change_Event", String)
    changelog_entry_type = cybox.TypedField("ChangeLog_Entry_Type", String)
    
    registry_hive_list = cybox.TypedField("Registry_Hive_List", HiveList)
    
    
    
    
    
