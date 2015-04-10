# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import cybox
import cybox.bindings.cybox_common as common_binding
from cybox.common import PatternFieldGroup
from cybox.utils import normalize_to_xml, denormalize_from_xml


class VocabField(cybox.TypedField):
    """TypedField subclass for VocabString fields.

    """
    def __init__(self, *args, **kwargs):
        """Intercepts the __init__() call to TypedField.

        Set the type that will be used in from_dict and from_obj calls to
        :class:`VocabString`.

        Set the type that will be used in ``__set__`` for casting as the
        original ``type_`` argument, or :class:`VocabString` if no `type_`
        argument was provided.

        """
        super(VocabField, self).__init__(*args, **kwargs)

        if self.type_:
            self.__vocab_impl = self.type_
        else:
            self.__vocab_impl = VocabString

        self.type_ = VocabString  # Force this

    def __set__(self, instance, value):
        """Overrides cybox.TypedField.__set__()."""
        type_ = self.__vocab_impl

        if value is None:
            instance._fields[self.name] = None
        elif isinstance(value, VocabString):
            instance._fields[self.name] = value
        elif type_._try_cast:  # noqa
            value = type_(value)
            instance._fields[self.name] = value
        else:
            error_fmt = "%s must be a %s, not a %s"
            error = error_fmt % (self.name, self.type_, type(value))
            raise ValueError(error)

        if self.callback_hook:
            self.callback_hook(instance)


class VocabString(PatternFieldGroup, cybox.Entity):
    _namespace = 'http://cybox.mitre.org/default_vocabularies-2'
    # All subclasses should override this
    _XSI_TYPE = None
    _ALLOWED_VALUES = None
    _binding = common_binding
    _binding_class = common_binding.ControlledVocabularyStringType

    def __init__(self, value=None):
        super(VocabString, self).__init__()
        self.value = value
        self.xsi_type = self._XSI_TYPE

        self.vocab_name = None
        self.vocab_reference = None

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, v):
        allowed = self._ALLOWED_VALUES

        if not v:
            self._value = None
        elif allowed and (v not in allowed):
            error = "Value must be one of {0}. Received '{1}'"
            error = error.format(allowed, v)
            raise ValueError(error)
        else:
            self._value = v

    def __str__(self):
        return str(self.value)

    def __eq__(self, other):
        # Check to make sure the values are identical.
        if isinstance(other, VocabString):
            other = other.value

        return other == self.value

    def is_plain(self):
        """Whether the VocabString can be represented as a single value.

        """
        return (
            self.xsi_type is None and
            self.vocab_name is None and
            self.vocab_reference is None and
            PatternFieldGroup.is_plain(self)
        )

    @staticmethod
    def lookup_class(xsi_type):
        if not xsi_type:
            return VocabString

        for (k, v) in _VOCAB_MAP.iteritems():
            # TODO: for now we ignore the prefix and just check for
            # a partial match
            if xsi_type in k:
                return v

        return VocabString

    def to_obj(self, return_obj=None, ns_info=None):
        self._collect_ns_info(ns_info)

        if not return_obj:
            return_obj = self._binding_class()
            
        return_obj.valueOf_ = normalize_to_xml(self.value, self.delimiter)
        return_obj.xsi_type = self.xsi_type

        if self.vocab_name is not None:
            return_obj.vocab_name = self.vocab_name
        if self.vocab_reference is not None:
            return_obj.vocab_reference = self.vocab_reference

        PatternFieldGroup.to_obj(self, return_obj=return_obj, ns_info=ns_info)

        return return_obj



    def to_dict(self):
        if self.is_plain():
            return self.value

        vocab_dict = {}
        if self.value is not None:
            vocab_dict['value'] = self.value
        if self.xsi_type:
            vocab_dict['xsi:type'] = self.xsi_type
        if self.vocab_name is not None:
            vocab_dict['vocab_name'] = self.vocab_name
        if self.vocab_reference is not None:
            vocab_dict['vocab_reference'] = self.vocab_reference

        PatternFieldGroup.to_dict(self, vocab_dict)

        return vocab_dict

    @classmethod
    def from_obj(cls, vocab_obj, return_obj=None):
        if not vocab_obj:
            return None

        if not return_obj:
            klass = VocabString.lookup_class(vocab_obj.xsi_type)
            return_obj = klass()

        # xsi_type should be set automatically by the class's constructor.

        return_obj.vocab_name = vocab_obj.vocab_name
        return_obj.vocab_reference = vocab_obj.vocab_reference
        return_obj.xsi_type = vocab_obj.xsi_type

        PatternFieldGroup.from_obj(vocab_obj, return_obj)

        # We need to check for a non-default delimiter before trying to parse
        # the value.
        return_obj.value = denormalize_from_xml(
            value=vocab_obj.valueOf_,
            delimiter=return_obj.delimiter
        )

        return return_obj

    @classmethod
    def from_dict(cls, vocab_dict, return_obj=None):
        if not vocab_dict:
            return None

        if not return_obj:
            if isinstance(vocab_dict, dict):
                klass = VocabString.lookup_class(vocab_dict.get('xsi:type'))
                return_obj = klass()
            else:
                return_obj = cls()

        # In case this is a "plain" string, just set it.
        if not isinstance(vocab_dict, dict):
            return_obj.value = vocab_dict
        else:
            return_obj.xsi_type = vocab_dict.get('xsi:type', cls._XSI_TYPE)
            return_obj.value = vocab_dict.get('value')
            return_obj.vocab_name = vocab_dict.get('vocab_name')
            return_obj.vocab_reference = vocab_dict.get('vocab_reference')

            PatternFieldGroup.from_dict(vocab_dict, return_obj)

        return return_obj


class EventType(VocabString):
    _namespace = 'http://cybox.mitre.org/default_vocabularies-2'
    _XSI_TYPE = 'cyboxVocabs:EventTypeVocab-1.0.1'
    _VOCAB_VERSION = '1.0.1'
    _ALLOWED_VALUES = (
        'File Ops (CRUD)',
        'Registry Ops',
        'Memory Ops',
        'Process Mgt',
        'Thread Mgt',
        'Service Mgt',
        'Session Mgt',
        'API Calls',
        'Port Scan',
        'IP Ops',
        'DNS Lookup Ops',
        'Socket Ops',
        'IPC',
        'Configuration Management',
        'User/Password Mgt',
        'Account Ops (App Layer)',
        'HTTP Traffic',
        'App Layer Traffic',
        'Packet Traffic',
        'Data Flow',
        'Anomaly Events',
        'Technical Compliance',
        'Procedural Compliance',
        'GUI/KVM',
        'Autorun',
        'USB/Media Detection',
        'SQL',
        'DHCP',
        'Redirection',
        'Authentication Ops',
        'Authorization (ACL)',
        'Privilege Ops',
        'Basic System Ops',
        'Signature Detection',
        'Auto-update Ops',
        'Application Logic',
        'Email Ops',
    )
    TERM_APP_LAYER_TRAFFIC = 'App Layer Traffic'
    TERM_IP_OPS = 'IP Ops'
    TERM_FILE_OPS_CRUD = 'File Ops (CRUD)'
    TERM_BASIC_SYSTEM_OPS = 'Basic System Ops'
    TERM_SIGNATURE_DETECTION = 'Signature Detection'
    TERM_ACCOUNT_OPS_APP_LAYER = 'Account Ops (App Layer)'
    TERM_AUTORUN = 'Autorun'
    TERM_DATA_FLOW = 'Data Flow'
    TERM_PORT_SCAN = 'Port Scan'
    TERM_SERVICE_MGT = 'Service Mgt'
    TERM_HTTP_TRAFFIC = 'HTTP Traffic'
    TERM_PROCEDURAL_COMPLIANCE = 'Procedural Compliance'
    TERM_REGISTRY_OPS = 'Registry Ops'
    TERM_TECHNICAL_COMPLIANCE = 'Technical Compliance'
    TERM_AUTHENTICATION_OPS = 'Authentication Ops'
    TERM_DNS_LOOKUP_OPS = 'DNS Lookup Ops'
    TERM_AUTO_UPDATE_OPS = 'Auto-update Ops'
    TERM_EMAIL_OPS = 'Email Ops'
    TERM_CONFIGURATION_MANAGEMENT = 'Configuration Management'
    TERM_PRIVILEGE_OPS = 'Privilege Ops'
    TERM_ANOMALY_EVENTS = 'Anomaly Events'
    TERM_AUTHORIZATION_ACL = 'Authorization (ACL)'
    TERM_MEMORY_OPS = 'Memory Ops'
    TERM_PROCESS_MGT = 'Process Mgt'
    TERM_APPLICATION_LOGIC = 'Application Logic'
    TERM_SESSION_MGT = 'Session Mgt'
    TERM_THREAD_MGT = 'Thread Mgt'
    TERM_IPC = 'IPC'
    TERM_PACKET_TRAFFIC = 'Packet Traffic'
    TERM_USER_PASSWORD_MGT = 'User/Password Mgt'
    TERM_REDIRECTION = 'Redirection'
    TERM_USB_MEDIA_DETECTION = 'USB/Media Detection'
    TERM_GUI_KVM = 'GUI/KVM'
    TERM_SQL = 'SQL'
    TERM_DHCP = 'DHCP'
    TERM_API_CALLS = 'API Calls'
    TERM_SOCKET_OPS = 'Socket Ops'


