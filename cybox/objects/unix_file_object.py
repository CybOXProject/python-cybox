# Copyright (c) 2020, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from mixbox import fields

import cybox.bindings.unix_file_object as unix_file_binding
from cybox.common import String, UnsignedLong
from cybox.objects.file_object import File, FilePermissions


def _validate_unix_type(instance, value):
    allowed = instance._ALLOWED_VALUES
    if not value:
        return
    elif not allowed:
        return
    elif value in allowed:
        return
    else:
        error = "Value must be one of {allowed}. Received '{value}'"
        error = error.format(**locals())
        raise ValueError(error)


class UnixFilePermissions(FilePermissions):
    _binding = unix_file_binding
    _binding_class = unix_file_binding.UnixFilePermissionsType
    _namespace = "http://cybox.mitre.org/objects#UnixFileObject-2"

    suid = fields.BooleanField("suid")
    sgid = fields.BooleanField("sgid")
    uread = fields.BooleanField("uread")
    uwrite = fields.BooleanField("uwrite")
    uexec = fields.BooleanField("uexec")
    gread = fields.BooleanField("gread")
    gwrite = fields.BooleanField("gwrite")
    gexec = fields.BooleanField("gexec")
    oread = fields.BooleanField("oread")
    owrite = fields.BooleanField("owrite")
    oexec = fields.BooleanField("oexec")


class UnixFile(File):
    _binding = unix_file_binding
    _binding_class = unix_file_binding.UnixFileObjectType
    _namespace = "http://cybox.mitre.org/objects#UnixFileObject-2"
    _XSI_NS = "UnixFileObj"
    _XSI_TYPE = "UnixFileObjectType"

    TYPE_REGULAR_FILE = "regularfile"
    TYPE_DIRECTORY = "directory"
    TYPE_SOCKET = "socket"
    TYPE_SYMBOLIC_LINK = "symboliclink"
    TYPE_BLOCK_SPECIAL_FILE = "blockspecialfile"
    TYPE_CHARACTER_SPECIAL_FILE = "characterspecialfile"

    _ALLOWED_VALUES = (
        TYPE_REGULAR_FILE,
        TYPE_DIRECTORY,
        TYPE_SOCKET,
        TYPE_SYMBOLIC_LINK,
        TYPE_BLOCK_SPECIAL_FILE,
        TYPE_CHARACTER_SPECIAL_FILE
    )

    group_owner = fields.TypedField("Group_Owner", String)
    inode = fields.TypedField("INode", UnsignedLong)
    type_ = fields.TypedField("Type", String, preset_hook=_validate_unix_type)

    # Override abstract types
    permissions = fields.TypedField('Permissions', UnixFilePermissions)

    @property
    def privilege_list(self):
        return self.permissions

    @privilege_list.setter
    def privilege_list(self, value):
        self.permissions = value
