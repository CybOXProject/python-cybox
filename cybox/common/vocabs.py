# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

# TODO: This module should probably move to mixbox.
import functools

from mixbox import entities
from mixbox import fields
from mixbox import typedlist
from mixbox.vendor import six

import cybox.bindings.cybox_common as common_binding
from cybox.common import PatternFieldGroup
from cybox.utils import normalize_to_xml, denormalize_from_xml


def validate_value(instance, value):
    allowed = instance._ALLOWED_VALUES

    if not value:
        return
    elif not allowed:
        return
    elif value in allowed:
        return
    else:
        error = "Value for vocab {instance.__class__} must be one of {allowed}. Received '{value}'"
        error = error.format(**locals())
        raise ValueError(error)


class VocabFactory(entities.EntityFactory):
    _convert_strings = True
    
    @classmethod
    def entity_class(cls, key):
        if not key:
            return VocabString

        for xsitype, klass in six.iteritems(_VOCAB_MAP):
            if key in xsitype:
                return klass

        return VocabString


class VocabList(typedlist.TypedList):
    """VocabString fields can be any type of VocabString, though there is often
    a preferred/default VocabString type.

    The TypedList will attempt to make sure that every input item is an instance
    of the default VocabString and throw an error if it isn't. This sublcass
    overrides that behavior and allows any instance of VocabString to be
    inserted.
    """

    def _is_valid(self, value):
        return isinstance(value, VocabString)


class VocabField(fields.TypedField):
    """TypedField subclass for VocabString fields."""

    def __init__(self, *args, **kwargs):
        """Intercepts the __init__() call to TypedField.

        Set the type that will be used in from_dict and from_obj calls to
        :class:`VocabString`.

        Set the type that will be used in ``__set__`` for casting as the
        original ``type_`` argument, or :class:`VocabString` if no `type_`
        argument was provided.

        """
        super(VocabField, self).__init__(*args, **kwargs)
        self.factory = VocabFactory  # force this factory

        if self._unresolved_type is None:
            self.type_ = VocabString

        self._listfunc = functools.partial(VocabList, type=self._unresolved_type)

    def check_type(self, value):
        return isinstance(value, VocabString)


class VocabString(PatternFieldGroup, entities.Entity):
    _namespace = 'http://cybox.mitre.org/default_vocabularies-2'
    # All subclasses should override this
    _XSI_TYPE = None
    _ALLOWED_VALUES = ()
    _binding = common_binding
    _binding_class = common_binding.ControlledVocabularyStringType

    value = fields.TypedField("valueOf_", key_name="value", preset_hook=validate_value)
    vocab_name = fields.TypedField("vocab_name")
    vocab_reference = fields.TypedField("vocab_reference")
    xsi_type = fields.TypedField("xsi_type", key_name="xsi:type")

    def __init__(self, value=None):
        super(VocabString, self).__init__()
        self.value = value
        self.xsi_type = self._XSI_TYPE
        self.vocab_name = None
        self.vocab_reference = None

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
            (self.xsi_type is None or type(self)._XSI_TYPE == self.xsi_type) and
            self.vocab_name is None and
            self.vocab_reference is None and
            super(VocabString, self).is_plain()
        )

    def to_obj(self, ns_info=None):
        obj = super(VocabString, self).to_obj(ns_info=ns_info)
        obj.valueOf_ = normalize_to_xml(self.value, self.delimiter)
        return obj

    def to_dict(self):
        if self.is_plain():
            return self.value
        return super(VocabString, self).to_dict()

    @classmethod
    def from_obj(cls, cls_obj):
        if not cls_obj:
            return None

        obj = super(VocabString, cls).from_obj(cls_obj)
        obj.value = denormalize_from_xml(value=cls_obj.valueOf_, delimiter=obj.delimiter)
        return obj


#: Mapping of Controlled Vocabulary xsi:type's to their class implementations.
_VOCAB_MAP = {}

def _get_terms(vocab_class):
    """Helper function used by register_vocab."""
    for k, v in vocab_class.__dict__.items():
        if k.startswith("TERM_"):
            yield v


def register_vocab(cls):
    """Register a VocabString subclass.

    Also, calculate all the permitted values for class being decorated by
    adding an ``_ALLOWED_VALUES`` tuple of all the values of class members
    beginning with ``TERM_``.
    """
    _VOCAB_MAP[cls._XSI_TYPE] = cls  # noqa

    cls._ALLOWED_VALUES = tuple(_get_terms(cls))
    return cls