class ActionType(VocabString):
    _namespace = 'http://cybox.mitre.org/default_vocabularies-2'
    _XSI_TYPE = 'cyboxVocabs:ActionTypeVocab-1.0'
    _VOCAB_VERSION = '1.0'
    _ALLOWED_VALUES = (
        'Accept',
        'Access',
        'Add',
        'Alert',
        'Allocate',
        'Archive',
        'Assign',
        'Audit',
        'Backup',
        'Bind',
        'Block',
        'Call',
        'Change',
        'Check',
        'Clean',
        'Click',
        'Close',
        'Compare',
        'Compress',
        'Configure',
        'Connect',
        'Control',
        'Copy/Duplicate',
        'Create',
        'Decode',
        'Decompress',
        'Decrypt',
        'Deny',
        'Depress',
        'Detect',
        'Disconnect',
        'Download',
        'Draw',
        'Drop',
        'Encode',
        'Encrypt',
        'Enumerate',
        'Execute',
        'Extract',
        'Filter',
        'Find',
        'Flush',
        'Fork',
        'Free',
        'Get',
        'Hook',
        'Hide',
        'Impersonate',
        'Initialize',
        'Inject',
        'Install',
        'Interleave',
        'Join',
        'Kill',
        'Listen',
        'Load',
        'Lock',
        'Login/Logon',
        'Logout/Logoff',
        'Map',
        'Merge',
        'Modify',
        'Monitor',
        'Move',
        'Open',
        'Pack',
        'Pause',
        'Press',
        'Protect',
        'Quarantine',
        'Query',
        'Queue',
        'Raise',
        'Read',
        'Receive',
        'Release',
        'Rename',
        'Remove/Delete',
        'Replicate',
        'Restore',
        'Resume',
        'Revert',
        'Run',
        'Save',
        'Scan',
        'Schedule',
        'Search',
        'Send',
        'Set',
        'Shutdown',
        'Sleep',
        'Snapshot',
        'Start',
        'Stop',
        'Suspend',
        'Synchronize',
        'Throw',
        'Transmit',
        'Unblock',
        'Unhide',
        'Unhook',
        'Uninstall',
        'Unload',
        'Unlock',
        'Unmap',
        'Unpack',
        'Update',
        'Upgrade',
        'Upload',
        'Wipe/Destroy/Purge',
        'Write',
    )
    TERM_COPY_DUPLICATE = 'Copy/Duplicate'
    TERM_HIDE = 'Hide'
    TERM_MONITOR = 'Monitor'
    TERM_UNHIDE = 'Unhide'
    TERM_ACCESS = 'Access'
    TERM_DETECT = 'Detect'
    TERM_REPLICATE = 'Replicate'
    TERM_TRANSMIT = 'Transmit'
    TERM_RAISE = 'Raise'
    TERM_SCHEDULE = 'Schedule'
    TERM_MODIFY = 'Modify'
    TERM_UPDATE = 'Update'
    TERM_FREE = 'Free'
    TERM_DECOMPRESS = 'Decompress'
    TERM_INITIALIZE = 'Initialize'
    TERM_CHANGE = 'Change'
    TERM_EXECUTE = 'Execute'
    TERM_UNMAP = 'Unmap'
    TERM_UNLOAD = 'Unload'
    TERM_LOGIN_LOGON = 'Login/Logon'
    TERM_RELEASE = 'Release'
    TERM_CONTROL = 'Control'
    TERM_MOVE = 'Move'
    TERM_DECRYPT = 'Decrypt'
    TERM_KILL = 'Kill'
    TERM_CHECK = 'Check'
    TERM_INJECT = 'Inject'
    TERM_DISCONNECT = 'Disconnect'
    TERM_CREATE = 'Create'
    TERM_SEND = 'Send'
    TERM_SAVE = 'Save'
    TERM_LISTEN = 'Listen'
    TERM_FORK = 'Fork'
    TERM_RUN = 'Run'
    TERM_IMPERSONATE = 'Impersonate'
    TERM_THROW = 'Throw'
    TERM_PROTECT = 'Protect'
    TERM_JOIN = 'Join'
    TERM_RECEIVE = 'Receive'
    TERM_REVERT = 'Revert'
    TERM_UPLOAD = 'Upload'
    TERM_QUEUE = 'Queue'
    TERM_INTERLEAVE = 'Interleave'
    TERM_UPGRADE = 'Upgrade'
    TERM_BLOCK = 'Block'
    TERM_PACK = 'Pack'
    TERM_RENAME = 'Rename'
    TERM_SCAN = 'Scan'
    TERM_EXTRACT = 'Extract'
    TERM_RESUME = 'Resume'
    TERM_FIND = 'Find'
    TERM_DOWNLOAD = 'Download'
    TERM_QUERY = 'Query'
    TERM_PAUSE = 'Pause'
    TERM_COMPRESS = 'Compress'
    TERM_START = 'Start'
    TERM_ADD = 'Add'
    TERM_REMOVE_DELETE = 'Remove/Delete'
    TERM_ALLOCATE = 'Allocate'
    TERM_DRAW = 'Draw'
    TERM_CONFIGURE = 'Configure'
    TERM_GET = 'Get'
    TERM_PRESS = 'Press'
    TERM_UNINSTALL = 'Uninstall'
    TERM_DENY = 'Deny'
    TERM_CLICK = 'Click'
    TERM_BIND = 'Bind'
    TERM_FILTER = 'Filter'
    TERM_MERGE = 'Merge'
    TERM_UNHOOK = 'Unhook'
    TERM_SNAPSHOT = 'Snapshot'
    TERM_INSTALL = 'Install'
    TERM_BACKUP = 'Backup'
    TERM_ASSIGN = 'Assign'
    TERM_LOAD = 'Load'
    TERM_WRITE = 'Write'
    TERM_COMPARE = 'Compare'
    TERM_SET = 'Set'
    TERM_HOOK = 'Hook'
    TERM_CONNECT = 'Connect'
    TERM_SHUTDOWN = 'Shutdown'
    TERM_FLUSH = 'Flush'
    TERM_CLOSE = 'Close'
    TERM_OPEN = 'Open'
    TERM_ARCHIVE = 'Archive'
    TERM_DEPRESS = 'Depress'
    TERM_ENCRYPT = 'Encrypt'
    TERM_SEARCH = 'Search'
    TERM_DECODE = 'Decode'
    TERM_CALL = 'Call'
    TERM_ENCODE = 'Encode'
    TERM_WIPE_DESTROY_PURGE = 'Wipe/Destroy/Purge'
    TERM_MAP = 'Map'
    TERM_READ = 'Read'
    TERM_STOP = 'Stop'
    TERM_ALERT = 'Alert'
    TERM_UNPACK = 'Unpack'
    TERM_AUDIT = 'Audit'
    TERM_QUARANTINE = 'Quarantine'
    TERM_DROP = 'Drop'
    TERM_CLEAN = 'Clean'
    TERM_RESTORE = 'Restore'
    TERM_SUSPEND = 'Suspend'
    TERM_LOGOUT_LOGOFF = 'Logout/Logoff'
    TERM_SYNCHRONIZE = 'Synchronize'
    TERM_LOCK = 'Lock'
    TERM_ACCEPT = 'Accept'
    TERM_UNLOCK = 'Unlock'
    TERM_UNBLOCK = 'Unblock'
    TERM_SLEEP = 'Sleep'
    TERM_ENUMERATE = 'Enumerate'


