import maec_bundle_3_0 as maecbundle
import cybox.process_object_1_3 as cybox_process_object
import cybox_helper.objects.port_object as maec_port_object
import cybox_helper.objects.address_object as maec_address_object

class process_object:
    def __init__(self, id):
        self.id = id
        
    def build_object(self, process_attributes):
        cybox_object = maecbundle.cybox_core_1_0.AssociatedObjectType(id=self.id, type_='Process')
        proc_object = cybox_process_object.ProcessObjectType()
        proc_object.set_anyAttributes_({'xsi:type' : 'ProcessObj:ProcessObjectType'})
        
        image_info = cybox_process_object.ImageInfoType()
        for key, value in process_attributes.items():
            if key == 'name':
                continue
            elif key == 'filename' and self.__value_test(value):
                proc_object.set_Path(maecbundle.cybox_common_types_1_0.StringObjectAttributeType(datatype='String',valueOf_=maecbundle.quote_xml(value)))
            elif key == 'command_line' and self.__value_test(value):
                image_info.set_Command_Line(maecbundle.cybox_common_types_1_0.StringObjectAttributeType(datatype='String',valueOf_=maecbundle.quote_xml(value)))
            elif key == 'pid' and self.__value_test(value):
                proc_object.set_PID(maecbundle.cybox_common_types_1_0.UnsignedIntegerObjectAttributeType(datatype='UnsignedInt', valueOf_=value))
            elif key == 'parentpid' and self.__value_test(value):
                proc_object.set_Parent_PID(maecbundle.cybox_common_types_1_0.UnsignedIntegerObjectAttributeType(datatype='UnsignedInt', valueOf_=value))
            elif key == 'child_pid_list':
                child_list = cybox_process_object.ChildPIDListType()
                for id in value:
                    child_list.add_Child_PID(maecbundle.cybox_common_types_1_0.UnsignedIntegerObjectAttributeType(datatype='UnsignedInt', valueOf_=id))
                proc_object.set_Child_PID_List(child_list)
            elif key == 'argument_list':
                arg_list = []
                for arg in value:
                    arg_list.append(maecbundle.cybox_common_types_1_0.StringObjectAttributeType(datatype='String',valueOf_=maecbundle.quote_xml(arg)))
                argument_list = cybox_process_object.ArgumentListType()
                argument_list.set_Argument(arg_list)
                proc_object.set_Argument_List(argument_list)
            elif key == 'environment_variable_list':
                env_list = maecbundle.cybox_common_types_1_0.EnvironmentVariableListType()
                for env_name, env_value in value.items():
                    env_var = maecbundle.cybox_common_types_1_0.EnvironmentVariableType(
                        Name=maecbundle.cybox_common_types_1_0.StringObjectAttributeType(datatype='String',valueOf_=maecbundle.quote_xml(env_name)),
                        Value=maecbundle.cybox_common_types_1_0.StringObjectAttributeType(datatype='String',valueOf_=maecbundle.quote_xml(env_value))
                    )
                    env_list.add_Environment_Variable(env_var)
                proc_object.set_Environment_Variable_List(env_list)
            elif key == 'port_list':
                port_list = cybox_process_object.PortListType()
                for port_dict in value:
                    portobj = maec_port_object.port_object.cybox_port_from_dict(port_dict)
                    port_list.add_Port(portobj)
                proc_object.set_Post_List(port_list)
            elif key == 'network_connection_list':
                conn_list = cybox_process_object.NetworkConnectionListType()
                for conn_dict in value:
                    connobj = cybox_process_object.NetworkConnectionType()
                    for conn_key, conn_value in conn_dict.items():
                        if conn_key == 'creation_time' and self.__value_test(conn_value):
                            connobj.set_Creation_Time(maecbundle.cybox_common_types_1_0.DateTimeObjectAttributeType(datatype='DateTime',valueOf_=maecbundle.quote_xml(conn_value)))
                        elif conn_key == 'destination_ip_address' and self.__value_test(conn_value):
                            connobj.set_Destination_Address(maec_address_object.address_object.cybox_address_from_dict(conn_value))
                        elif conn_key == 'destination_port' and self.__value_test(conn_value):
                            connobj.set_Source_Port(maec_port_object.port_object.cybox_port_from_dict(conn_value))
                        elif conn_key == 'source_ip_address' and self.__value_test(conn_value):
                            connobj.set_Source_Address(maec_address_object.address_object.cybox_address_from_dict(conn_value))
                        elif conn_key == 'source_port' and self.__value_test(conn_value):
                            connobj.set_Source_Port(maec_port_object.port_object.cybox_port_from_dict(conn_value))
                        elif conn_key == 'tcp_state' and self.__value_test(conn_value):
                            cybox_process_object.ConnectionStateType(datatype='String',valueOf_=conn_value)
                    conn_list.add_Network_Connection(connobj)
            elif key == 'string_list':
                string_list = maecbundle.cybox_common_types_1_0.ExtractedStringsType()
                for str_dict in value:
                    strobj = maecbundle.cybox_common_types_1_0.ExtractedStringType()
                    for str_key, str_value in str_dict.items():
                        if str_key == 'string_value' and self.__value_test(str_value):
                            strobj.set_String_Value(maecbundle.cybox_common_types_1_0.StringObjectAttributeType(datatype='String',valueOf_=maecbundle.quote_xml(str_value)))
                        elif str_key == 'hashes' and self.__value_test(str_value):
                            hash_list = maecbundle.cybox_common_types_1_0.HashListType()
                            for hash_dict in value:
                                hashobj = maecbundle.cybox_common_types_1_0.HashType()
                                for hash_key, hash_value in hash_dict:
                                    if hash_key == 'type' and self.__value_test(hash_value):
                                        pass
                                    elif hash_key == 'other_type' and self.__value_test(hash_value):
                                        hashobj.set_Other_Type(maecbundle.cybox_common_types_1_0.StringObjectAttributeType(datatype='String',valueOf_=maecbundle.quote_xml(hash_value)))
                                    elif hash_key == 'simple_hash_value' and self.__value_test(hash_value):
                                        hashobj.set_Simple_Hash_Value(maecbundle.cybox_common_types_1_0.SimpleHashValueType(valueOf_=maecbundle.quote_xml(hash_value)))
                                    elif hash_key == 'fuzzy_hash_value' and self.__value_test(hash_value):
                                        hashobj.set_Fuzzy_Hash_Value(maecbundle.cybox_common_types_1_0.SimpleHashValueType(valueOf_=maecbundle.quote_xml(hash_value)))
                                    elif hash_key == 'fuzzy_hash_structure' and self.__value_test(hash_value):
                                        struture = maecbundle.cybox_common_types_1_0.FuzzyHashStructureType()
                                        for struct_key, struct_value in hash_value:
                                            if struct_key == 'block_size':
                                                pass #TODO
                                            elif struct_key == 'block_type':
                                                pass #TODO
                                hash_list.add_Hash(hashobj)
                        elif str_key == 'address' and self.__value_test(str_value):
                            pass #TODO
                        elif str_key == 'length' and self.__value_test(str_value):
                            maecbundle.cybox_common_types_1_0.PositiveIntegerObjectAttributeType(datatype='PositiveInteger',valueOf_=maecbundle.quote_xml(str_value))
                        elif str_key == 'language' and self.__value_test(str_value):
                            strobj.set_Language(maecbundle.cybox_common_types_1_0.StringObjectAttributeType(datatype='String',valueOf_=maecbundle.quote_xml(str_value)))
                        elif str_key == 'english_translation' and self.__value_test(str_value):
                            pass
                    string_list.add_String(str)
            elif key == 'username' and self.__value_test(value):
                proc_object.set_Username(maecbundle.cybox_common_types_1_0.StringObjectAttributeType(datatype='String',valueOf_=maecbundle.quote_xml(value)))
            elif key == 'creation_time' and self.__value_test(value):
                proc_object.set_Creation_Time(maecbundle.cybox_common_types_1_0.DateTimeObjectAttributeType(datatype='DateTime',valueOf_=maecbundle.quote_xml(value)))
            elif key == 'start_time' and self.__value_test(value):
                proc_object.set_Start_Time(maecbundle.cybox_common_types_1_0.DateTimeObjectAttributeType(datatype='DateTime',valueOf_=maecbundle.quote_xml(value)))
            elif key == 'kernel_time' and self.__value_test(value):
                proc_object.set_Kernel_Time(maecbundle.cybox_common_types_1_0.DurationObjectAttributeType(datatype='Duration',valueOf_=maecbundle.quote_xml(value)))            
            elif key == 'user_time' and self.__value_test(value):
                proc_object.set_User_Time(maecbundle.cybox_common_types_1_0.DurationObjectAttributeType(datatype='Duration',valueOf_=maecbundle.quote_xml(value)))            
            elif key == 'association':
                cybox_object.set_association_type(value)
            elif key == 'av_classifications':
                cybox_object.set_Domain_specific_Object_Attributes(value)
                
        if image_info.hasContent_():
            proc_object.set_Image_Info(image_info)
        
        if proc_object.hasContent_():                                                                    
            cybox_object.set_Defined_Object(proc_object)
        
        return cybox_object