@register_vocab
class EventType(VocabString):
    _namespace = 'http://cybox.mitre.org/default_vocabularies-2'
    _XSI_TYPE = 'cyboxVocabs:EventTypeVocab-1.0.1'
    _VOCAB_VERSION = '1.0.1'

    TERM_ACCOUNT_OPS_APP_LAYER = 'Account Ops (App Layer)'
    TERM_ANOMALY_EVENTS = 'Anomaly Events'
    TERM_API_CALLS = 'API Calls'
    TERM_APPLICATION_LOGIC = 'Application Logic'
    TERM_APP_LAYER_TRAFFIC = 'App Layer Traffic'
    TERM_AUTHENTICATION_OPS = 'Authentication Ops'
    TERM_AUTHORIZATION_ACL = 'Authorization (ACL)'
    TERM_AUTORUN = 'Autorun'
    TERM_AUTO_UPDATE_OPS = 'Auto-update Ops'
    TERM_BASIC_SYSTEM_OPS = 'Basic System Ops'
    TERM_CONFIGURATION_MANAGEMENT = 'Configuration Management'
    TERM_DATA_FLOW = 'Data Flow'
    TERM_DHCP = 'DHCP'
    TERM_DNS_LOOKUP_OPS = 'DNS Lookup Ops'
    TERM_EMAIL_OPS = 'Email Ops'
    TERM_FILE_OPS_CRUD = 'File Ops (CRUD)'
    TERM_GUI_KVM = 'GUI/KVM'
    TERM_HTTP_TRAFFIC = 'HTTP Traffic'
    TERM_IPC = 'IPC'
    TERM_IP_OPS = 'IP Ops'
    TERM_MEMORY_OPS = 'Memory Ops'
    TERM_PACKET_TRAFFIC = 'Packet Traffic'
    TERM_PORT_SCAN = 'Port Scan'
    TERM_PRIVILEGE_OPS = 'Privilege Ops'
    TERM_PROCEDURAL_COMPLIANCE = 'Procedural Compliance'
    TERM_PROCESS_MGT = 'Process Mgt'
    TERM_REDIRECTION = 'Redirection'
    TERM_REGISTRY_OPS = 'Registry Ops'
    TERM_SERVICE_MGT = 'Service Mgt'
    TERM_SESSION_MGT = 'Session Mgt'
    TERM_SIGNATURE_DETECTION = 'Signature Detection'
    TERM_SOCKET_OPS = 'Socket Ops'
    TERM_SQL = 'SQL'
    TERM_TECHNICAL_COMPLIANCE = 'Technical Compliance'
    TERM_THREAD_MGT = 'Thread Mgt'
    TERM_USB_MEDIA_DETECTION = 'USB/Media Detection'
    TERM_USER_PASSWORD_MGT = 'User/Password Mgt'


@register_vocab
class ActionType(VocabString):
    _namespace = 'http://cybox.mitre.org/default_vocabularies-2'
    _XSI_TYPE = 'cyboxVocabs:ActionTypeVocab-1.0'
    _VOCAB_VERSION = '1.0'

    TERM_ACCEPT = 'Accept'
    TERM_ACCESS = 'Access'
    TERM_ADD = 'Add'
    TERM_ALERT = 'Alert'
    TERM_ALLOCATE = 'Allocate'
    TERM_ARCHIVE = 'Archive'
    TERM_ASSIGN = 'Assign'
    TERM_AUDIT = 'Audit'
    TERM_BACKUP = 'Backup'
    TERM_BIND = 'Bind'
    TERM_BLOCK = 'Block'
    TERM_CALL = 'Call'
    TERM_CHANGE = 'Change'
    TERM_CHECK = 'Check'
    TERM_CLEAN = 'Clean'
    TERM_CLICK = 'Click'
    TERM_CLOSE = 'Close'
    TERM_COMPARE = 'Compare'
    TERM_COMPRESS = 'Compress'
    TERM_CONFIGURE = 'Configure'
    TERM_CONNECT = 'Connect'
    TERM_CONTROL = 'Control'
    TERM_COPY_DUPLICATE = 'Copy/Duplicate'
    TERM_CREATE = 'Create'
    TERM_DECODE = 'Decode'
    TERM_DECOMPRESS = 'Decompress'
    TERM_DECRYPT = 'Decrypt'
    TERM_DENY = 'Deny'
    TERM_DEPRESS = 'Depress'
    TERM_DETECT = 'Detect'
    TERM_DISCONNECT = 'Disconnect'
    TERM_DOWNLOAD = 'Download'
    TERM_DRAW = 'Draw'
    TERM_DROP = 'Drop'
    TERM_ENCODE = 'Encode'
    TERM_ENCRYPT = 'Encrypt'
    TERM_ENUMERATE = 'Enumerate'
    TERM_EXECUTE = 'Execute'
    TERM_EXTRACT = 'Extract'
    TERM_FILTER = 'Filter'
    TERM_FIND = 'Find'
    TERM_FLUSH = 'Flush'
    TERM_FORK = 'Fork'
    TERM_FREE = 'Free'
    TERM_GET = 'Get'
    TERM_HIDE = 'Hide'
    TERM_HOOK = 'Hook'
    TERM_IMPERSONATE = 'Impersonate'
    TERM_INITIALIZE = 'Initialize'
    TERM_INJECT = 'Inject'
    TERM_INSTALL = 'Install'
    TERM_INTERLEAVE = 'Interleave'
    TERM_JOIN = 'Join'
    TERM_KILL = 'Kill'
    TERM_LISTEN = 'Listen'
    TERM_LOAD = 'Load'
    TERM_LOCK = 'Lock'
    TERM_LOGIN_LOGON = 'Login/Logon'
    TERM_LOGOUT_LOGOFF = 'Logout/Logoff'
    TERM_MAP = 'Map'
    TERM_MERGE = 'Merge'
    TERM_MODIFY = 'Modify'
    TERM_MONITOR = 'Monitor'
    TERM_MOVE = 'Move'
    TERM_OPEN = 'Open'
    TERM_PACK = 'Pack'
    TERM_PAUSE = 'Pause'
    TERM_PRESS = 'Press'
    TERM_PROTECT = 'Protect'
    TERM_QUARANTINE = 'Quarantine'
    TERM_QUERY = 'Query'
    TERM_QUEUE = 'Queue'
    TERM_RAISE = 'Raise'
    TERM_READ = 'Read'
    TERM_RECEIVE = 'Receive'
    TERM_RELEASE = 'Release'
    TERM_REMOVE_DELETE = 'Remove/Delete'
    TERM_RENAME = 'Rename'
    TERM_REPLICATE = 'Replicate'
    TERM_RESTORE = 'Restore'
    TERM_RESUME = 'Resume'
    TERM_REVERT = 'Revert'
    TERM_RUN = 'Run'
    TERM_SAVE = 'Save'
    TERM_SCAN = 'Scan'
    TERM_SCHEDULE = 'Schedule'
    TERM_SEARCH = 'Search'
    TERM_SEND = 'Send'
    TERM_SET = 'Set'
    TERM_SHUTDOWN = 'Shutdown'
    TERM_SLEEP = 'Sleep'
    TERM_SNAPSHOT = 'Snapshot'
    TERM_START = 'Start'
    TERM_STOP = 'Stop'
    TERM_SUSPEND = 'Suspend'
    TERM_SYNCHRONIZE = 'Synchronize'
    TERM_THROW = 'Throw'
    TERM_TRANSMIT = 'Transmit'
    TERM_UNBLOCK = 'Unblock'
    TERM_UNHIDE = 'Unhide'
    TERM_UNHOOK = 'Unhook'
    TERM_UNINSTALL = 'Uninstall'
    TERM_UNLOAD = 'Unload'
    TERM_UNLOCK = 'Unlock'
    TERM_UNMAP = 'Unmap'
    TERM_UNPACK = 'Unpack'
    TERM_UPDATE = 'Update'
    TERM_UPGRADE = 'Upgrade'
    TERM_UPLOAD = 'Upload'
    TERM_WIPE_DESTROY_PURGE = 'Wipe/Destroy/Purge'
    TERM_WRITE = 'Write'