class ActionObjectAssociationType(VocabString):
    _namespace = 'http://cybox.mitre.org/default_vocabularies-2'
    _XSI_TYPE = 'cyboxVocabs:ActionObjectAssociationTypeVocab-1.0'
    _VOCAB_VERSION = '1.0'
    _ALLOWED_VALUES = (
        'Initiating',
        'Affected',
        'Utilized',
        'Returned',
    )
    TERM_UTILIZED = 'Utilized'
    TERM_AFFECTED = 'Affected'
    TERM_RETURNED = 'Returned'
    TERM_INITIATING = 'Initiating'


class HashName(VocabString):
    _namespace = 'http://cybox.mitre.org/default_vocabularies-2'
    _XSI_TYPE = 'cyboxVocabs:HashNameVocab-1.0'
    _VOCAB_VERSION = '1.0'
    _ALLOWED_VALUES = (
        'MD5',
        'MD6',
        'SHA1',
        'SHA224',
        'SHA256',
        'SHA384',
        'SHA512',
        'SSDEEP',
    )
    TERM_SHA1 = 'SHA1'
    TERM_SHA224 = 'SHA224'
    TERM_SHA512 = 'SHA512'
    TERM_SHA384 = 'SHA384'
    TERM_SSDEEP = 'SSDEEP'
    TERM_SHA256 = 'SHA256'
    TERM_MD6 = 'MD6'
    TERM_MD5 = 'MD5'


class ActionArgumentName(VocabString):
    _namespace = 'http://cybox.mitre.org/default_vocabularies-2'
    _XSI_TYPE = 'cyboxVocabs:ActionArgumentNameVocab-1.0'
    _VOCAB_VERSION = '1.0'
    _ALLOWED_VALUES = (
        'API',
        'Application Name',
        'Database Name',
        'Privilege Name',
        'Proxy Name',
        'Proxy Bypass',
        'Creation Flags',
        'Flags',
        'Access Mode',
        'Share Mode',
        'Callback Address',
        'Source Address',
        'Destination Address',
        'Base Address',
        'Starting Address',
        'Size (bytes)',
        'Number of Bytes Per Send',
        'Control Parameter',
        'Host Name',
        'Function Name',
        'Function Address',
        'Options',
        'Transfer Flags',
        'Control Code',
        'APC Mode',
        'APC Address',
        'Base Address',
        'Protection',
        'Target PID',
        'Mapping Offset',
        'File Information Class',
        'Function Ordinal',
        'Function Name',
        'Hook Type',
        'Request Size',
        'Requested Version',
        'Service Type',
        'Service State',
        'Service Name',
        'Hostname',
        'Shutdown Flag',
        'Sleep Time (ms)',
        'Delay Time (ms)',
        'Code Address',
        'Parameter Address',
        'Server',
        'Reason',
        'System Metric Index',
        'Initial Owner',
        'Error Control',
        'Username',
        'Password',
        'Command',
    )
    TERM_DATABASE_NAME = 'Database Name'
    TERM_DESTINATION_ADDRESS = 'Destination Address'
    TERM_CALLBACK_ADDRESS = 'Callback Address'
    TERM_SOURCE_ADDRESS = 'Source Address'
    TERM_HOSTNAME = 'Hostname'
    TERM_NUMBER_OF_BYTES_PER_SEND = 'Number of Bytes Per Send'
    TERM_SIZE_BYTES = 'Size (bytes)'
    TERM_DELAY_TIME_MS = 'Delay Time (ms)'
    TERM_SHARE_MODE = 'Share Mode'
    TERM_SLEEP_TIME_MS = 'Sleep Time (ms)'
    TERM_TARGET_PID = 'Target PID'
    TERM_PARAMETER_ADDRESS = 'Parameter Address'
    TERM_SERVICE_NAME = 'Service Name'
    TERM_STARTING_ADDRESS = 'Starting Address'
    TERM_REQUESTED_VERSION = 'Requested Version'
    TERM_REQUEST_SIZE = 'Request Size'
    TERM_ERROR_CONTROL = 'Error Control'
    TERM_FUNCTION_ADDRESS = 'Function Address'
    TERM_SHUTDOWN_FLAG = 'Shutdown Flag'
    TERM_REASON = 'Reason'
    TERM_PROTECTION = 'Protection'
    TERM_INITIAL_OWNER = 'Initial Owner'
    TERM_CREATION_FLAGS = 'Creation Flags'
    TERM_FILE_INFORMATION_CLASS = 'File Information Class'
    TERM_PASSWORD = 'Password'
    TERM_FUNCTION_ORDINAL = 'Function Ordinal'
    TERM_USERNAME = 'Username'
    TERM_SERVICE_STATE = 'Service State'
    TERM_PRIVILEGE_NAME = 'Privilege Name'
    TERM_PROXY_BYPASS = 'Proxy Bypass'
    TERM_APPLICATION_NAME = 'Application Name'
    TERM_HOOK_TYPE = 'Hook Type'
    TERM_APC_ADDRESS = 'APC Address'
    TERM_MAPPING_OFFSET = 'Mapping Offset'
    TERM_APC_MODE = 'APC Mode'
    TERM_FLAGS = 'Flags'
    TERM_CODE_ADDRESS = 'Code Address'
    TERM_CONTROL_PARAMETER = 'Control Parameter'
    TERM_OPTIONS = 'Options'
    TERM_TRANSFER_FLAGS = 'Transfer Flags'
    TERM_SYSTEM_METRIC_INDEX = 'System Metric Index'
    TERM_BASE_ADDRESS = 'Base Address'
    TERM_ACCESS_MODE = 'Access Mode'
    TERM_SERVICE_TYPE = 'Service Type'
    TERM_SERVER = 'Server'
    TERM_API = 'API'
    TERM_FUNCTION_NAME = 'Function Name'
    TERM_CONTROL_CODE = 'Control Code'
    TERM_COMMAND = 'Command'
    TERM_PROXY_NAME = 'Proxy Name'
    TERM_HOST_NAME = 'Host Name'


class ActionRelationshipType(VocabString):
    _namespace = 'http://cybox.mitre.org/default_vocabularies-2'
    _XSI_TYPE = 'cyboxVocabs:ActionRelationshipTypeVocab-1.0'
    _VOCAB_VERSION = '1.0'
    _ALLOWED_VALUES = (
        'Preceded_By',
        'Followed_By',
        'Equivalent_To',
        'Related_To',
        'Dependent_On',
        'Initiated_By',
        'Initiated',
    )
    TERM_INITIATED = 'Initiated'
    TERM_INITIATED_BY = 'Initiated_By'
    TERM_FOLLOWED_BY = 'Followed_By'
    TERM_RELATED_TO = 'Related_To'
    TERM_PRECEDED_BY = 'Preceded_By'
    TERM_DEPENDENT_ON = 'Dependent_On'
    TERM_EQUIVALENT_TO = 'Equivalent_To'


