import cybox.utils as utils
import cybox.bindings.cybox_common_types_binding_1_0 as common_types_binding_binding
import cybox.bindings.win_executable_file_object_1_3 as win_executable_file_binding
from cybox.common.baseobjectattribute import Base_Object_Attribute
from cybox.objects.win_file_object import Win_File

class Win_Executable_File:
    def __init__(self):
        pass
        
    @classmethod
    def object_from_dict(cls, win_executable_file_dict):
        """Create the Win Executable File Object object representation from an input dictionary"""
        win_executable_file_obj = Win_File.object_from_dict(win_executable_file_dict, win_executable_file_binding.WindowsExecutableFileObjectType())
        win_executable_file_obj.set_anyAttributes_({'xsi:type' : 'WinExecutableFileObj:WindowsExecutableFileObjectType'})

        for key, value in win_executable_file_dict.items():
            if key == 'peak_code_entropy':
                entropy_obj = win_executable_file_binding.EntropyType()
                for entropy_key, entropy_value in value.items():
                    if entropy_key == 'value' and utils.test_value(entropy_value):
                        entropy_obj.set_Value(Base_Object_Attribute.object_from_dict(common_types_binding.FloatObjectAttributeType(datatype='Float'), entropy_value))
                    elif entropy_key == 'min' and utils.test_value(entropy_value):
                        entropy_obj.set_Min(Base_Object_Attribute.object_from_dict(common_types_binding.FloatObjectAttributeType(datatype='Float'), entropy_value))
                    elif entropy_key == 'max' and utils.test_value(entropy_value):
                        entropy_obj.set_Max(Base_Object_Attribute.object_from_dict(common_types_binding.FloatObjectAttributeType(datatype='Float'), entropy_value))
                if entropy_obj.hasContent_():
                    win_executable_file_obj.set_Peak_Code_Entropy(entropy_obj)
            elif key == 'pe_attributes':
                pe_attributes_obj = cls.__pe_attributes_obj_from_dict(value)
                if pe_attributes_obj.hasContent_() : win_executable_file_obj.set_PE_Attributes(pe_attributes_obj)
        
        return win_executable_file_obj

    @classmethod
    def dict_from_object(cls, win_executable_file_obj):
        """Parse and return a dictionary for a Win Executable File Object object"""
        win_executable_file_dict = {}
        if win_executable_file_obj.get_Peak_Code_Entropy() is not None:
            entropy_obj = win_executable_file_obj.get_Peak_Code_Entropy()
            entropy_dict = {}
            if entropy_obj.get_Value() is not None: entropy_dict['value'] = Base_Object_Attribute.dict_from_object(entropy_obj.get_Value())
            if entropy_obj.get_Max() is not None: entropy_dict['max'] = Base_Object_Attribute.dict_from_object(entropy_obj.get_Max())
            if entropy_obj.get_Min() is not None: entropy_dict['min'] = Base_Object_Attribute.dict_from_object(entropy_obj.get_Min())
            win_executable_file_dict['peak_code_entropy'] = entropy_dict
        if win_executable_file_obj.get_PE_Attributes() is not None: win_executable_file_dict['pe_attributes'] = cls.__pe_attributes_dict_from_obj(win_executable_file_obj.get_PE_Attributes())
        return win_executable_file_dict

    @classmethod
    def __pe_attributes_dict_from_obj(cls, pe_attributes_obj):
        pe_attributes_dict = {}
        if pe_attributes_obj.get_Base_Address() is not None: pe_attributes_dict['base_address'] = Base_Object_Attribute.dict_from_object(pe_attributes_obj.get_Base_Address())
        if pe_attributes_obj.get_Exports() is not None: pe_attributes_dict['exports'] = cls.__exports_dict_from_obj(pe_attributes_obj.get_Exports())
        return pe_attributes_dict 

    @classmethod
    def __pe_attributes_obj_from_dict(cls, pe_attributes_dict):
        pe_attributes_obj = win_executable_file_binding.PEAttributesType()
        for pe_attributes_key, pe_attributes_value in value.items():
            if pe_attributes_key == 'base_address' and utils.test_value(pe_attributes_value):
                pe_attributes.set_Base_Address(Base_Object_Attribute.object_from_dict(common_types_binding.HexBinaryObjectAttributeType(datatype='hexBinary'), pe_attributes_value))
            elif pe_attributes_key == 'exports':
                exports_obj = cls.__exports_obj_from_dict(value)
                if exports_obj.hasContent_() : pe_attributes.set_Exports(exports_obj)
        return pe_attributes_obj

    @classmethod
    def __exports_obj_from_dict(cls, exports_dict):
        exports_obj = win_executable_file_binding.PEExportsType()
        for key, value in exports_dict.items():
            if key == 'exported_functions':
                exported_functions = win_executable_file_binding.PEExportedFunctionsType()
                for exported_function in value:
                    xported_function = win_executable_file_binding.PEExportedFunctionType()
                    for exported_function_key, exported_function_value in exported_function.items():
                        if exported_function_key == 'function_name' and utils.test_value(exported_function_value):
                            xported_function.set_Function_Name(Base_Object_Attribute.object_from_dict(common_types_binding.StringObjectAttributeType(datatype='String'), exported_function_value))
                        elif exported_function_key == 'entry_point' and utils.test_value(exported_function_value):
                            xported_function.set_Entry_Point(cBase_Object_Attribute.object_from_dict(ommon_types_binding.HexBinaryObjectAttributeType(datatype='hexBinary'), exported_function_value))
                        elif exported_function_key == 'ordinal' and utils.test_value(exported_function_value):
                            xported_function.set_Ordinal(Base_Object_Attribute.object_from_dict(common_types_binding.NonNegativeIntegerObjectAttributeType(datatype='NonNegativeInteger'), exported_function_value))
                    if xported_function.hasContent_():
                        exported_functions.add_Exported_Function(xported_function)
                if exported_functions.hasContent_():
                    exports.set_Exported_Functions(exported_functions)
            elif key == 'exports_time_stamp' and utils.test_value(value):
                exports.set_Exports_Time_stamp(Base_Object_Attribute.object_from_dict(common_types_binding.DateTimeObjectAttributeType(datatype='DateTime'), exported_function_value))
            elif key == 'number_of_addresses' and utils.test_value(value):
                exports.set_Number_Of_Addresses(Base_Object_Attribute.object_from_dict(common_types_binding.LongObjectAttributeType(datatype='Long'), exported_function_value))
            elif key == 'number_of_names' and utils.test_value(value):
                exports.set_Number_Of_Names(Base_Object_Attribute.object_from_dict(common_types_binding.LongObjectAttributeType(datatype='Long'), exported_function_value))
        return exports_obj

    @classmethod
    def __exports_dict_from_obj(cls, exports_obj):
        exports_dict = {}
        if exports_obj.get_Exported_Functions() is not None:
            exported_functions = []
            for exported_function_obj in exports_obj.get_Exported_Functions().get_Exported_Function():
                exported_function_dict = {}
                if exported_function_obj.get_Function_Name() is not None: exported_function_dict['function_name'] = Base_Object_Attribute.dict_from_object(exported_function_obj.get_Function_Name())
                if exported_function_obj.get_Entry_Point() is not None: exported_function_dict['entry_point'] = Base_Object_Attribute.dict_from_object(exported_function_obj.get_Entry_Point())
                if exported_function_obj.get_Ordinal() is not None: exported_function_dict['ordinal'] = Base_Object_Attribute.dict_from_object(exported_function_obj.get_Ordinal())
                exported_functions.append(exported_function_dict)
            exports_dict['exported_functions'] = exported_functions
        if exports_obj.get_Exports_Time_Stamp() is not None: exports_dict['exports_time_stamp'] = Base_Object_Attribute.dict_from_object(exports_obj.get_Exports_Time_Stamp())
        if exports_obj.get_Number_Of_Addresses() is not None: exports_dict['number_of_addresses'] = Base_Object_Attribute.dict_from_object(exports_obj.get_Number_Of_Addresses())
        if exports_obj.get_Number_Of_Names() is not None: exports_dict['number_of_names'] = Base_Object_Attribute.dict_from_object(exports_obj.get_Number_Of_Names())
        return exports_dict