@register_vocab
class ActionObjectAssociationType(VocabString):
    _namespace = 'http://cybox.mitre.org/default_vocabularies-2'
    _XSI_TYPE = 'cyboxVocabs:ActionObjectAssociationTypeVocab-1.0'
    _VOCAB_VERSION = '1.0'

    TERM_AFFECTED = 'Affected'
    TERM_INITIATING = 'Initiating'
    TERM_RETURNED = 'Returned'
    TERM_UTILIZED = 'Utilized'


@register_vocab
class HashName(VocabString):
    _namespace = 'http://cybox.mitre.org/default_vocabularies-2'
    _XSI_TYPE = 'cyboxVocabs:HashNameVocab-1.0'
    _VOCAB_VERSION = '1.0'

    TERM_MD5 = 'MD5'
    TERM_MD6 = 'MD6'
    TERM_SHA1 = 'SHA1'
    TERM_SHA224 = 'SHA224'
    TERM_SHA256 = 'SHA256'
    TERM_SHA384 = 'SHA384'
    TERM_SHA512 = 'SHA512'
    TERM_SSDEEP = 'SSDEEP'


@register_vocab
class ActionArgumentName(VocabString):
    _namespace = 'http://cybox.mitre.org/default_vocabularies-2'
    _XSI_TYPE = 'cyboxVocabs:ActionArgumentNameVocab-1.0'
    _VOCAB_VERSION = '1.0'

    TERM_ACCESS_MODE = 'Access Mode'
    TERM_APC_ADDRESS = 'APC Address'
    TERM_APC_MODE = 'APC Mode'
    TERM_API = 'API'
    TERM_APPLICATION_NAME = 'Application Name'
    TERM_BASE_ADDRESS = 'Base Address'
    TERM_CALLBACK_ADDRESS = 'Callback Address'
    TERM_CODE_ADDRESS = 'Code Address'
    TERM_COMMAND = 'Command'
    TERM_CONTROL_CODE = 'Control Code'
    TERM_CONTROL_PARAMETER = 'Control Parameter'
    TERM_CREATION_FLAGS = 'Creation Flags'
    TERM_DATABASE_NAME = 'Database Name'
    TERM_DELAY_TIME_MS = 'Delay Time (ms)'
    TERM_DESTINATION_ADDRESS = 'Destination Address'
    TERM_ERROR_CONTROL = 'Error Control'
    TERM_FILE_INFORMATION_CLASS = 'File Information Class'
    TERM_FLAGS = 'Flags'
    TERM_FUNCTION_ADDRESS = 'Function Address'
    TERM_FUNCTION_NAME = 'Function Name'
    TERM_FUNCTION_ORDINAL = 'Function Ordinal'
    TERM_HOOK_TYPE = 'Hook Type'
    TERM_HOSTNAME = 'Hostname'
    TERM_HOST_NAME = 'Host Name'
    TERM_INITIAL_OWNER = 'Initial Owner'
    TERM_MAPPING_OFFSET = 'Mapping Offset'
    TERM_NUMBER_OF_BYTES_PER_SEND = 'Number of Bytes Per Send'
    TERM_OPTIONS = 'Options'
    TERM_PARAMETER_ADDRESS = 'Parameter Address'
    TERM_PASSWORD = 'Password'
    TERM_PRIVILEGE_NAME = 'Privilege Name'
    TERM_PROTECTION = 'Protection'
    TERM_PROXY_BYPASS = 'Proxy Bypass'
    TERM_PROXY_NAME = 'Proxy Name'
    TERM_REASON = 'Reason'
    TERM_REQUESTED_VERSION = 'Requested Version'
    TERM_REQUEST_SIZE = 'Request Size'
    TERM_SERVER = 'Server'
    TERM_SERVICE_NAME = 'Service Name'
    TERM_SERVICE_STATE = 'Service State'
    TERM_SERVICE_TYPE = 'Service Type'
    TERM_SHARE_MODE = 'Share Mode'
    TERM_SHUTDOWN_FLAG = 'Shutdown Flag'
    TERM_SIZE_BYTES = 'Size (bytes)'
    TERM_SLEEP_TIME_MS = 'Sleep Time (ms)'
    TERM_SOURCE_ADDRESS = 'Source Address'
    TERM_STARTING_ADDRESS = 'Starting Address'
    TERM_SYSTEM_METRIC_INDEX = 'System Metric Index'
    TERM_TARGET_PID = 'Target PID'
    TERM_TRANSFER_FLAGS = 'Transfer Flags'
    TERM_USERNAME = 'Username'