class ObjectRelationship(VocabString):
    _namespace = 'http://cybox.mitre.org/default_vocabularies-2'
    _XSI_TYPE = 'cyboxVocabs:ObjectRelationshipVocab-1.1'
    _VOCAB_VERSION = '1.1'
    _ALLOWED_VALUES = (
        'Created',
        'Created_By',
        'Deleted',
        'Deleted_By',
        'Modified_Properties_Of',
        'Properties_Modified_By',
        'Read_From',
        'Read_From_By',
        'Wrote_To',
        'Written_To_By',
        'Downloaded_From',
        'Downloaded_To',
        'Downloaded',
        'Downloaded_By',
        'Uploaded',
        'Uploaded_By',
        'Uploaded_To',
        'Received_Via_Upload',
        'Uploaded_From',
        'Sent_Via_Upload',
        'Suspended',
        'Suspended_By',
        'Paused',
        'Paused_By',
        'Resumed',
        'Resumed_By',
        'Opened',
        'Opened_By',
        'Closed',
        'Closed_By',
        'Copied_From',
        'Copied_To',
        'Copied',
        'Copied_By',
        'Moved_From',
        'Moved_To',
        'Moved',
        'Moved_By',
        'Searched_For',
        'Searched_For_By',
        'Allocated',
        'Allocated_By',
        'Initialized_To',
        'Initialized_By',
        'Sent',
        'Sent_By',
        'Sent_To',
        'Received_From',
        'Received',
        'Received_By',
        'Mapped_Into',
        'Mapped_By',
        'Properties_Queried',
        'Properties_Queried_By',
        'Values_Enumerated',
        'Values_Enumerated_By',
        'Bound',
        'Bound_By',
        'Freed',
        'Freed_By',
        'Killed',
        'Killed_By',
        'Encrypted',
        'Encrypted_By',
        'Encrypted_To',
        'Encrypted_From',
        'Decrypted',
        'Decrypted_By',
        'Packed',
        'Packed_By',
        'Unpacked',
        'Unpacked_By',
        'Packed_From',
        'Packed_Into',
        'Encoded',
        'Encoded_By',
        'Decoded',
        'Decoded_By',
        'Compressed_From',
        'Compressed_Into',
        'Compressed',
        'Compressed_By',
        'Decompressed',
        'Decompressed_By',
        'Joined',
        'Joined_By',
        'Merged',
        'Merged_By',
        'Locked',
        'Locked_By',
        'Unlocked',
        'Unlocked_By',
        'Hooked',
        'Hooked_By',
        'Unhooked',
        'Unhooked_By',
        'Monitored',
        'Monitored_By',
        'Listened_On',
        'Listened_On_By',
        'Renamed_From',
        'Renamed_To',
        'Renamed',
        'Renamed_By',
        'Injected_Into',
        'Injected_As',
        'Injected',
        'Injected_By',
        'Deleted_From',
        'Previously_Contained',
        'Loaded_Into',
        'Loaded_From',
        'Set_To',
        'Set_From',
        'Resolved_To',
        'Related_To',
        'Dropped',
        'Dropped_By',
        'Contains',
        'Contained_Within',
        'Extracted_From',
        'Installed',
        'Installed_By',
        'Connected_To',
        'Connected_From',
        'Sub-domain_Of',
        'Supra-domain_Of',
        'Root_Domain_Of',
        'FQDN_Of',
        'Parent_Of',
        'Child_Of',
        'Characterizes',
        'Characterized_By',
        'Used',
        'Used_By',
        'Redirects_To',
    )
    TERM_MODIFIED_PROPERTIES_OF = 'Modified_Properties_Of'
    TERM_UNLOCKED = 'Unlocked'
    TERM_COPIED_FROM = 'Copied_From'
    TERM_INITIALIZED_TO = 'Initialized_To'
    TERM_UNLOCKED_BY = 'Unlocked_By'
    TERM_DELETED_FROM = 'Deleted_From'
    TERM_SET_TO = 'Set_To'
    TERM_DECODED = 'Decoded'
    TERM_RESUMED_BY = 'Resumed_By'
    TERM_UPLOADED_FROM = 'Uploaded_From'
    TERM_ROOT_DOMAIN_OF = 'Root_Domain_Of'
    TERM_PAUSED_BY = 'Paused_By'
    TERM_ENCODED = 'Encoded'
    TERM_RECEIVED = 'Received'
    TERM_MOVED_FROM = 'Moved_From'
    TERM_HOOKED = 'Hooked'
    TERM_PROPERTIES_MODIFIED_BY = 'Properties_Modified_By'
    TERM_UNPACKED = 'Unpacked'
    TERM_RENAMED = 'Renamed'
    TERM_SET_FROM = 'Set_From'
    TERM_JOINED_BY = 'Joined_By'
    TERM_COPIED_BY = 'Copied_By'
    TERM_PACKED_FROM = 'Packed_From'
    TERM_SENT_TO = 'Sent_To'
    TERM_RENAMED_FROM = 'Renamed_From'
    TERM_MERGED_BY = 'Merged_By'
    TERM_UNHOOKED = 'Unhooked'
    TERM_LOADED_FROM = 'Loaded_From'
    TERM_OPENED_BY = 'Opened_By'
    TERM_DROPPED = 'Dropped'
    TERM_DROPPED_BY = 'Dropped_By'
    TERM_CONNECTED_FROM = 'Connected_From'
    TERM_UPLOADED_TO = 'Uploaded_To'
    TERM_FQDN_OF = 'FQDN_Of'
    TERM_PROPERTIES_QUERIED_BY = 'Properties_Queried_By'
    TERM_CHILD_OF = 'Child_Of'
    TERM_ENCRYPTED_TO = 'Encrypted_To'
    TERM_SENT = 'Sent'
    TERM_FREED = 'Freed'
    TERM_UPLOADED = 'Uploaded'
    TERM_FREED_BY = 'Freed_By'
    TERM_DELETED = 'Deleted'
    TERM_MAPPED_INTO = 'Mapped_Into'
    TERM_DOWNLOADED_BY = 'Downloaded_By'
    TERM_SENT_BY = 'Sent_By'
    TERM_CREATED_BY = 'Created_By'
    TERM_LISTENED_ON = 'Listened_On'
    TERM_COPIED_TO = 'Copied_To'
    TERM_READ_FROM = 'Read_From'
    TERM_INJECTED_AS = 'Injected_As'
    TERM_KILLED = 'Killed'
    TERM_RESUMED = 'Resumed'
    TERM_VALUES_ENUMERATED = 'Values_Enumerated'
    TERM_LOCKED = 'Locked'
    TERM_PACKED_BY = 'Packed_By'
    TERM_CREATED = 'Created'
    TERM_ENCRYPTED_BY = 'Encrypted_By'
    TERM_RELATED_TO = 'Related_To'
    TERM_ENCRYPTED_FROM = 'Encrypted_From'
    TERM_CONTAINED_WITHIN = 'Contained_Within'
    TERM_UPLOADED_BY = 'Uploaded_By'
    TERM_CLOSED_BY = 'Closed_By'
    TERM_UNPACKED_BY = 'Unpacked_By'
    TERM_CONNECTED_TO = 'Connected_To'
    TERM_ENCRYPTED = 'Encrypted'
    TERM_INSTALLED = 'Installed'
    TERM_PAUSED = 'Paused'
    TERM_HOOKED_BY = 'Hooked_By'
    TERM_INJECTED_INTO = 'Injected_Into'
    TERM_SUSPENDED = 'Suspended'
    TERM_DOWNLOADED_TO = 'Downloaded_To'
    TERM_ALLOCATED = 'Allocated'
    TERM_PACKED = 'Packed'
    TERM_MONITORED = 'Monitored'
    TERM_OPENED = 'Opened'
    TERM_REDIRECTS_TO = 'Redirects_To'
    TERM_PREVIOUSLY_CONTAINED = 'Previously_Contained'
    TERM_SENT_VIA_UPLOAD = 'Sent_Via_Upload'
    TERM_BOUND_BY = 'Bound_By'
    TERM_CLOSED = 'Closed'
    TERM_SEARCHED_FOR_BY = 'Searched_For_By'
    TERM_RECEIVED_FROM = 'Received_From'
    TERM_USED = 'Used'
    TERM_KILLED_BY = 'Killed_By'
    TERM_COMPRESSED_FROM = 'Compressed_From'
    TERM_RESOLVED_TO = 'Resolved_To'
    TERM_RENAMED_TO = 'Renamed_To'
    TERM_DELETED_BY = 'Deleted_By'
    TERM_LISTENED_ON_BY = 'Listened_On_By'
    TERM_DOWNLOADED = 'Downloaded'
    TERM_COMPRESSED = 'Compressed'
    TERM_CHARACTERIZED_BY = 'Characterized_By'
    TERM_DECODED_BY = 'Decoded_By'
    TERM_WRITTEN_TO_BY = 'Written_To_By'
    TERM_DECOMPRESSED_BY = 'Decompressed_By'
    TERM_CHARACTERIZES = 'Characterizes'
    TERM_MONITORED_BY = 'Monitored_By'
    TERM_RECEIVED_BY = 'Received_By'
    TERM_SUSPENDED_BY = 'Suspended_By'
    TERM_MAPPED_BY = 'Mapped_By'
    TERM_LOCKED_BY = 'Locked_By'
    TERM_MOVED = 'Moved'
    TERM_SUPRA_DOMAIN_OF = 'Supra-domain_Of'
    TERM_DECRYPTED_BY = 'Decrypted_By'
    TERM_PARENT_OF = 'Parent_Of'
    TERM_MOVED_BY = 'Moved_By'
    TERM_INITIALIZED_BY = 'Initialized_By'
    TERM_READ_FROM_BY = 'Read_From_By'
    TERM_DECRYPTED = 'Decrypted'
    TERM_USED_BY = 'Used_By'
    TERM_CONTAINS = 'Contains'
    TERM_RENAMED_BY = 'Renamed_By'
    TERM_RECEIVED_VIA_UPLOAD = 'Received_Via_Upload'
    TERM_COMPRESSED_BY = 'Compressed_By'
    TERM_COPIED = 'Copied'
    TERM_WROTE_TO = 'Wrote_To'
    TERM_DOWNLOADED_FROM = 'Downloaded_From'
    TERM_SEARCHED_FOR = 'Searched_For'
    TERM_ENCODED_BY = 'Encoded_By'
    TERM_MERGED = 'Merged'
    TERM_DECOMPRESSED = 'Decompressed'
    TERM_COMPRESSED_INTO = 'Compressed_Into'
    TERM_INJECTED = 'Injected'
    TERM_PACKED_INTO = 'Packed_Into'
    TERM_VALUES_ENUMERATED_BY = 'Values_Enumerated_By'
    TERM_ALLOCATED_BY = 'Allocated_By'
    TERM_SUB_DOMAIN_OF = 'Sub-domain_Of'
    TERM_JOINED = 'Joined'
    TERM_MOVED_TO = 'Moved_To'
    TERM_LOADED_INTO = 'Loaded_Into'
    TERM_BOUND = 'Bound'
    TERM_UNHOOKED_BY = 'Unhooked_By'
    TERM_PROPERTIES_QUERIED = 'Properties_Queried'
    TERM_EXTRACTED_FROM = 'Extracted_From'
    TERM_INSTALLED_BY = 'Installed_By'
    TERM_INJECTED_BY = 'Injected_By'


