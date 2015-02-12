# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import cybox
import cybox.bindings.process_object as process_binding
from cybox.common import ObjectProperties, String, DateTime, UnsignedInteger, Duration, EnvironmentVariableList, ExtractedFeatures
from cybox.objects.address_object import Address
from cybox.objects.network_connection_object import NetworkConnection
from cybox.objects.port_object import Port

class PortList(cybox.EntityList):
    _binding = process_binding
    _binding_class = process_binding.PortListType
    _binding_var = "Port"
    _contained_type = Port
    _namespace = "http://cybox.mitre.org/objects#ProcessObject-2"

class NetworkConnectionList(cybox.EntityList):
    _binding = process_binding
    _binding_class = process_binding.NetworkConnectionListType
    _binding_var = "Network_Connection"
    _contained_type = NetworkConnection
    _namespace = "http://cybox.mitre.org/objects#ProcessObject-2"

class ChildPIDList(cybox.EntityList):
    _binding = process_binding
    _binding_class = process_binding.ChildPIDListType
    _binding_var = "Child_PID"
    _contained_type = UnsignedInteger
    _namespace = "http://cybox.mitre.org/objects#ProcessObject-2"

class ArgumentList(cybox.EntityList):
    _binding = process_binding
    _binding_class = process_binding.ArgumentListType
    _binding_var = "Argument"
    _contained_type = String
    _namespace = "http://cybox.mitre.org/objects#ProcessObject-2"

class ImageInfo(cybox.Entity):
    _binding = process_binding
    _binding_class = process_binding.ImageInfoType
    _namespace = "http://cybox.mitre.org/objects#ProcessObject-2"

    file_name = cybox.TypedField("File_Name", String)
    command_line = cybox.TypedField("Command_Line", String)
    current_directory = cybox.TypedField("Current_Directory", String)
    path = cybox.TypedField("Path", String)

class Process(ObjectProperties):
    _binding = process_binding
    _binding_class = process_binding.ProcessObjectType
    _namespace = "http://cybox.mitre.org/objects#ProcessObject-2"
    _XSI_NS = "ProcessObj"
    _XSI_TYPE = "ProcessObjectType"

    pid = cybox.TypedField("PID", UnsignedInteger)
    name = cybox.TypedField("Name", String)
    creation_time = cybox.TypedField("Creation_Time", DateTime)
    parent_pid = cybox.TypedField("Parent_PID", UnsignedInteger)
    child_pid_list = cybox.TypedField("Child_PID_List", ChildPIDList)
    image_info = cybox.TypedField("Image_Info", ImageInfo)
    argument_list = cybox.TypedField("Argument_List", ArgumentList)
    environment_variable_list = cybox.TypedField("Environment_Variable_List", EnvironmentVariableList)
    kernel_time = cybox.TypedField("Kernel_Time", Duration)
    port_list = cybox.TypedField("Port_List", PortList)
    network_connection_list = cybox.TypedField("Network_Connection_List", NetworkConnectionList)
    start_time = cybox.TypedField("Start_Time", DateTime)
    #status TODO: Add support
    username = cybox.TypedField("Username", String)
    user_time = cybox.TypedField("User_Time", Duration)
    extracted_features = cybox.TypedField("Extracted_Features", ExtractedFeatures)