@register_vocab
class ActionRelationshipType(VocabString):
    _namespace = 'http://cybox.mitre.org/default_vocabularies-2'
    _XSI_TYPE = 'cyboxVocabs:ActionRelationshipTypeVocab-1.0'
    _VOCAB_VERSION = '1.0'

    TERM_DEPENDENT_ON = 'Dependent_On'
    TERM_EQUIVALENT_TO = 'Equivalent_To'
    TERM_FOLLOWED_BY = 'Followed_By'
    TERM_INITIATED = 'Initiated'
    TERM_INITIATED_BY = 'Initiated_By'
    TERM_PRECEDED_BY = 'Preceded_By'
    TERM_RELATED_TO = 'Related_To'


@register_vocab
class ObjectRelationship(VocabString):
    _namespace = 'http://cybox.mitre.org/default_vocabularies-2'
    _XSI_TYPE = 'cyboxVocabs:ObjectRelationshipVocab-1.1'
    _VOCAB_VERSION = '1.1'

    TERM_ALLOCATED = 'Allocated'
    TERM_ALLOCATED_BY = 'Allocated_By'
    TERM_BOUND = 'Bound'
    TERM_BOUND_BY = 'Bound_By'
    TERM_CHARACTERIZED_BY = 'Characterized_By'
    TERM_CHARACTERIZES = 'Characterizes'
    TERM_CHILD_OF = 'Child_Of'
    TERM_CLOSED = 'Closed'
    TERM_CLOSED_BY = 'Closed_By'
    TERM_COMPRESSED = 'Compressed'
    TERM_COMPRESSED_BY = 'Compressed_By'
    TERM_COMPRESSED_FROM = 'Compressed_From'
    TERM_COMPRESSED_INTO = 'Compressed_Into'
    TERM_CONNECTED_FROM = 'Connected_From'
    TERM_CONNECTED_TO = 'Connected_To'
    TERM_CONTAINED_WITHIN = 'Contained_Within'
    TERM_CONTAINS = 'Contains'
    TERM_COPIED = 'Copied'
    TERM_COPIED_BY = 'Copied_By'
    TERM_COPIED_FROM = 'Copied_From'
    TERM_COPIED_TO = 'Copied_To'
    TERM_CREATED = 'Created'
    TERM_CREATED_BY = 'Created_By'
    TERM_DECODED = 'Decoded'
    TERM_DECODED_BY = 'Decoded_By'
    TERM_DECOMPRESSED = 'Decompressed'
    TERM_DECOMPRESSED_BY = 'Decompressed_By'
    TERM_DECRYPTED = 'Decrypted'
    TERM_DECRYPTED_BY = 'Decrypted_By'
    TERM_DELETED = 'Deleted'
    TERM_DELETED_BY = 'Deleted_By'
    TERM_DELETED_FROM = 'Deleted_From'
    TERM_DOWNLOADED = 'Downloaded'
    TERM_DOWNLOADED_BY = 'Downloaded_By'
    TERM_DOWNLOADED_FROM = 'Downloaded_From'
    TERM_DOWNLOADED_TO = 'Downloaded_To'
    TERM_DROPPED = 'Dropped'
    TERM_DROPPED_BY = 'Dropped_By'
    TERM_ENCODED = 'Encoded'
    TERM_ENCODED_BY = 'Encoded_By'
    TERM_ENCRYPTED = 'Encrypted'
    TERM_ENCRYPTED_BY = 'Encrypted_By'
    TERM_ENCRYPTED_FROM = 'Encrypted_From'
    TERM_ENCRYPTED_TO = 'Encrypted_To'
    TERM_EXTRACTED_FROM = 'Extracted_From'
    TERM_FQDN_OF = 'FQDN_Of'
    TERM_FREED = 'Freed'
    TERM_FREED_BY = 'Freed_By'
    TERM_HOOKED = 'Hooked'
    TERM_HOOKED_BY = 'Hooked_By'
    TERM_INITIALIZED_BY = 'Initialized_By'
    TERM_INITIALIZED_TO = 'Initialized_To'
    TERM_INJECTED = 'Injected'
    TERM_INJECTED_AS = 'Injected_As'
    TERM_INJECTED_BY = 'Injected_By'
    TERM_INJECTED_INTO = 'Injected_Into'
    TERM_INSTALLED = 'Installed'
    TERM_INSTALLED_BY = 'Installed_By'
    TERM_JOINED = 'Joined'
    TERM_JOINED_BY = 'Joined_By'
    TERM_KILLED = 'Killed'
    TERM_KILLED_BY = 'Killed_By'
    TERM_LISTENED_ON = 'Listened_On'
    TERM_LISTENED_ON_BY = 'Listened_On_By'
    TERM_LOADED_FROM = 'Loaded_From'
    TERM_LOADED_INTO = 'Loaded_Into'
    TERM_LOCKED = 'Locked'
    TERM_LOCKED_BY = 'Locked_By'
    TERM_MAPPED_BY = 'Mapped_By'
    TERM_MAPPED_INTO = 'Mapped_Into'
    TERM_MERGED = 'Merged'
    TERM_MERGED_BY = 'Merged_By'
    TERM_MODIFIED_PROPERTIES_OF = 'Modified_Properties_Of'
    TERM_MONITORED = 'Monitored'
    TERM_MONITORED_BY = 'Monitored_By'
    TERM_MOVED = 'Moved'
    TERM_MOVED_BY = 'Moved_By'
    TERM_MOVED_FROM = 'Moved_From'
    TERM_MOVED_TO = 'Moved_To'
    TERM_OPENED = 'Opened'
    TERM_OPENED_BY = 'Opened_By'
    TERM_PACKED = 'Packed'
    TERM_PACKED_BY = 'Packed_By'
    TERM_PACKED_FROM = 'Packed_From'
    TERM_PACKED_INTO = 'Packed_Into'
    TERM_PARENT_OF = 'Parent_Of'
    TERM_PAUSED = 'Paused'
    TERM_PAUSED_BY = 'Paused_By'
    TERM_PREVIOUSLY_CONTAINED = 'Previously_Contained'
    TERM_PROPERTIES_MODIFIED_BY = 'Properties_Modified_By'
    TERM_PROPERTIES_QUERIED = 'Properties_Queried'
    TERM_PROPERTIES_QUERIED_BY = 'Properties_Queried_By'
    TERM_READ_FROM = 'Read_From'
    TERM_READ_FROM_BY = 'Read_From_By'
    TERM_RECEIVED = 'Received'
    TERM_RECEIVED_BY = 'Received_By'
    TERM_RECEIVED_FROM = 'Received_From'
    TERM_RECEIVED_VIA_UPLOAD = 'Received_Via_Upload'
    TERM_REDIRECTS_TO = 'Redirects_To'
    TERM_RELATED_TO = 'Related_To'
    TERM_RENAMED = 'Renamed'
    TERM_RENAMED_BY = 'Renamed_By'
    TERM_RENAMED_FROM = 'Renamed_From'
    TERM_RENAMED_TO = 'Renamed_To'
    TERM_RESOLVED_TO = 'Resolved_To'
    TERM_RESUMED = 'Resumed'
    TERM_RESUMED_BY = 'Resumed_By'
    TERM_ROOT_DOMAIN_OF = 'Root_Domain_Of'
    TERM_SEARCHED_FOR = 'Searched_For'
    TERM_SEARCHED_FOR_BY = 'Searched_For_By'
    TERM_SENT = 'Sent'
    TERM_SENT_BY = 'Sent_By'
    TERM_SENT_TO = 'Sent_To'
    TERM_SENT_VIA_UPLOAD = 'Sent_Via_Upload'
    TERM_SET_FROM = 'Set_From'
    TERM_SET_TO = 'Set_To'
    TERM_SUB_DOMAIN_OF = 'Sub-domain_Of'
    TERM_SUPRA_DOMAIN_OF = 'Supra-domain_Of'
    TERM_SUSPENDED = 'Suspended'
    TERM_SUSPENDED_BY = 'Suspended_By'
    TERM_UNHOOKED = 'Unhooked'
    TERM_UNHOOKED_BY = 'Unhooked_By'
    TERM_UNLOCKED = 'Unlocked'
    TERM_UNLOCKED_BY = 'Unlocked_By'
    TERM_UNPACKED = 'Unpacked'
    TERM_UNPACKED_BY = 'Unpacked_By'
    TERM_UPLOADED = 'Uploaded'
    TERM_UPLOADED_BY = 'Uploaded_By'
    TERM_UPLOADED_FROM = 'Uploaded_From'
    TERM_UPLOADED_TO = 'Uploaded_To'
    TERM_USED = 'Used'
    TERM_USED_BY = 'Used_By'
    TERM_VALUES_ENUMERATED = 'Values_Enumerated'
    TERM_VALUES_ENUMERATED_BY = 'Values_Enumerated_By'
    TERM_WRITTEN_TO_BY = 'Written_To_By'
    TERM_WROTE_TO = 'Wrote_To'


