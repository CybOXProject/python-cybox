import maec_bundle_3_0 as maecbundle
import cybox.win_executable_file_object_1_3 as cybox_win_executable_file_object

class win_executable_file_object:
    def __init__(self, id):
        self.id = id
        
    def build_object(self, win_executable_file_attributes):
        cybox_object = maecbundle.cybox_core_1_0.AssociatedObjectType(id=self.generator.generate_obj_id(), type_='File')
        win_executable_file_obj = cybox_win_executable_file_object.WindowsExecutableFileObjectType()
        win_executable_file_obj.set_anyAttributes_({'xsi:type' : 'WinExecutableFileObj:WindowsExecutableFileObjectType'})
        pe_attributes = cybox_win_executable_file_object.PEAttributesType()

        for key, value in win_executable_file_attributes.items():
            if key.lower() == 'peak_code_entropy' and self.__value_test(value):
                entropytype = cybox_win_executable_file_object.EntropyType()
                for entropy_key, entropy_value in value.items():
                    if entropy_key.lower() == 'value' and self.__value_test(entropy_value):
                        entropytype.set_Value(maecbundle.cybox_common_types_1_0.FloatObjectAttributeType(datatype='Float',valueOf_=entropy_value))
                    elif entropy_key.lower() == 'min' and self.__value_test(entropy_value):
                        entropytype.set_Min(maecbundle.cybox_common_types_1_0.FloatObjectAttributeType(datatype='Float',valueOf_=entropy_value))
                    elif entropy_key.lower() == 'max' and self.__value_test(entropy_value):
                        entropytype.set_Max(maecbundle.cybox_common_types_1_0.FloatObjectAttributeType(datatype='Float',valueOf_=entropy_value))
                if entropytype.hasContent_():
                    win_executable_file_obj.set_Peak_Code_Entropy(entropytype)
            elif key.lower() == 'pe_attributes' and self.__value_test(value):
                pe_attributes = cybox_win_executable_file_object.PEAttributesType()
                for pe_attributes_key, pe_attributes_value in value.items():
                    if pe_attributes_key.lower() == 'base_address' and self.__value_test(pe_attributes_value):
                        pe_attributes.set_Base_Address(maecbundle.cybox_common_types_1_0.HexBinaryObjectAttributeType(datatype='hexBinary',valueOf_=pe_attributes_value))
                    elif pe_attributes_key.lower() == 'exports' and self.__value_test(pe_attributes_value):
                        exports = cybox_win_executable_file_object.PEExportsType()
                        for export_key, export_value in pe_attributes_value.items():
                            if export_key.lower() == 'exported_functions' and self.__value_test(export_value):
                                exported_functions = cybox_win_executable_file_object.PEExportedFunctionsType()
                                for exported_function in export_value:
                                    xported_function = cybox_win_executable_file_object.PEExportedFunctionType()
                                    for exported_function_key, exported_function_value in exported_function.items():
                                        if exported_function_key.lower() == 'function_name' and self.__value_test(exported_function_value):
                                            xported_function.set_Function_Name(maecbundle.cybox_common_types_1_0.StringObjectAttributeType(datatype='String',valueOf_=maecbundle.quote_xml(exported_function_value)))
                                        elif exported_function_key.lower() == 'entry_point' and self.__value_test(exported_function_value):
                                            xported_function.set_Entry_Point(maecbundle.cybox_common_types_1_0.HexBinaryObjectAttributeType(datatype='hexBinary',valueOf_=exported_function_value))
                                        elif exported_function_key.lower() == 'ordinal' and self.__value_test(exported_function_value):
                                            xported_function.set_Ordinal(maecbundle.cybox_common_types_1_0.NonNegativeIntegerObjectAttributeType(datatype='NonNegativeInteger',valueOf_=exported_function_value))
                                    if xported_function.hasContent_():
                                        exported_functions.add_Exported_Function(xported_function)
                                if exported_functions.hasContent_():
                                    exports.set_Exported_Functions(exported_functions)
                            elif export_key.lower() == 'exports_time_stamp' and self.__value_test(export_value):
                                exports.set_Exports_Time_stamp(maecbundle.cybox_common_types_1_0.DateTimeObjectAttributeType(datatype='DateTime',valueOf_=exported_function_value))
                            elif export_key.lower() == 'number_of_addresses' and self.__value_test(export_value):
                                exports.set_Number_Of_Addresses(maecbundle.cybox_common_types_1_0.LongObjectAttributeType(datatype='Long',valueOf_=exported_function_value))
                            elif export_key.lower() == 'number_of_names' and self.__value_test(export_value):
                                exports.set_Number_Of_Names(maecbundle.cybox_common_types_1_0.LongObjectAttributeType(datatype='Long',valueOf_=exported_function_value))
                        if exports.hasContent_():
                            pe_attributes.set_Exports(exports)
            elif key == 'association':
                cybox_object.set_association_type(value)
        
        if pe_attributes.hasContent_():
            win_executable_file_obj.set_PE_Attributes(pe_attributes)
        if win_executable_file_obj.hasContent_():
            cybox_object.set_Defined_Object(win_executable_file_obj)
        
        return cybox_object