class CharacterEncoding(VocabString):
    _namespace = 'http://cybox.mitre.org/default_vocabularies-2'
    _XSI_TYPE = 'cyboxVocabs:CharacterEncodingVocab-1.0'
    _VOCAB_VERSION = '1.0'
    _ALLOWED_VALUES = (
        'ASCII',
        'UTF-8',
        'UTF-16',
        'UTF-32',
        'Windows-1250',
        'Windows-1251',
        'Windows-1252',
        'Windows-1253',
        'Windows-1254',
        'Windows-1255',
        'Windows-1256',
        'Windows-1257',
        'Windows-1258',
    )
    TERM_WINDOWS_1255 = 'Windows-1255'
    TERM_UTF_32 = 'UTF-32'
    TERM_WINDOWS_1252 = 'Windows-1252'
    TERM_UTF_8 = 'UTF-8'
    TERM_WINDOWS_1258 = 'Windows-1258'
    TERM_WINDOWS_1256 = 'Windows-1256'
    TERM_WINDOWS_1257 = 'Windows-1257'
    TERM_WINDOWS_1254 = 'Windows-1254'
    TERM_UTF_16 = 'UTF-16'
    TERM_ASCII = 'ASCII'
    TERM_WINDOWS_1253 = 'Windows-1253'
    TERM_WINDOWS_1250 = 'Windows-1250'
    TERM_WINDOWS_1251 = 'Windows-1251'


class ObjectState(VocabString):
    _namespace = 'http://cybox.mitre.org/default_vocabularies-2'
    _XSI_TYPE = 'cyboxVocabs:ObjectStateVocab-1.0'
    _VOCAB_VERSION = '1.0'
    _ALLOWED_VALUES = (
        'Exists',
        'Does Not Exist',
        'Open',
        'Closed',
        'Active',
        'Inactive',
        'Locked',
        'Unlocked',
        'Started',
        'Stopped',
    )
    TERM_LOCKED = 'Locked'
    TERM_EXISTS = 'Exists'
    TERM_UNLOCKED = 'Unlocked'
    TERM_STARTED = 'Started'
    TERM_DOES_NOT_EXIST = 'Does Not Exist'
    TERM_INACTIVE = 'Inactive'
    TERM_STOPPED = 'Stopped'
    TERM_CLOSED = 'Closed'
    TERM_ACTIVE = 'Active'
    TERM_OPEN = 'Open'


