import cybox
#import cybox.bindings.cybox_common_types_1_0 as common_types_binding
import cybox.bindings.process_object_1_3 as process_binding
from cybox.objects.port_object import Port
from cybox.objects.address_object import Address
from cybox.common.extracted_string_list import ExtractedStringList
from cybox.common.environment_variable_list import EnvironmentVariableList
from cybox.common import DefinedObject, String, DateTime, UnsignedInteger, Duration

class Process(DefinedObject):
    _XSI_TYPE = "ProcessObjectType"

    def __init__(self):
        self.is_hidden = None
        self.pid = None
        self.name = None
        self.creation_time = None
        self.parent_pid = None
        self.child_pid_list = []
        self.image_info = None
        self.argument_list = []
        self.environment_variable_list = None
        self.kernel_time = None
        self.port_list = []
        self.network_connection_list = []
        self.start_time = None
        self.status = None
        self.string_list = None
        self.username = None
        self.user_time = None

    def to_obj(self, process_obj = None):
        if process_obj == None:
            process_obj = process_binding.ProcessObjectType()
            process_obj.set_anyAttributes_({'xsi:type' : 'ProcessObj:ProcessObjectType'})
        
        if self.is_hidden is not None: process_obj.set_is_hidden(self.is_hidden)
        if self.pid is not None: process_obj.set_PID(self.pid.to_obj())
        if self.name is not None: process_obj.set_Name(self.name.to_obj())
        if self.creation_time is not None: process_obj.set_Creation_Time(self.creation_time.to_obj())
        if self.parent_pid is not None: process_obj.set_Parent_PID(self.parent_pid.to_obj())
        if self.child_pid_list is not None:
            child_pid_list_obj = process_binding.ChildPIDListType() 
            for child_pid_obj in self.child_pid_list:
                child_pid_list_obj.add_Child_PID(child_pid_obj.to_obj())
            process_obj.set_Child_PID_List(child_pid_list_obj)
        if self.image_info is not None: process_obj.set_Image_Info(self.image_info.to_obj())
        if self.argument_list is not None: 
            argument_list_obj = process_binding.ArgumentListType()
            for argument_obj in self.argument_list:
                argument_list_obj.add_Argument(argument_obj.to_obj())
            process_obj.set_Argument_List(argument_list_obj)
        if self.environment_variable_list is not None: process_obj.set_Environment_Variable_List(self.environment_variable_list.to_obj())
        if self.kernel_time is not None: process_obj.set_Kernel_Time(self.kernel_time.to_obj())
        if self.port_list is not None: 
            port_list_obj = process_binding.PortListType()
            for port_obj in self.port_list:
                port_list_obj.add_Port(port_obj.to_obj())
            process_obj.set_Port_List(port_list_obj)
        if self.network_connection_list() is not None :
            netcon_list_obj = process_binding.NetworkConnectionListType()
            for network_conn_obj in self.network_connection_list:
                netcon_list_obj.add_Network_Connection(network_conn_obj.to_obj())
            process_obj.set_Network_Connection_List(netcon_list_obj)
        if self.start_time is not None: process_obj.set_Start_Time(self.start_time.to_obj())
        if self.status is not None: pass
        if self.string_list is not None: process_obj.set_String_List(self.string_list.to_obj())
        if self.username is not None: process_obj.set_Username(self.username.to_obj())
        if self.user_time is not None: process_obj.set_User_Time(self.usertime.to_obj())

        return process_obj

    def to_dict(self):
        process_dict = {}

        if self.is_hidden is not None: process_dict['is_hidden'] = self.is_hidden
        if self.pid is not None: process_dict['is_hidden'] = self.pid.to_dict()
        if self.name is not None: process_dict['name'] = self.name.to_dict()
        if self.creation_time is not None: process_dict['creation_time'] = self.creation_time.to_dict()
        if self.parent_pid is not None: process_dict['parent_pid'] = self.parent_pid.to_dict()
        if self.child_pid_list is not None:
            child_pid_list = []
            for child_pid_obj in self.child_pid_list:
                child_pid_list.append(child_pid_obj.to_dict())
            process_dict['child_pid_list'] = child_pid_list
        if self.image_info is not None: process_dict['image_info'] = self.image_info.to_dict()
        if self.argument_list is not None: 
            argument_list = []
            for argument_obj in self.argument_list:
                argument_list.append(argument_obj.to_dict())
            process_dict['argument_list'] = argument_list
        if self.environment_variable_list is not None: process_dict['environment_variable_list'] = self.environment_variable_list.to_list()
        if self.kernel_time is not None: process_dict['kernel_time'] = self.kernel_time.to_dict()
        if self.port_list is not None: 
            port_list = []
            for port_obj in self.port_list:
                port_list.append(port_obj.to_dict())
            process_dict['port_list'] = port_list
        if self.network_connection_list() is not None : 
            netcon_list = []
            for network_conn_obj in self.network_connection_list:
                netcon_list.append(network_conn_obj.to_dict())
            process_dict['network_connection_list'] = netcon_list
        if self.start_time is not None: process_dict['start_time'] = self.start_time.to_dict()
        if self.status is not None: pass
        if self.string_list is not None: process_dict['string_list'] = self.string_list.to_list()
        if self.username is not None: process_dict['username'] = self.username.to_dict()
        if self.user_time is not None: process_dict['user_time'] = self.user_time.to_dict()
        process_dict['xsi:type'] = _XSI_TYPE

        return process_dict
    
    @staticmethod
    def from_dict(process_dict, process_cls = None):
        if not process_dict:
            return None                
        if process_cls == None:
            process_ = Process()
        else:
            process_ = process_cls
        
        process_.is_hidden = process_dict.get('is_hidden')
        process_.pid = UnsignedInteger.from_dict(process_dict.get('pid'))
        process_.name = String.from_dict(process_dict.get('name'))
        process_.creation_time = DateTime.from_dict(process_dict.get('creation_time'))
        process_.parent_pid = UnsignedInteger.from_dict(process_dict.get('parent_pid'))
        process_.child_pid_list = [UnsignedInteger.from_dict(x) for x in process_dict.get('child_pid_list')]
        process_.image_info = ImageInfo.from_dict(process_dict.get('image_info'))
        process_.argument_list = [String.from_dict(x) for x in process_dict.get('argument_list')]
        process_.environment_variable_list = EnvironmentVariableList.from_list(process_dict.get('environment_variable_list'))
        process_.kernel_time = Duration.from_dict(process_dict.get('kernel_time'))
        process_.port_list = [Port.from_dict(x) for x in process_dict.get('port_list')]
        process_.network_connection_list = [ProcessNetworkConnection.from_dict(x) for x in process_dict.get('network_connection_list')]
        process_.start_time = DateTime.from_dict(process_dict.get('start_time'))
        process_.string_list = ExtractedStringList.from_list(process_dict.get('string_list'))
        process_.username = String.from_dict(process_dict.get('username'))
        process_.user_time = Duration.from_dict(process_dict.get('user_time'))

        return process_

    @staticmethod
    def from_obj(process_obj, process_cls = None):
        if not process_obj:
            return None                
        if process_cls == None:
            process_ = Process()
        else:
            process_ = process_cls

        process_.is_hidden = process_obj.get_is_hidden()
        process_.pid = UnsignedInteger.from_obj(process_obj.get_PID())
        process_.name = String.from_obj(process_obj.get_Name())
        process_.creation_time = DateTime.from_obj(process_obj.get_Creation_Time())
        process_.parent_pid = UnsignedInteger.from_obj(process_obj.get_Parent_PID())
        process_.child_pid_list = [UnsignedInteger.from_obj(x) for x in process_obj.get_Child_PID_List().get_Child_PID()]
        process_.image_info = ImageInfo.from_obj(process_obj.get_Image_Info())
        process_.argument_list = [String.from_obj(x) for x in process_obj.get_Argument_List().get_Argument()]
        process_.environment_variable_list = EnvironmentVariableList.from_obj(process_obj.get_Environment_Variable_List())
        process_.kernel_time = Duration.from_obj(process_obj.get_Kernel_Time())
        process_.port_list = [Port.from_obj(x) for x in process_obj.get_Port_List().get_Port()]
        process_.network_connection_list = [ProcessNetworkConnection.from_obj(x) for x in process_obj.get_Network_Connection_List().get_Network_Connection()]
        process_.start_time = DateTime.from_obj(process_obj.get_Start_Time())
        process_.string_list = ExtractedStringList.from_obj(process_obj.get_String_List())
        process_.username = String.from_obj(process_obj.get_Username())
        process_.user_time = Duration.from_obj(process_obj.get_User_Time())

        return process_


