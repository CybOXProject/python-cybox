# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from mixbox import entities
from mixbox import fields

import cybox.bindings.process_object as process_binding
from cybox.common import ObjectProperties, String, DateTime, UnsignedInteger, Duration, EnvironmentVariableList, ExtractedFeatures
from cybox.objects.network_connection_object import NetworkConnection
from cybox.objects.port_object import Port


class PortList(entities.EntityList):
    _binding = process_binding
    _binding_class = process_binding.PortListType
    _namespace = "http://cybox.mitre.org/objects#ProcessObject-2"
    port = fields.TypedField("Port", Port, multiple=True)


class NetworkConnectionList(entities.EntityList):
    _binding = process_binding
    _binding_class = process_binding.NetworkConnectionListType
    _namespace = "http://cybox.mitre.org/objects#ProcessObject-2"
    network_connection = fields.TypedField("Network_Connection", NetworkConnection, multiple=True)


class ChildPIDList(entities.EntityList):
    _binding = process_binding
    _binding_class = process_binding.ChildPIDListType
    _namespace = "http://cybox.mitre.org/objects#ProcessObject-2"
    child_pid = fields.TypedField("Child_PID", UnsignedInteger, multiple=True)


class ArgumentList(entities.EntityList):
    _binding = process_binding
    _binding_class = process_binding.ArgumentListType
    _namespace = "http://cybox.mitre.org/objects#ProcessObject-2"
    argument = fields.TypedField("Argument", String, multiple=True)


class ImageInfo(entities.Entity):
    _binding = process_binding
    _binding_class = process_binding.ImageInfoType
    _namespace = "http://cybox.mitre.org/objects#ProcessObject-2"

    file_name = fields.TypedField("File_Name", String)
    command_line = fields.TypedField("Command_Line", String)
    current_directory = fields.TypedField("Current_Directory", String)
    path = fields.TypedField("Path", String)


class Process(ObjectProperties):
    _binding = process_binding
    _binding_class = process_binding.ProcessObjectType
    _namespace = "http://cybox.mitre.org/objects#ProcessObject-2"
    _XSI_NS = "ProcessObj"
    _XSI_TYPE = "ProcessObjectType"

    pid = fields.TypedField("PID", UnsignedInteger)
    name = fields.TypedField("Name", String)
    creation_time = fields.TypedField("Creation_Time", DateTime)
    parent_pid = fields.TypedField("Parent_PID", UnsignedInteger)
    child_pid_list = fields.TypedField("Child_PID_List", ChildPIDList)
    image_info = fields.TypedField("Image_Info", ImageInfo)
    argument_list = fields.TypedField("Argument_List", ArgumentList)
    environment_variable_list = fields.TypedField("Environment_Variable_List", EnvironmentVariableList)
    kernel_time = fields.TypedField("Kernel_Time", Duration)
    port_list = fields.TypedField("Port_List", PortList)
    network_connection_list = fields.TypedField("Network_Connection_List", NetworkConnectionList)
    start_time = fields.TypedField("Start_Time", DateTime)
    #status TODO: Add support
    username = fields.TypedField("Username", String)
    user_time = fields.TypedField("User_Time", Duration)
    extracted_features = fields.TypedField("Extracted_Features", ExtractedFeatures)
    is_hidden = fields.TypedField("is_hidden")