class ToolType(VocabString):
    _namespace = 'http://cybox.mitre.org/default_vocabularies-2'
    _XSI_TYPE = 'cyboxVocabs:ToolTypeVocab-1.1'
    _VOCAB_VERSION = '1.1'
    _ALLOWED_VALUES = (
        'NIDS',
        'NIPS',
        'HIDS',
        'HIPS',
        'Firewall',
        'Router',
        'Proxy',
        'Gateway',
        'SNMP/MIBs',
        'AV',
        'DBMS Monitor',
        'Vulnerability Scanner',
        'Configuration Scanner',
        'Asset Scanner',
        'SIM',
        'SEM',
        'Digital Forensics',
        'Static Malware Analysis',
        'Dynamic Malware Analysis',
        'System Configuration Management Tool',
        'Network Configuration Management Tool',
        'Packet Capture and Analysis',
        'Network Flow Capture and Analysis',
        'Intelligence Service Platform',
    )
    TERM_VULNERABILITY_SCANNER = 'Vulnerability Scanner'
    TERM_CONFIGURATION_SCANNER = 'Configuration Scanner'
    TERM_ROUTER = 'Router'
    TERM_STATIC_MALWARE_ANALYSIS = 'Static Malware Analysis'
    TERM_SIM = 'SIM'
    TERM_ASSET_SCANNER = 'Asset Scanner'
    TERM_DYNAMIC_MALWARE_ANALYSIS = 'Dynamic Malware Analysis'
    TERM_SNMP_MIBS = 'SNMP/MIBs'
    TERM_HIDS = 'HIDS'
    TERM_DBMS_MONITOR = 'DBMS Monitor'
    TERM_PROXY = 'Proxy'
    TERM_PACKET_CAPTURE_AND_ANALYSIS = 'Packet Capture and Analysis'
    TERM_NIDS = 'NIDS'
    TERM_AV = 'AV'
    TERM_SYSTEM_CONFIGURATION_MANAGEMENT_TOOL = 'System Configuration Management Tool'
    TERM_DIGITAL_FORENSICS = 'Digital Forensics'
    TERM_SEM = 'SEM'
    TERM_INTELLIGENCE_SERVICE_PLATFORM = 'Intelligence Service Platform'
    TERM_NETWORK_CONFIGURATION_MANAGEMENT_TOOL = 'Network Configuration Management Tool'
    TERM_FIREWALL = 'Firewall'
    TERM_NETWORK_FLOW_CAPTURE_AND_ANALYSIS = 'Network Flow Capture and Analysis'
    TERM_NIPS = 'NIPS'
    TERM_GATEWAY = 'Gateway'
    TERM_HIPS = 'HIPS'