class ProcessNetworkConnection(cybox.Entity):
    def __init__(self, dest_ip = None, dest_port = None, source_ip = None, source_port = None):
        self.creation_time = None
        self.destination_ip_address = dest_ip
        self.destination_port = dest_port
        self.source_ip_address = source_ip
        self.source_port = source_port
        self.tcp_state = None
    
    def to_obj(self):
        network_connection_obj = process_binding.NetworkConnectionType()

        if self.creation_time is not None: network_connection_obj.set_Creation_Time(self.creation_time.to_obj())
        if self.destination_ip_address is not None: network_connection_obj.set_Destination_IP_Address(self.destination_ip_address.to_obj()) 
        if self.destination_port is not None: network_connection_obj.set_Destination_Port(self.destination_port.to_obj()) 
        if self.source_ip_address is not None: network_connection_obj.set_Source_IP_Address(self.source_ip_address.to_obj()) 
        if self.source_port is not None: network_connection_obj.set_Source_Port(self.source_port.to_obj()) 
        if self.tcp_state is not None: network_connection_obj.set_TCP_State(self.tcp_state.to_obj()) 

        return network_connection_obj

    def to_dict(self):
        network_connection_dict = {}

        if self.creation_time is not None: network_connection_dict['creation_time'] = self.creation_time.to_dict()
        if self.destination_ip_address is not None: network_connection_dict['destination_ip_address'] = self.destination_ip_address.to_dict()
        if self.destination_port is not None: network_connection_dict['destination_port'] = self.destination_port.to_dict() 
        if self.source_ip_address is not None: network_connection_dict['source_ip_address'] = self.source_ip_address.to_dict()
        if self.source_port is not None: network_connection_dict['source_port'] = self.source_port.to_dict() 
        if self.tcp_state is not None: network_connection_dict['tcp_state'] = self.tcp_state.to_dict()

        return network_connection_dict

    @staticmethod
    def from_dict(network_connection_dict):
        if not network_connection_dict:
            return None

        network_connection_ = ProcessNetworkConnection()
        network_connection_.creation_time = DateTime.from_dict(network_connection_dict.get('creation_time'))
        network_connection_.destination_ip_address = Address.from_dict(network_connection_dict.get('destination_ip_address'))
        network_connection_.destination_port = Port.from_dict(network_connection_dict.get('destination_port'))
        network_connection_.source_ip_address = Address.from_dict(network_connection_dict.get('source_ip_address'))
        network_connection_.source_port = Port.from_dict(network_connection_dict.get('source_port'))
        network_connection_.tcp_state = String.from_dict(network_connection_dict.get('tcp_state'))

        return network_connection_

    @staticmethod
    def from_obj(network_connection_obj):
        if not network_connection_obj:
            return None

        network_connection_ = ProcessNetworkConnection()
        network_connection_.creation_time = DateTime.from_obj(network_connection_obj.get_Creation_Time())
        network_connection_.destination_ip_address = Address.from_obj(network_connection_obj.get_Destination_IP_Address())
        network_connection_.destination_port = Port.from_obj(network_connection_obj.get_Destination_Port())
        network_connection_.source_ip_address = Address.from_obj(network_connection_obj.get_Source_IP_Address())
        network_connection_.source_port = Port.from_obj(network_connection_obj.get_Source_Port())
        network_connection_.tcp_state = String.from_obj(network_connection_obj.get_TCP_State())

        return network_connection_