@register_vocab
class CharacterEncoding(VocabString):
    _namespace = 'http://cybox.mitre.org/default_vocabularies-2'
    _XSI_TYPE = 'cyboxVocabs:CharacterEncodingVocab-1.0'
    _VOCAB_VERSION = '1.0'

    TERM_ASCII = 'ASCII'
    TERM_UTF_16 = 'UTF-16'
    TERM_UTF_32 = 'UTF-32'
    TERM_UTF_8 = 'UTF-8'
    TERM_WINDOWS_1250 = 'Windows-1250'
    TERM_WINDOWS_1251 = 'Windows-1251'
    TERM_WINDOWS_1252 = 'Windows-1252'
    TERM_WINDOWS_1253 = 'Windows-1253'
    TERM_WINDOWS_1254 = 'Windows-1254'
    TERM_WINDOWS_1255 = 'Windows-1255'
    TERM_WINDOWS_1256 = 'Windows-1256'
    TERM_WINDOWS_1257 = 'Windows-1257'
    TERM_WINDOWS_1258 = 'Windows-1258'


@register_vocab
class ObjectState(VocabString):
    _namespace = 'http://cybox.mitre.org/default_vocabularies-2'
    _XSI_TYPE = 'cyboxVocabs:ObjectStateVocab-1.0'
    _VOCAB_VERSION = '1.0'

    TERM_ACTIVE = 'Active'
    TERM_CLOSED = 'Closed'
    TERM_DOES_NOT_EXIST = 'Does Not Exist'
    TERM_EXISTS = 'Exists'
    TERM_INACTIVE = 'Inactive'
    TERM_LOCKED = 'Locked'
    TERM_OPEN = 'Open'
    TERM_STARTED = 'Started'
    TERM_STOPPED = 'Stopped'
    TERM_UNLOCKED = 'Unlocked'