class ActionName(VocabString):
    _namespace = 'http://cybox.mitre.org/default_vocabularies-2'
    _XSI_TYPE = 'cyboxVocabs:ActionNameVocab-1.1'
    _VOCAB_VERSION = '1.1'
    _ALLOWED_VALUES = (
        'Accept Socket Connection',
        'Add Connection to Network Share',
        'Add Network Share',
        'Add System Call Hook',
        'Add User',
        'Add Windows Hook',
        'Add Scheduled Task',
        'Allocate Virtual Memory in Process',
        'Bind Address to Socket',
        'Change Service Configuration',
        'Check for Remote Debugger',
        'Close Port',
        'Close Registry Key',
        'Close Socket',
        'Configure Service',
        'Connect to IP',
        'Connect to Named Pipe',
        'Connect to Network Share',
        'Connect to Socket',
        'Connect to URL',
        'Control Driver',
        'Control Service',
        'Copy File',
        'Create Dialog Box',
        'Create Directory',
        'Create Event',
        'Create File',
        'Create File Alternate Data Stream',
        'Create File Mapping',
        'Create File Symbolic Link',
        'Create Hidden File',
        'Create Mailslot',
        'Create Module',
        'Create Mutex',
        'Create Named Pipe',
        'Create Process',
        'Create Process as User',
        'Create Registry Key',
        'Create Registry Key Value',
        'Create Remote Thread in Process',
        'Create Service',
        'Create Socket',
        'Create Symbolic Link',
        'Create Thread',
        'Create Window',
        'Delete Directory',
        'Delete File',
        'Delete Named Pipe',
        'Delete Network Share',
        'Delete Registry Key',
        'Delete Registry Key Value',
        'Delete Service',
        'Delete User',
        'Disconnect from Named Pipe',
        'Disconnect from Network Share',
        'Disconnect from Socket',
        'Download File',
        'Enumerate DLLs',
        'Enumerate Network Shares',
        'Enumerate Protocols',
        'Enumerate Registry Key Subkeys',
        'Enumerate Registry Key Values',
        'Enumerate Threads in Process',
        'Enumerate Processes',
        'Enumerate Services',
        'Enumerate System Handles',
        'Enumerate Threads',
        'Enumerate Users',
        'Enumerate Windows',
        'Find File',
        'Find Window',
        'Flush Process Instruction Cache',
        'Free Library',
        'Free Process Virtual Memory',
        'Get Disk Free Space',
        'Get Disk Type',
        'Get Elapsed System Up Time',
        'Get File Attributes',
        'Get Function Address',
        'Get System Global Flags',
        'Get Host By Address',
        'Get Host By Name',
        'Get Host Name',
        'Get Library File Name',
        'Get Library Handle',
        'Get NetBIOS Name',
        'Get Process Current Directory',
        'Get Process Environment Variable',
        'Get Process Startup Information',
        'Get Processes Snapshot',
        'Get Registry Key Attributes',
        'Get Service Status',
        'Get System Global Flags',
        'Get System Local Time',
        'Get System Host Name',
        'Get System NetBIOS Name',
        'Get System Network Parameters',
        'Get System Time',
        'Get Thread Context',
        'Get Thread Username',
        'Get User Attributes',
        'Get Username',
        'Get Windows Directory',
        'Get Windows System Directory',
        'Get Windows Temporary Files Directory',
        'Hide Window',
        'Impersonate Process',
        'Impersonate Thread',
        'Inject Memory Page',
        'Kill Process',
        'Kill Thread',
        'Kill Window',
        'Listen on Port',
        'Listen on Socket',
        'Load and Call Driver',
        'Load Driver',
        'Load Library',
        'Load Module',
        'Lock File',
        'Logon as User',
        'Map File',
        'Map Library',
        'Map View of File',
        'Modify File',
        'Modify Named Pipe',
        'Modify Process',
        'Modify Service',
        'Modify Registry Key',
        'Modify Registry Key Value',
        'Monitor Registry Key',
        'Move File',
        'Open File',
        'Open File Mapping',
        'Open Mutex',
        'Open Port',
        'Open Process',
        'Open Registry Key',
        'Open Service',
        'Open Service Control Manager',
        'Protect Virtual Memory',
        'Query Disk Attributes',
        'Query DNS',
        'Query Process Virtual Memory',
        'Queue APC in Thread',
        'Read File',
        'Read From Named Pipe',
        'Read From Process Memory',
        'Read Registry Key Value',
        'Receive Data on Socket',
        'Receive Email Message',
        'Release Mutex',
        'Rename File',
        'Revert Thread to Self',
        'Send Control Code to File',
        'Send Control Code to Pipe',
        'Send Control Code to Service',
        'Send Data on Socket',
        'Send Data to Address on Socket',
        'Send DNS Query',
        'Send Email Message',
        'Send ICMP Request',
        'Send Reverse DNS Query',
        'Set File Attributes',
        'Set NetBIOS Name',
        'Set Process Current Directory',
        'Set Process Environment Variable',
        'Set System Global Flags',
        'Set System Host Name',
        'Set System Time',
        'Set Thread Context',
        'Show Window',
        'Shutdown System',
        'Sleep Process',
        'Sleep System',
        'Start Service',
        'Unload Driver',
        'Unlock File',
        'Unmap File',
        'Unload Module',
        'Upload File',
        'Write to File',
        'Write to Process Virtual Memory',
    )
    TERM_ADD_SCHEDULED_TASK = 'Add Scheduled Task'
    TERM_GET_WINDOWS_DIRECTORY = 'Get Windows Directory'
    TERM_ENUMERATE_NETWORK_SHARES = 'Enumerate Network Shares'
    TERM_ENUMERATE_PROTOCOLS = 'Enumerate Protocols'
    TERM_GET_ELAPSED_SYSTEM_UP_TIME = 'Get Elapsed System Up Time'
    TERM_DISCONNECT_FROM_NETWORK_SHARE = 'Disconnect from Network Share'
    TERM_CONTROL_DRIVER = 'Control Driver'
    TERM_CREATE_SERVICE = 'Create Service'
    TERM_ENUMERATE_USERS = 'Enumerate Users'
    TERM_CREATE_MODULE = 'Create Module'
    TERM_CREATE_SOCKET = 'Create Socket'
    TERM_GET_WINDOWS_TEMPORARY_FILES_DIRECTORY = 'Get Windows Temporary Files Directory'
    TERM_FIND_FILE = 'Find File'
    TERM_ADD_CONNECTION_TO_NETWORK_SHARE = 'Add Connection to Network Share'
    TERM_SLEEP_PROCESS = 'Sleep Process'
    TERM_CREATE_DIRECTORY = 'Create Directory'
    TERM_IMPERSONATE_PROCESS = 'Impersonate Process'
    TERM_CREATE_THREAD = 'Create Thread'
    TERM_ENUMERATE_PROCESSES = 'Enumerate Processes'
    TERM_OPEN_MUTEX = 'Open Mutex'
    TERM_LOGON_AS_USER = 'Logon as User'
    TERM_ACCEPT_SOCKET_CONNECTION = 'Accept Socket Connection'
    TERM_MODIFY_NAMED_PIPE = 'Modify Named Pipe'
    TERM_CREATE_FILE_ALTERNATE_DATA_STREAM = 'Create File Alternate Data Stream'
    TERM_KILL_PROCESS = 'Kill Process'
    TERM_UPLOAD_FILE = 'Upload File'
    TERM_MODIFY_SERVICE = 'Modify Service'
    TERM_LOAD_LIBRARY = 'Load Library'
    TERM_ADD_SYSTEM_CALL_HOOK = 'Add System Call Hook'
    TERM_LISTEN_ON_PORT = 'Listen on Port'
    TERM_LOAD_MODULE = 'Load Module'
    TERM_ENUMERATE_THREADS = 'Enumerate Threads'
    TERM_GET_LIBRARY_FILE_NAME = 'Get Library File Name'
    TERM_OPEN_REGISTRY_KEY = 'Open Registry Key'
    TERM_CREATE_HIDDEN_FILE = 'Create Hidden File'
    TERM_ENUMERATE_SERVICES = 'Enumerate Services'
    TERM_LOAD_DRIVER = 'Load Driver'
    TERM_GET_DISK_FREE_SPACE = 'Get Disk Free Space'
    TERM_CREATE_REMOTE_THREAD_IN_PROCESS = 'Create Remote Thread in Process'
    TERM_DELETE_NETWORK_SHARE = 'Delete Network Share'
    TERM_MODIFY_REGISTRY_KEY = 'Modify Registry Key'
    TERM_GET_PROCESS_CURRENT_DIRECTORY = 'Get Process Current Directory'
    TERM_QUERY_DNS = 'Query DNS'
    TERM_RECEIVE_EMAIL_MESSAGE = 'Receive Email Message'
    TERM_GET_LIBRARY_HANDLE = 'Get Library Handle'
    TERM_GET_NETBIOS_NAME = 'Get NetBIOS Name'
    TERM_ALLOCATE_VIRTUAL_MEMORY_IN_PROCESS = 'Allocate Virtual Memory in Process'
    TERM_READ_FROM_PROCESS_MEMORY = 'Read From Process Memory'
    TERM_MODIFY_PROCESS = 'Modify Process'
    TERM_CREATE_PROCESS = 'Create Process'
    TERM_HIDE_WINDOW = 'Hide Window'
    TERM_RELEASE_MUTEX = 'Release Mutex'
    TERM_GET_SYSTEM_NETWORK_PARAMETERS = 'Get System Network Parameters'
    TERM_SEND_DNS_QUERY = 'Send DNS Query'
    TERM_COPY_FILE = 'Copy File'
    TERM_CREATE_NAMED_PIPE = 'Create Named Pipe'
    TERM_SET_SYSTEM_TIME = 'Set System Time'
    TERM_FREE_LIBRARY = 'Free Library'
    TERM_READ_FILE = 'Read File'
    TERM_CREATE_FILE_SYMBOLIC_LINK = 'Create File Symbolic Link'
    TERM_DELETE_REGISTRY_KEY_VALUE = 'Delete Registry Key Value'
    TERM_GET_HOST_BY_NAME = 'Get Host By Name'
    TERM_CREATE_FILE_MAPPING = 'Create File Mapping'
    TERM_SLEEP_SYSTEM = 'Sleep System'
    TERM_UNLOCK_FILE = 'Unlock File'
    TERM_PROTECT_VIRTUAL_MEMORY = 'Protect Virtual Memory'
    TERM_UNLOAD_DRIVER = 'Unload Driver'
    TERM_CREATE_FILE = 'Create File'
    TERM_SET_SYSTEM_HOST_NAME = 'Set System Host Name'
    TERM_QUEUE_APC_IN_THREAD = 'Queue APC in Thread'
    TERM_GET_FUNCTION_ADDRESS = 'Get Function Address'
    TERM_CREATE_REGISTRY_KEY = 'Create Registry Key'
    TERM_SHOW_WINDOW = 'Show Window'
    TERM_FIND_WINDOW = 'Find Window'
    TERM_ENUMERATE_SYSTEM_HANDLES = 'Enumerate System Handles'
    TERM_CREATE_MUTEX = 'Create Mutex'
    TERM_OPEN_SERVICE_CONTROL_MANAGER = 'Open Service Control Manager'
    TERM_UNLOAD_MODULE = 'Unload Module'
    TERM_SEND_EMAIL_MESSAGE = 'Send Email Message'
    TERM_QUERY_PROCESS_VIRTUAL_MEMORY = 'Query Process Virtual Memory'
    TERM_CONNECT_TO_NAMED_PIPE = 'Connect to Named Pipe'
    TERM_CREATE_WINDOW = 'Create Window'
    TERM_DELETE_SERVICE = 'Delete Service'
    TERM_DELETE_USER = 'Delete User'
    TERM_SET_THREAD_CONTEXT = 'Set Thread Context'
    TERM_GET_SYSTEM_HOST_NAME = 'Get System Host Name'
    TERM_MAP_LIBRARY = 'Map Library'
    TERM_INJECT_MEMORY_PAGE = 'Inject Memory Page'
    TERM_CREATE_SYMBOLIC_LINK = 'Create Symbolic Link'
    TERM_SET_SYSTEM_GLOBAL_FLAGS = 'Set System Global Flags'
    TERM_MAP_FILE = 'Map File'
    TERM_CONNECT_TO_NETWORK_SHARE = 'Connect to Network Share'
    TERM_KILL_THREAD = 'Kill Thread'
    TERM_BIND_ADDRESS_TO_SOCKET = 'Bind Address to Socket'
    TERM_GET_FILE_ATTRIBUTES = 'Get File Attributes'
    TERM_DISCONNECT_FROM_NAMED_PIPE = 'Disconnect from Named Pipe'
    TERM_GET_PROCESS_STARTUP_INFORMATION = 'Get Process Startup Information'
    TERM_QUERY_DISK_ATTRIBUTES = 'Query Disk Attributes'
    TERM_LOCK_FILE = 'Lock File'
    TERM_GET_SYSTEM_NETBIOS_NAME = 'Get System NetBIOS Name'
    TERM_START_SERVICE = 'Start Service'
    TERM_GET_REGISTRY_KEY_ATTRIBUTES = 'Get Registry Key Attributes'
    TERM_LOAD_AND_CALL_DRIVER = 'Load and Call Driver'
    TERM_UNMAP_FILE = 'Unmap File'
    TERM_GET_THREAD_CONTEXT = 'Get Thread Context'
    TERM_CREATE_EVENT = 'Create Event'
    TERM_CLOSE_SOCKET = 'Close Socket'
    TERM_DELETE_DIRECTORY = 'Delete Directory'
    TERM_OPEN_SERVICE = 'Open Service'
    TERM_DELETE_FILE = 'Delete File'
    TERM_RECEIVE_DATA_ON_SOCKET = 'Receive Data on Socket'
    TERM_DELETE_NAMED_PIPE = 'Delete Named Pipe'
    TERM_CHANGE_SERVICE_CONFIGURATION = 'Change Service Configuration'
    TERM_GET_HOST_BY_ADDRESS = 'Get Host By Address'
    TERM_ADD_NETWORK_SHARE = 'Add Network Share'
    TERM_FLUSH_PROCESS_INSTRUCTION_CACHE = 'Flush Process Instruction Cache'
    TERM_GET_THREAD_USERNAME = 'Get Thread Username'
    TERM_ENUMERATE_REGISTRY_KEY_SUBKEYS = 'Enumerate Registry Key Subkeys'
    TERM_CHECK_FOR_REMOTE_DEBUGGER = 'Check for Remote Debugger'
    TERM_OPEN_FILE_MAPPING = 'Open File Mapping'
    TERM_DELETE_REGISTRY_KEY = 'Delete Registry Key'
    TERM_LISTEN_ON_SOCKET = 'Listen on Socket'
    TERM_SET_FILE_ATTRIBUTES = 'Set File Attributes'
    TERM_KILL_WINDOW = 'Kill Window'
    TERM_GET_USERNAME = 'Get Username'
    TERM_OPEN_PORT = 'Open Port'
    TERM_GET_SYSTEM_LOCAL_TIME = 'Get System Local Time'
    TERM_GET_WINDOWS_SYSTEM_DIRECTORY = 'Get Windows System Directory'
    TERM_MODIFY_REGISTRY_KEY_VALUE = 'Modify Registry Key Value'
    TERM_DISCONNECT_FROM_SOCKET = 'Disconnect from Socket'
    TERM_CLOSE_PORT = 'Close Port'
    TERM_WRITE_TO_PROCESS_VIRTUAL_MEMORY = 'Write to Process Virtual Memory'
    TERM_CONNECT_TO_IP = 'Connect to IP'
    TERM_CLOSE_REGISTRY_KEY = 'Close Registry Key'
    TERM_GET_PROCESS_ENVIRONMENT_VARIABLE = 'Get Process Environment Variable'
    TERM_GET_SYSTEM_TIME = 'Get System Time'
    TERM_SEND_DATA_ON_SOCKET = 'Send Data on Socket'
    TERM_SET_NETBIOS_NAME = 'Set NetBIOS Name'
    TERM_MODIFY_FILE = 'Modify File'
    TERM_GET_DISK_TYPE = 'Get Disk Type'
    TERM_MAP_VIEW_OF_FILE = 'Map View of File'
    TERM_SEND_REVERSE_DNS_QUERY = 'Send Reverse DNS Query'
    TERM_ENUMERATE_DLLS = 'Enumerate DLLs'
    TERM_FREE_PROCESS_VIRTUAL_MEMORY = 'Free Process Virtual Memory'
    TERM_GET_SERVICE_STATUS = 'Get Service Status'
    TERM_CREATE_REGISTRY_KEY_VALUE = 'Create Registry Key Value'
    TERM_SET_PROCESS_CURRENT_DIRECTORY = 'Set Process Current Directory'
    TERM_MONITOR_REGISTRY_KEY = 'Monitor Registry Key'
    TERM_ENUMERATE_THREADS_IN_PROCESS = 'Enumerate Threads in Process'
    TERM_ADD_WINDOWS_HOOK = 'Add Windows Hook'
    TERM_WRITE_TO_FILE = 'Write to File'
    TERM_CREATE_MAILSLOT = 'Create Mailslot'
    TERM_GET_PROCESSES_SNAPSHOT = 'Get Processes Snapshot'
    TERM_DOWNLOAD_FILE = 'Download File'
    TERM_OPEN_FILE = 'Open File'
    TERM_READ_FROM_NAMED_PIPE = 'Read From Named Pipe'
    TERM_READ_REGISTRY_KEY_VALUE = 'Read Registry Key Value'
    TERM_SEND_CONTROL_CODE_TO_FILE = 'Send Control Code to File'
    TERM_RENAME_FILE = 'Rename File'
    TERM_SEND_DATA_TO_ADDRESS_ON_SOCKET = 'Send Data to Address on Socket'
    TERM_SHUTDOWN_SYSTEM = 'Shutdown System'
    TERM_GET_SYSTEM_GLOBAL_FLAGS = 'Get System Global Flags'
    TERM_SEND_CONTROL_CODE_TO_SERVICE = 'Send Control Code to Service'
    TERM_ENUMERATE_WINDOWS = 'Enumerate Windows'
    TERM_CONNECT_TO_URL = 'Connect to URL'
    TERM_CREATE_PROCESS_AS_USER = 'Create Process as User'
    TERM_CONTROL_SERVICE = 'Control Service'
    TERM_MOVE_FILE = 'Move File'
    TERM_OPEN_PROCESS = 'Open Process'
    TERM_ENUMERATE_REGISTRY_KEY_VALUES = 'Enumerate Registry Key Values'
    TERM_IMPERSONATE_THREAD = 'Impersonate Thread'
    TERM_SET_PROCESS_ENVIRONMENT_VARIABLE = 'Set Process Environment Variable'
    TERM_SEND_CONTROL_CODE_TO_PIPE = 'Send Control Code to Pipe'
    TERM_SEND_ICMP_REQUEST = 'Send ICMP Request'
    TERM_CONNECT_TO_SOCKET = 'Connect to Socket'
    TERM_REVERT_THREAD_TO_SELF = 'Revert Thread to Self'
    TERM_CONFIGURE_SERVICE = 'Configure Service'
    TERM_CREATE_DIALOG_BOX = 'Create Dialog Box'
    TERM_ADD_USER = 'Add User'
    TERM_GET_HOST_NAME = 'Get Host Name'
    TERM_GET_USER_ATTRIBUTES = 'Get User Attributes'


