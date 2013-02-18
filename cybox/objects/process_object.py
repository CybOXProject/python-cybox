import cybox.utils as utils
import cybox.bindings.cybox_common_types_1_0 as common_types_binding
import cybox.bindings.process_object_1_3 as process_binding
from cybox.objects.port_object import Port
from cybox.objects.address_object import Address
from cybox.common.baseobjectattribute import Base_Object_Attribute
from cybox.common.environment_variable_list import Environment_Variable_List
from cybox.common.extracted_string_list import Extracted_String_List

class Process:
    def __init__(self):
        pass
    
    @classmethod   
    def object_from_dict(cls, process_dict, process_obj = None):
        if process_obj == None:
            process_obj = process_binding.ProcessObjectType()
            process_obj.set_anyAttributes_({'xsi:type' : 'ProcessObj:ProcessObjectType'})
        
        for key, value in process_attributes.items():
            if key == 'is_hidden' and utils.test_value(value):
                process_obj.set_is_hidden(value.get('value'))
            elif key == 'name' and utils.test_value(value):
                process_obj.set_Name(Base_Object_Attribute.object_from_dict(common_types_binding.StringObjectAttributeType(datatype='String'),value))
            elif key == 'image_info':
                image_info = process_binding.ImageInfoType()
                for image_info_key, image_info_value in value.items():
                    if image_info_key == 'file_name' and utils.test_value(image_info_value):
                        image_info.set_File_Name(Base_Object_Attribute.object_from_dict(common_types_binding.StringObjectAttributeType(datatype='String'),image_info_value))
                    elif image_info_key == 'command_line' and utils.test_value(image_info_value):
                        image_info.set_Command_Line(Base_Object_Attribute.object_from_dict(common_types_binding.StringObjectAttributeType(datatype='String'),image_info_value))
                    elif image_info_key == 'current_directory' and utils.test_value(image_info_value):
                        image_info.set_Current_Directory(Base_Object_Attribute.object_from_dict(common_types_binding.StringObjectAttributeType(datatype='String'),image_info_value))
                    elif image_info_key == 'path' and utils.test_value(image_info_value):
                        image_info.set_Command_Line(Base_Object_Attribute.object_from_dict(common_types_binding.StringObjectAttributeType(datatype='String'),image_info_value))
                if image_info.hasContent_() : process_obj.set_Image_Info(image_info)
            elif key == 'pid' and utils.test_value(value):
                process_obj.set_PID(Base_Object_Attribute.object_from_dict(common_types_binding.UnsignedIntegerObjectAttributeType(datatype='UnsignedInt'),value))
            elif key == 'parent_pid' and utils.test_value(value):
                process_obj.set_Parent_PID(Base_Object_Attribute.object_from_dict(common_types_binding.UnsignedIntegerObjectAttributeType(datatype='UnsignedInt'),value))
            elif key == 'child_pid_list':
                child_list = process_binding.ChildPIDListType()
                for id in value:
                    child_list.add_Child_PID(Base_Object_Attribute.object_from_dict(common_types_binding.UnsignedIntegerObjectAttributeType(datatype='UnsignedInt'), id))
                if child_list.hasContent_() : process_obj.set_Child_PID_List(child_list)
            elif key == 'argument_list':
                arg_list = []
                for arg in value:
                    arg_list.append(Base_Object_Attribute.object_from_dict(common_types_binding.StringObjectAttributeType(datatype='String'),arg))
                argument_list = process_binding.ArgumentListType()
                argument_list.set_Argument(arg_list)
                process_obj.set_Argument_List(argument_list)
            elif key == 'Environment_Variable_List':
                env_variable_list = Environment_Variable_List.object_from_dict(value)
                if env_variable_list.hasContent_(): process_obj.set_Environment_Variable_List(env_list)
            elif key == 'port_list':
                port_list = process_binding.PortListType()
                for port_dict in value:
                    port_obj = port.object_from_dict(port_dict)
                    port_list.add_Port(port_obj)
                process_obj.set_Post_List(port_list)
            elif key == 'network_connection_list':
                conn_list = process_binding.NetworkConnectionListType()
                for conn_dict in value:
                    connobj = process_binding.NetworkConnectionType()
                    for conn_key, conn_value in conn_dict.items():
                        if conn_key == 'creation_time' and utils.test_value(conn_value):
                            connobj.set_Creation_Time(Base_Object_Attribute.object_from_dict(common_types_binding.DateTimeObjectAttributeType(datatype='DateTime'),conn_value))
                        elif conn_key == 'destination_ip_Address' and utils.test_value(conn_value):
                            connobj.set_Destination_Address(Address.object_from_dict(conn_value))
                        elif conn_key == 'destination_port' and utils.test_value(conn_value):
                            connobj.set_Source_Port(port.object_from_dict(conn_value))
                        elif conn_key == 'source_ip_Address' and utils.test_value(conn_value):
                            connobj.set_Source_Address(Address.object_from_dict(conn_value))
                        elif conn_key == 'source_port' and utils.test_value(conn_value):
                            connobj.set_Source_Port(port.object_from_dict(conn_value))
                        elif conn_key == 'tcp_state' and utils.test_value(conn_value):
                            connobj.set_TCP_State(Base_Object_Attribute.object_from_dict(common_types_binding.StringObjectAttributeType(datatype='String'), value))
                    if connobj.hasContent_() : conn_list.add_Network_Connection(connobj)
            elif key == 'string_list':
                string_list = Extracted_String_List.object_from_dict(value)
                if string_list.hasContent_() : process_obj.set_String_List(string_list)
            elif key == 'username' and utils.test_value(value):
                process_obj.set_Username(Base_Object_Attribute.object_from_dict(common_types_binding.StringObjectAttributeType(datatype='String'),value))
            elif key == 'creation_time' and utils.test_value(value):
                process_obj.set_Creation_Time(Base_Object_Attribute.object_from_dict(common_types_binding.DateTimeObjectAttributeType(datatype='DateTime'),value))
            elif key == 'start_time' and utils.test_value(value):
                process_obj.set_Start_Time(Base_Object_Attribute.object_from_dict(common_types_binding.DateTimeObjectAttributeType(datatype='DateTime'),value))
            elif key == 'kernel_time' and utils.test_value(value):
                process_obj.set_Kernel_Time(Base_Object_Attribute.object_from_dict(common_types_binding.DurationObjectAttributeType(datatype='Duration'),value))            
            elif key == 'user_time' and utils.test_value(value):
                process_obj.set_User_Time(Base_Object_Attribute.object_from_dict(common_types_binding.DurationObjectAttributeType(datatype='Duration'),value))            
                
        return process_obj

    @classmethod
    def dict_from_object(cls, process_obj):
        process_dict = {}
        if process_obj.get_is_hidden() is not None: process_dict['is_hidden'] = {'value' : process_obj.get_is_hidden()}
        if process_obj.get_PID() is not None: process_dict['pid'] = Base_Object_Attribute.dict_from_object(process_obj.get_PID())
        if process_obj.get_Creation_Time() is not None: process_dict['creation_time'] = Base_Object_Attribute.dict_from_object(process_obj.get_Creation_Time())
        if process_obj.get_Parent_PID() is not None: process_dict['parent_pid'] = Base_Object_Attribute.dict_from_object(process_obj.get_Parent_PID())
        if process_obj.get_Child_PID_List() is not None:
            child_pid_list = []
            for child_pid in process_obj.get_Child_PID_List().get_Child_PID():
                child_pid_list.append(Base_Object_Attribute.dict_from_object(child_pid)) 
            process_dict['child_pid_list'] = child_pid_list
        if process_obj.get_Image_Info() is not None:
            image_info = process_obj.get_Image_Info()
            image_info_dict = {}
            if image_info.get_File_Name() is not None: image_info_dict['file_name'] = Base_Object_Attribute.dict_from_object(image_info.get_File_Name())
            if image_info.get_Command_Line() is not None: image_info_dict['command_line'] = Base_Object_Attribute.dict_from_object(image_info.get_Command_Line())
            if image_info.get_Current_Directory() is not None: image_info_dict['current_directory'] = Base_Object_Attribute.dict_from_object(image_info.get_Current_Directory())
            if image_info.get_Path() is not None: image_info_dict['path'] = Base_Object_Attribute.dict_from_object(image_info.get_Path())
            process_dict['image_info'] = image_info_dict
        if process_obj.get_Argument_List() is not None:
            argument_list = []
            for argument in process_obj.get_Argument_List().get_Argument():
                argument_list.append(Base_Object_Attribute.dict_from_object(argument))
            process_dict['argument_list'] = argument_list
        if process_obj.get_Environment_Variable_List() is not None: process_dict['Environment_Variable_List'] = Environment_Variable_List.dict_from_object(process_obj.get_Environment_Variable_List())
        if process_obj.get_Kernel_Time() is not None: process_dict['kernel_time'] = Base_Object_Attribute.dict_from_object(image_info.get_Kernel_Time())
        if process_obj.get_Port_List() is not None: 
            port_list = []
            for port in process_obj.get_Port_List().get_Port():
                port_list.append(port.dict_from_object(port))
            process_dict['port_list'] = port_list
        if process_obj.get_Network_Connection_List() is not None:
            network_connection_list = []
            for network_connection in process_obj.get_Network_Connection_List().get_Network_Connection():
                network_connection_dict = {}
                if network_connection.get_Creation_Time() is not None: network_connection_dict['creation_time'] = Base_Object_Attribute.dict_from_object(network_connection.get_Creation_Time())
                if network_connection.get_Destination_IP_Address() is not None: network_connection_dict['destination_ip_Address'] = Address.dict_from_object(network_connection.get_Destination_IP_Address())
                if network_connection.get_Destination_Port() is not None: network_connection_dict['destination_port'] = port.dict_from_object(network_connection.get_Destination_Port())
                if network_connection.get_Source_IP_Address() is not None: network_connection_dict['source_ip_Address'] = Address.dict_from_object(network_connection.get_Source_IP_Address())
                if network_connection.get_Destination_Port() is not None: network_connection_dict['source_port'] = port.dict_from_object(network_connection.get_Source_Port())
                if network_connection.get_TCP_State() is not None: network_connection_dict['tcp_state'] = Base_Object_Attribute.dict_from_object(network_connection.get_TCP_State())
                network_connection_list.append(network_connection_dict)
            process_dict['network_connection_list'] = network_connection_list
        if process_obj.get_Start_Time() is not None: process_dict['start_time'] = Base_Object_Attribute.dict_from_object(process_obj.get_Start_Time())
        if process_obj.get_Status() is not None: process_dict['status'] = Base_Object_Attribute.dict_from_object(process_obj.get_Status())
        if process_obj.get_String_List() is not None: process_dict['Extracted_String_List'] = Extracted_String_List.dict_from_object(process_obj.get_String_List())
        if process_obj.get_Username() is not None: process_dict['username'] = Base_Object_Attribute.dict_from_object(process_obj.get_Username())
        if process_obj.get_User_Time() is not None: process_dict['user_time'] = Base_Object_Attribute.dict_from_object(process_obj.get_User_Time())
        return process_dict