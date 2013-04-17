"""Common utility methods"""

from .idgen import *
from .nsparser import NamespaceParser

import itertools

# Maps an ObjectType name to a tuple (module, class_name) where the class
# can be found
OBJECTS = {
            "AddressObjectType": 'cybox.objects.address_object.Address',
            "ArtifactType": 'cybox.objects.artifact.Artifact',
            "URIObjectType": 'cybox.objects.uri_object.URI',
            "EmailMessageObjectType": 'cybox.objects.email_message_object.EmailMessage',
            "FileObjectType": 'cybox.objects.file_object.File',
            "PortObjectType": 'cybox.objects.port_object.Port',
            "WindowsDriverObjectType" : 'cybox.objects.win_driver_object.WinDriver',
            "WindowsKernelHookObjectType" : 'cybox.objects.win_kernel_hook_object.WinKernelHook',
            "WindowsMutexObjectType" : 'cybox.objects.win_mutex_object.WinMutex',
            "WindowsProcessObjectType" : 'cybox.objects.win_process_object.WinProcess',
            "WindowsRegistryKeyObjectType" : 'cybox.objects.win_registry_key_object.WinRegistryKey',
            "WindowsServiceObjectType" : 'cybox.objects.win_service_object.WinService',
            "WindowsEventObjectType" : 'cybox.objects.win_event_object.WinEvent',
            # These are just for testing. Please don't attempt to use!
            "!!ObjectTestCase": 'cybox.utils.IDGenerator',
            "!!MissingModule": 'some.nonexistent.module',
            "!!BadClassName": 'cybox.utils.NonexistentClass',
          }

class UnknownObjectTypeError(Exception):
    pass

def get_class_for_object_type(object_type):
    """Gets the class where a given XML Type can be parsed

    Raises an UnknownObjectType if object_type has not been defined in the
        dictionary above.
    Raises an ImportError if the specified module is not available.
    Raises an AttributeError if the specified module does not contain the
         correct class.
    """
    full_class_name = OBJECTS.get(object_type)
    if not full_class_name:
        raise UnknownObjectTypeError("%s is not a known object type" %
                                        object_type)

    module = ".".join(full_class_name.split('.')[:-1])
    class_name = full_class_name.split('.')[-1]

    # May raise ImportError
    mod = __import__(module, fromlist=[class_name])

    # May raise AttributeError
    return getattr(mod, class_name)


def test_value(value):
    """
    Test if an input string value is not None and has a length grater than 0 or
    if a dictionary contains a "value" key whose value is not None and has
    a length greater than 0.

    We explicitly want to return True even if the value is False or 0, since
    some parts of the standards are boolean or allow a 0 value, and we want to
    distinguish the case where the "value" key is omitted entirely.
    """
    if isinstance(value, dict):
        v = value.get('value', None)
    elif isinstance(value, str):
        v = value
    elif isinstance(value, unicode):
        v = value
    elif isinstance(value, int):
        v = value
    elif isinstance(value, float):
        v = value
    else:
        v = None
    return (v is not None) and (len(str(v)) > 0)