@register_vocab
class ToolType(VocabString):
    _namespace = 'http://cybox.mitre.org/default_vocabularies-2'
    _XSI_TYPE = 'cyboxVocabs:ToolTypeVocab-1.1'
    _VOCAB_VERSION = '1.1'

    TERM_ASSET_SCANNER = 'Asset Scanner'
    TERM_AV = 'AV'
    TERM_CONFIGURATION_SCANNER = 'Configuration Scanner'
    TERM_DBMS_MONITOR = 'DBMS Monitor'
    TERM_DIGITAL_FORENSICS = 'Digital Forensics'
    TERM_DYNAMIC_MALWARE_ANALYSIS = 'Dynamic Malware Analysis'
    TERM_FIREWALL = 'Firewall'
    TERM_GATEWAY = 'Gateway'
    TERM_HIDS = 'HIDS'
    TERM_HIPS = 'HIPS'
    TERM_INTELLIGENCE_SERVICE_PLATFORM = 'Intelligence Service Platform'
    TERM_NETWORK_CONFIGURATION_MANAGEMENT_TOOL = 'Network Configuration Management Tool'
    TERM_NETWORK_FLOW_CAPTURE_AND_ANALYSIS = 'Network Flow Capture and Analysis'
    TERM_NIDS = 'NIDS'
    TERM_NIPS = 'NIPS'
    TERM_PACKET_CAPTURE_AND_ANALYSIS = 'Packet Capture and Analysis'
    TERM_PROXY = 'Proxy'
    TERM_ROUTER = 'Router'
    TERM_SEM = 'SEM'
    TERM_SIM = 'SIM'
    TERM_SNMP_MIBS = 'SNMP/MIBs'
    TERM_STATIC_MALWARE_ANALYSIS = 'Static Malware Analysis'
    TERM_SYSTEM_CONFIGURATION_MANAGEMENT_TOOL = 'System Configuration Management Tool'
    TERM_VULNERABILITY_SCANNER = 'Vulnerability Scanner'


