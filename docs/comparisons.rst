Comparing CybOX Entities
========================

An example:

.. doctest::

    >>> from cybox.objects.file_object import File

    >>> file_1 = File.from_dict({'file_name': 'abcd.dll', 'size_in_bytes': '25556'})
    >>> file_2 = File.from_dict({'file_name': 'abcd.dll', 'size_in_bytes': '25556'})
    >>> file_3 = File.from_dict({'file_name': 'abcd.dll', 'size_in_bytes': '1337'})

    # First, disable the use of ``size_in_bytes`` comparisons.
    >>> File.size_in_bytes.comparable = False

    >>> file_1 == file_2
    True
    >>> file_1 == file_3
    True

    # Now, set it back to True (the default).
    >>> File.size_in_bytes.comparable = True

    >>> file_1 == file_2
    True
    >>> file_1 == file_3
    False
