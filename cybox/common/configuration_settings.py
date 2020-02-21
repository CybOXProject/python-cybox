# Copyright (c) 2020, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from mixbox import entities, fields

import cybox.bindings.cybox_common as common_binding


class ConfigurationSetting(entities.Entity):
    _binding = common_binding
    _binding_class = common_binding.ConfigurationSettingType
    _namespace = 'http://cybox.mitre.org/common-2'

    item_name = fields.TypedField("Item_Name")
    item_value = fields.TypedField("Item_Value")
    item_type = fields.TypedField("Item_Type")
    item_description = fields.TypedField("Item_Description")


class ConfigurationSettings(entities.Entity):
    _binding = common_binding
    _binding_class = common_binding.ConfigurationSettingsType
    _namespace = 'http://cybox.mitre.org/common-2'

    configuration_setting = fields.TypedField("Configuration_Setting", ConfigurationSetting, multiple=True)