@register_vocab
class ActionName(VocabString):
    _namespace = 'http://cybox.mitre.org/default_vocabularies-2'
    _XSI_TYPE = 'cyboxVocabs:ActionNameVocab-1.1'
    _VOCAB_VERSION = '1.1'

    TERM_ACCEPT_SOCKET_CONNECTION = 'Accept Socket Connection'
    TERM_ADD_CONNECTION_TO_NETWORK_SHARE = 'Add Connection to Network Share'
    TERM_ADD_NETWORK_SHARE = 'Add Network Share'
    TERM_ADD_SCHEDULED_TASK = 'Add Scheduled Task'
    TERM_ADD_SYSTEM_CALL_HOOK = 'Add System Call Hook'
    TERM_ADD_USER = 'Add User'
    TERM_ADD_WINDOWS_HOOK = 'Add Windows Hook'
    TERM_ALLOCATE_VIRTUAL_MEMORY_IN_PROCESS = 'Allocate Virtual Memory in Process'
    TERM_BIND_ADDRESS_TO_SOCKET = 'Bind Address to Socket'
    TERM_CHANGE_SERVICE_CONFIGURATION = 'Change Service Configuration'
    TERM_CHECK_FOR_REMOTE_DEBUGGER = 'Check for Remote Debugger'
    TERM_CLOSE_PORT = 'Close Port'
    TERM_CLOSE_REGISTRY_KEY = 'Close Registry Key'
    TERM_CLOSE_SOCKET = 'Close Socket'
    TERM_CONFIGURE_SERVICE = 'Configure Service'
    TERM_CONNECT_TO_IP = 'Connect to IP'
    TERM_CONNECT_TO_NAMED_PIPE = 'Connect to Named Pipe'
    TERM_CONNECT_TO_NETWORK_SHARE = 'Connect to Network Share'
    TERM_CONNECT_TO_SOCKET = 'Connect to Socket'
    TERM_CONNECT_TO_URL = 'Connect to URL'
    TERM_CONTROL_DRIVER = 'Control Driver'
    TERM_CONTROL_SERVICE = 'Control Service'
    TERM_COPY_FILE = 'Copy File'
    TERM_CREATE_DIALOG_BOX = 'Create Dialog Box'
    TERM_CREATE_DIRECTORY = 'Create Directory'
    TERM_CREATE_EVENT = 'Create Event'
    TERM_CREATE_FILE = 'Create File'
    TERM_CREATE_FILE_ALTERNATE_DATA_STREAM = 'Create File Alternate Data Stream'
    TERM_CREATE_FILE_MAPPING = 'Create File Mapping'
    TERM_CREATE_FILE_SYMBOLIC_LINK = 'Create File Symbolic Link'
    TERM_CREATE_HIDDEN_FILE = 'Create Hidden File'
    TERM_CREATE_MAILSLOT = 'Create Mailslot'
    TERM_CREATE_MODULE = 'Create Module'
    TERM_CREATE_MUTEX = 'Create Mutex'
    TERM_CREATE_NAMED_PIPE = 'Create Named Pipe'
    TERM_CREATE_PROCESS = 'Create Process'
    TERM_CREATE_PROCESS_AS_USER = 'Create Process as User'
    TERM_CREATE_REGISTRY_KEY = 'Create Registry Key'
    TERM_CREATE_REGISTRY_KEY_VALUE = 'Create Registry Key Value'
    TERM_CREATE_REMOTE_THREAD_IN_PROCESS = 'Create Remote Thread in Process'
    TERM_CREATE_SERVICE = 'Create Service'
    TERM_CREATE_SOCKET = 'Create Socket'
    TERM_CREATE_SYMBOLIC_LINK = 'Create Symbolic Link'
    TERM_CREATE_THREAD = 'Create Thread'
    TERM_CREATE_WINDOW = 'Create Window'
    TERM_DELETE_DIRECTORY = 'Delete Directory'
    TERM_DELETE_FILE = 'Delete File'
    TERM_DELETE_NAMED_PIPE = 'Delete Named Pipe'
    TERM_DELETE_NETWORK_SHARE = 'Delete Network Share'
    TERM_DELETE_REGISTRY_KEY = 'Delete Registry Key'
    TERM_DELETE_REGISTRY_KEY_VALUE = 'Delete Registry Key Value'
    TERM_DELETE_SERVICE = 'Delete Service'
    TERM_DELETE_USER = 'Delete User'
    TERM_DISCONNECT_FROM_NAMED_PIPE = 'Disconnect from Named Pipe'
    TERM_DISCONNECT_FROM_NETWORK_SHARE = 'Disconnect from Network Share'
    TERM_DISCONNECT_FROM_SOCKET = 'Disconnect from Socket'
    TERM_DOWNLOAD_FILE = 'Download File'
    TERM_ENUMERATE_DLLS = 'Enumerate DLLs'
    TERM_ENUMERATE_NETWORK_SHARES = 'Enumerate Network Shares'
    TERM_ENUMERATE_PROCESSES = 'Enumerate Processes'
    TERM_ENUMERATE_PROTOCOLS = 'Enumerate Protocols'
    TERM_ENUMERATE_REGISTRY_KEY_SUBKEYS = 'Enumerate Registry Key Subkeys'
    TERM_ENUMERATE_REGISTRY_KEY_VALUES = 'Enumerate Registry Key Values'
    TERM_ENUMERATE_SERVICES = 'Enumerate Services'
    TERM_ENUMERATE_SYSTEM_HANDLES = 'Enumerate System Handles'
    TERM_ENUMERATE_THREADS = 'Enumerate Threads'
    TERM_ENUMERATE_THREADS_IN_PROCESS = 'Enumerate Threads in Process'
    TERM_ENUMERATE_USERS = 'Enumerate Users'
    TERM_ENUMERATE_WINDOWS = 'Enumerate Windows'
    TERM_FIND_FILE = 'Find File'
    TERM_FIND_WINDOW = 'Find Window'
    TERM_FLUSH_PROCESS_INSTRUCTION_CACHE = 'Flush Process Instruction Cache'
    TERM_FREE_LIBRARY = 'Free Library'
    TERM_FREE_PROCESS_VIRTUAL_MEMORY = 'Free Process Virtual Memory'
    TERM_GET_DISK_FREE_SPACE = 'Get Disk Free Space'
    TERM_GET_DISK_TYPE = 'Get Disk Type'
    TERM_GET_ELAPSED_SYSTEM_UP_TIME = 'Get Elapsed System Up Time'
    TERM_GET_FILE_ATTRIBUTES = 'Get File Attributes'
    TERM_GET_FUNCTION_ADDRESS = 'Get Function Address'
    TERM_GET_HOST_BY_ADDRESS = 'Get Host By Address'
    TERM_GET_HOST_BY_NAME = 'Get Host By Name'
    TERM_GET_HOST_NAME = 'Get Host Name'
    TERM_GET_LIBRARY_FILE_NAME = 'Get Library File Name'
    TERM_GET_LIBRARY_HANDLE = 'Get Library Handle'
    TERM_GET_NETBIOS_NAME = 'Get NetBIOS Name'
    TERM_GET_PROCESSES_SNAPSHOT = 'Get Processes Snapshot'
    TERM_GET_PROCESS_CURRENT_DIRECTORY = 'Get Process Current Directory'
    TERM_GET_PROCESS_ENVIRONMENT_VARIABLE = 'Get Process Environment Variable'
    TERM_GET_PROCESS_STARTUP_INFORMATION = 'Get Process Startup Information'
    TERM_GET_REGISTRY_KEY_ATTRIBUTES = 'Get Registry Key Attributes'
    TERM_GET_SERVICE_STATUS = 'Get Service Status'
    TERM_GET_SYSTEM_GLOBAL_FLAGS = 'Get System Global Flags'
    TERM_GET_SYSTEM_HOST_NAME = 'Get System Host Name'
    TERM_GET_SYSTEM_LOCAL_TIME = 'Get System Local Time'
    TERM_GET_SYSTEM_NETBIOS_NAME = 'Get System NetBIOS Name'
    TERM_GET_SYSTEM_NETWORK_PARAMETERS = 'Get System Network Parameters'
    TERM_GET_SYSTEM_TIME = 'Get System Time'
    TERM_GET_THREAD_CONTEXT = 'Get Thread Context'
    TERM_GET_THREAD_USERNAME = 'Get Thread Username'
    TERM_GET_USERNAME = 'Get Username'
    TERM_GET_USER_ATTRIBUTES = 'Get User Attributes'
    TERM_GET_WINDOWS_DIRECTORY = 'Get Windows Directory'
    TERM_GET_WINDOWS_SYSTEM_DIRECTORY = 'Get Windows System Directory'
    TERM_GET_WINDOWS_TEMPORARY_FILES_DIRECTORY = 'Get Windows Temporary Files Directory'
    TERM_HIDE_WINDOW = 'Hide Window'
    TERM_IMPERSONATE_PROCESS = 'Impersonate Process'
    TERM_IMPERSONATE_THREAD = 'Impersonate Thread'
    TERM_INJECT_MEMORY_PAGE = 'Inject Memory Page'
    TERM_KILL_PROCESS = 'Kill Process'
    TERM_KILL_THREAD = 'Kill Thread'
    TERM_KILL_WINDOW = 'Kill Window'
    TERM_LISTEN_ON_PORT = 'Listen on Port'
    TERM_LISTEN_ON_SOCKET = 'Listen on Socket'
    TERM_LOAD_AND_CALL_DRIVER = 'Load and Call Driver'
    TERM_LOAD_DRIVER = 'Load Driver'
    TERM_LOAD_LIBRARY = 'Load Library'
    TERM_LOAD_MODULE = 'Load Module'
    TERM_LOCK_FILE = 'Lock File'
    TERM_LOGON_AS_USER = 'Logon as User'
    TERM_MAP_FILE = 'Map File'
    TERM_MAP_LIBRARY = 'Map Library'
    TERM_MAP_VIEW_OF_FILE = 'Map View of File'
    TERM_MODIFY_FILE = 'Modify File'
    TERM_MODIFY_NAMED_PIPE = 'Modify Named Pipe'
    TERM_MODIFY_PROCESS = 'Modify Process'
    TERM_MODIFY_REGISTRY_KEY = 'Modify Registry Key'
    TERM_MODIFY_REGISTRY_KEY_VALUE = 'Modify Registry Key Value'
    TERM_MODIFY_SERVICE = 'Modify Service'
    TERM_MONITOR_REGISTRY_KEY = 'Monitor Registry Key'
    TERM_MOVE_FILE = 'Move File'
    TERM_OPEN_FILE = 'Open File'
    TERM_OPEN_FILE_MAPPING = 'Open File Mapping'
    TERM_OPEN_MUTEX = 'Open Mutex'
    TERM_OPEN_PORT = 'Open Port'
    TERM_OPEN_PROCESS = 'Open Process'
    TERM_OPEN_REGISTRY_KEY = 'Open Registry Key'
    TERM_OPEN_SERVICE = 'Open Service'
    TERM_OPEN_SERVICE_CONTROL_MANAGER = 'Open Service Control Manager'
    TERM_PROTECT_VIRTUAL_MEMORY = 'Protect Virtual Memory'
    TERM_QUERY_DISK_ATTRIBUTES = 'Query Disk Attributes'
    TERM_QUERY_DNS = 'Query DNS'
    TERM_QUERY_PROCESS_VIRTUAL_MEMORY = 'Query Process Virtual Memory'
    TERM_QUEUE_APC_IN_THREAD = 'Queue APC in Thread'
    TERM_READ_FILE = 'Read File'
    TERM_READ_FROM_NAMED_PIPE = 'Read From Named Pipe'
    TERM_READ_FROM_PROCESS_MEMORY = 'Read From Process Memory'
    TERM_READ_REGISTRY_KEY_VALUE = 'Read Registry Key Value'
    TERM_RECEIVE_DATA_ON_SOCKET = 'Receive Data on Socket'
    TERM_RECEIVE_EMAIL_MESSAGE = 'Receive Email Message'
    TERM_RELEASE_MUTEX = 'Release Mutex'
    TERM_RENAME_FILE = 'Rename File'
    TERM_REVERT_THREAD_TO_SELF = 'Revert Thread to Self'
    TERM_SEND_CONTROL_CODE_TO_FILE = 'Send Control Code to File'
    TERM_SEND_CONTROL_CODE_TO_PIPE = 'Send Control Code to Pipe'
    TERM_SEND_CONTROL_CODE_TO_SERVICE = 'Send Control Code to Service'
    TERM_SEND_DATA_ON_SOCKET = 'Send Data on Socket'
    TERM_SEND_DATA_TO_ADDRESS_ON_SOCKET = 'Send Data to Address on Socket'
    TERM_SEND_DNS_QUERY = 'Send DNS Query'
    TERM_SEND_EMAIL_MESSAGE = 'Send Email Message'
    TERM_SEND_ICMP_REQUEST = 'Send ICMP Request'
    TERM_SEND_REVERSE_DNS_QUERY = 'Send Reverse DNS Query'
    TERM_SET_FILE_ATTRIBUTES = 'Set File Attributes'
    TERM_SET_NETBIOS_NAME = 'Set NetBIOS Name'
    TERM_SET_PROCESS_CURRENT_DIRECTORY = 'Set Process Current Directory'
    TERM_SET_PROCESS_ENVIRONMENT_VARIABLE = 'Set Process Environment Variable'
    TERM_SET_SYSTEM_GLOBAL_FLAGS = 'Set System Global Flags'
    TERM_SET_SYSTEM_HOST_NAME = 'Set System Host Name'
    TERM_SET_SYSTEM_TIME = 'Set System Time'
    TERM_SET_THREAD_CONTEXT = 'Set Thread Context'
    TERM_SHOW_WINDOW = 'Show Window'
    TERM_SHUTDOWN_SYSTEM = 'Shutdown System'
    TERM_SLEEP_PROCESS = 'Sleep Process'
    TERM_SLEEP_SYSTEM = 'Sleep System'
    TERM_START_SERVICE = 'Start Service'
    TERM_UNLOAD_DRIVER = 'Unload Driver'
    TERM_UNLOAD_MODULE = 'Unload Module'
    TERM_UNLOCK_FILE = 'Unlock File'
    TERM_UNMAP_FILE = 'Unmap File'
    TERM_UPLOAD_FILE = 'Upload File'
    TERM_WRITE_TO_FILE = 'Write to File'
    TERM_WRITE_TO_PROCESS_VIRTUAL_MEMORY = 'Write to Process Virtual Memory'


@register_vocab
class InformationSourceType(VocabString):
    _namespace = 'http://cybox.mitre.org/default_vocabularies-2'
    _XSI_TYPE = 'cyboxVocabs:InformationSourceTypeVocab-1.0'
    _VOCAB_VERSION = '1.0'

    TERM_APPLICATION_FRAMEWORK = 'Application Framework'
    TERM_APPLICATION_LOGS = 'Application Logs'
    TERM_COMM_LOGS = 'Comm Logs'
    TERM_DBMS_LOG = 'DBMS Log'
    TERM_FRAMEWORKS = 'Frameworks'
    TERM_HELP_DESK = 'Help Desk'
    TERM_IAVM = 'IAVM'
    TERM_INCIDENT_MANAGEMENT = 'Incident Management'
    TERM_OS_DEVICE_DRIVER_APIS = 'OS/Device Driver APIs'
    TERM_TPM = 'TPM'
    TERM_VM_HYPERVISOR = 'VM Hypervisor'
    TERM_WEB_LOGS = 'Web Logs'