class InformationSourceType(VocabString):
    _namespace = 'http://cybox.mitre.org/default_vocabularies-2'
    _XSI_TYPE = 'cyboxVocabs:InformationSourceTypeVocab-1.0'
    _VOCAB_VERSION = '1.0'
    _ALLOWED_VALUES = (
        'Comm Logs',
        'Application Logs',
        'Web Logs',
        'DBMS Log',
        'OS/Device Driver APIs',
        'Frameworks',
        'VM Hypervisor',
        'TPM',
        'Application Framework',
        'Help Desk',
        'Incident Management',
        'IAVM',
    )
    TERM_IAVM = 'IAVM'
    TERM_INCIDENT_MANAGEMENT = 'Incident Management'
    TERM_APPLICATION_FRAMEWORK = 'Application Framework'
    TERM_APPLICATION_LOGS = 'Application Logs'
    TERM_TPM = 'TPM'
    TERM_DBMS_LOG = 'DBMS Log'
    TERM_FRAMEWORKS = 'Frameworks'
    TERM_OS_DEVICE_DRIVER_APIS = 'OS/Device Driver APIs'
    TERM_WEB_LOGS = 'Web Logs'
    TERM_COMM_LOGS = 'Comm Logs'
    TERM_VM_HYPERVISOR = 'VM Hypervisor'
    TERM_HELP_DESK = 'Help Desk'


#: Mapping of Controlled Vocabulary xsi:type's to their class implementations.
_VOCAB_MAP = {}


def add_vocab(cls):
    _VOCAB_MAP[cls._XSI_TYPE] = cls  # noqa


add_vocab(EventType)
add_vocab(ActionType)
add_vocab(ActionObjectAssociationType)
add_vocab(HashName)
add_vocab(ActionArgumentName)
add_vocab(ActionRelationshipType)
add_vocab(ObjectRelationship)
add_vocab(CharacterEncoding)
add_vocab(ObjectState)
add_vocab(ToolType)
add_vocab(ActionName)
add_vocab(InformationSourceType)


# Avoid polluting namespaces with our VocabString impls
__all__ = [
    'VocabString',
    'VocabField'
]