class ImageInfo(cybox.Entity):
    def __init__(self, file_name = None, command_line = None):
        self.file_name = file_name
        self.command_line = command_line
        self.current_directory = None
        self.path = None
    
    def to_obj(self):
        image_info_obj = process_binding.ImageInfoType()

        if self.file_name is not None: image_info_obj.set_File_Name(self.file_name.to_obj())
        if self.command_line is not None: image_info_obj.set_Command_Line(self.command_line.to_obj()) 
        if self.current_directory is not None: image_info_obj.set_Current_Directory(self.current_directory.to_obj()) 
        if self.path is not None: image_info_obj.Path(self.path.to_obj()) 

        return image_info_obj

    def to_dict(self):
        image_info_dict = {}

        if self.file_name is not None: image_info_dict['filename'] = self.file_name.to_dict()
        if self.command_line is not None: image_info_dict['command_line'] = self.command_line.to_dict()
        if self.current_directory is not None: image_info_dict['current_directory'] = self.current_directory.to_dict()
        if self.path is not None: image_info_dict['path'] = self.path.to_dict()

        return image_info_dict

    @staticmethod
    def from_dict(image_info_dict):
        if not image_info_dict:
            return None

        image_info_ = ImageInfo()
        image_info_.file_name = String.from_dict(image_info_dict.get('file_name'))
        image_info_.command_line = String.from_dict(image_info_dict.get('command_line'))
        image_info_.current_directory = String.from_dict(image_info_dict.get('current_directory'))
        image_info_.path = String.from_dict(image_info_dict.get('path'))

        return image_info_

    @staticmethod
    def from_obj(image_info_obj):
        if not image_info_obj:
            return None

        image_info_ = ImageInfo()
        image_info_.file_name = String.from_obj(image_info_obj.get_File_Name())
        image_info_.command_line = String.from_dict(image_info_obj.get_Command_Line())
        image_info_.current_directory = String.from_dict(image_info_obj.get_Current_Directory())
        image_info_.path = String.from_dict(image_info_obj.get_Path())

        return image_info_