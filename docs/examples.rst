Examples
========================

This page includes some basic examples of creating and parsing CybOX content.

There are a couple things we do in these examples that shouldn't be done
in production code:

* When calling ``to_xml()``, we use ``include_namespaces=False``. This is to
  make the example output easier to read, but means the resulting output
  cannot be successfully parsed. The XML parser doesn't know what namespaces
  to use if they aren't included. In production code, you should explicitly
  set ``include_namespaces`` to ``True`` or omit it entirely (``True`` is the
  default).

* We use ``set_id_method(IDGenerator.METHOD_INT)`` to make IDs for Objects and
  Observables easier to read and cross-reference within the XML document. In
  production code, you should omit this statement, which causes random UUIDs to
  be created instead.


Creating Objects
-------------------

The easiest way to create an object is to construct one and then set various
properties on it.


.. testcode::

    from cybox.objects.file_object import File
    f = File()
    f.file_name = "malware.exe"
    f.file_path = "C:\Windows\Temp\malware.exe"
    print f.to_xml(include_namespaces=False)

Which outputs:

.. testoutput::

    <FileObj:FileObjectType xsi:type="FileObj:FileObjectType">
        <FileObj:File_Name>malware.exe</FileObj:File_Name>
        <FileObj:File_Path>C:\Windows\Temp\malware.exe</FileObj:File_Path>
    </FileObj:FileObjectType>


For some objects, such as the AddressObject, you can pass parameters direcly
into the constructor.

.. testcode::

    from cybox.objects.address_object import Address
    a = Address("1.2.3.4", Address.CAT_IPV4)
    print a.to_xml(include_namespaces=False)

.. testoutput::

    <AddressObj:AddressObjectType xsi:type="AddressObj:AddressObjectType" category="ipv4-addr">
        <AddressObj:Address_Value>1.2.3.4</AddressObj:Address_Value>
    </AddressObj:AddressObjectType>


Creating Observables
--------------------

Full CybOX documents are expected to have ``Observables`` as the root element.
You can pass any object to the ``Observables`` constructor to generate the
proper XML.

.. testcode::

    from cybox.core import Observables
    from cybox.objects.file_object import File
    from cybox.utils import IDGenerator, set_id_method
    set_id_method(IDGenerator.METHOD_INT)
    f = File()
    f.file_name = "malware.exe"
    f.file_path = "C:\Windows\Temp\malware.exe"
    print Observables(f).to_xml(include_namespaces=False)

.. testoutput::

    <cybox:Observables cybox_major_version="2" cybox_minor_version="1" cybox_update_version="0">
        <cybox:Observable id="example:Observable-1">
            <cybox:Object id="example:File-2">
                <cybox:Properties xsi:type="FileObj:FileObjectType">
                    <FileObj:File_Name>malware.exe</FileObj:File_Name>
                    <FileObj:File_Path>C:\Windows\Temp\malware.exe</FileObj:File_Path>
                </cybox:Properties>
            </cybox:Object>
        </cybox:Observable>
    </cybox:Observables>


To include multiple objects as individual Observables within one document, you
can pass them as a list to the Observables constructor.

.. testcode::

    from cybox.core import Observables
    from cybox.objects.address_object import Address
    from cybox.objects.uri_object import URI
    from cybox.utils import IDGenerator, set_id_method
    set_id_method(IDGenerator.METHOD_INT)
    a = Address("1.2.3.4", Address.CAT_IPV4)
    u = URI("http://cybox.mitre.org/")
    print Observables([a, u]).to_xml(include_namespaces=False)

.. testoutput::

    <cybox:Observables cybox_major_version="2" cybox_minor_version="1" cybox_update_version="0">
        <cybox:Observable id="example:Observable-1">
            <cybox:Object id="example:Address-2">
                <cybox:Properties xsi:type="AddressObj:AddressObjectType" category="ipv4-addr">
                    <AddressObj:Address_Value>1.2.3.4</AddressObj:Address_Value>
                </cybox:Properties>
            </cybox:Object>
        </cybox:Observable>
        <cybox:Observable id="example:Observable-3">
            <cybox:Object id="example:URI-4">
                <cybox:Properties xsi:type="URIObj:URIObjectType">
                    <URIObj:Value>http://cybox.mitre.org/</URIObj:Value>
                </cybox:Properties>
            </cybox:Object>
        </cybox:Observable>
    </cybox:Observables>


HTTP Message Body
-----------------

When outputing XML, by default, reserved XML characters such as < and > are
escaped by default.

.. testcode::

    from cybox.objects.http_session_object import HTTPMessage
    m = HTTPMessage()
    m.message_body = "<html><title>An HTML page</title><body><p>Body text</p></body></html>"
    m.length = len(m.message_body.value)
    print m.to_xml(include_namespaces=False)

.. testoutput::

    <HTTPSessionObj:HTTPMessageType>
        <HTTPSessionObj:Length>69</HTTPSessionObj:Length>
        <HTTPSessionObj:Message_Body>&lt;html&gt;&lt;title&gt;An HTML page&lt;/title&gt;&lt;body&gt;&lt;p&gt;Body text&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</HTTPSessionObj:Message_Body>
    </HTTPSessionObj:HTTPMessageType>


When you parse this content, these characters are converted back.

.. testcode::

    from cybox.bindings.http_session_object import parseString
    m2 =  HTTPMessage.from_obj(parseString(m.to_xml()))
    print m2.message_body

.. testoutput::

    <html><title>An HTML page</title><body><p>Body text</p></body></html>



HTTP User Agent
---------------

.. testcode::

    from cybox.objects.http_session_object import * 
    fields = HTTPRequestHeaderFields()
    fields.user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:25.0) Gecko/20100101 Firefox/25.0'

    header = HTTPRequestHeader()
    header.parsed_header = fields

    request = HTTPClientRequest()
    request.http_request_header = header

    req_res = HTTPRequestResponse()
    req_res.http_client_request = request

    session = HTTPSession()
    session.http_request_response = [req_res]

    print session.to_xml(include_namespaces=False)

.. testoutput::

    <HTTPSessionObj:HTTPSessionObjectType xsi:type="HTTPSessionObj:HTTPSessionObjectType">
        <HTTPSessionObj:HTTP_Request_Response>
            <HTTPSessionObj:HTTP_Client_Request>
                <HTTPSessionObj:HTTP_Request_Header>
                    <HTTPSessionObj:Parsed_Header>
                        <HTTPSessionObj:User_Agent>Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:25.0) Gecko/20100101 Firefox/25.0</HTTPSessionObj:User_Agent>
                    </HTTPSessionObj:Parsed_Header>
                </HTTPSessionObj:HTTP_Request_Header>
            </HTTPSessionObj:HTTP_Client_Request>
        </HTTPSessionObj:HTTP_Request_Response>
    </HTTPSessionObj:HTTPSessionObjectType>


Objects with DateTime properties
--------------------------------
When setting DateTime properties on objects, you can either use a native Python
``datetime.datetime`` or a string.  The ``python-dateutil`` library is used
to parse strings into dates, so a wide variety of formats is supported.

.. testcode::

    import datetime
    from cybox.objects.email_message_object import EmailMessage
    e = EmailMessage()
    e.from_ = "spammer@spam.com"
    e.subject = "This is not spam"
    e.date = datetime.datetime(2012, 1, 17, 8, 35, 6)
    print e.to_xml(include_namespaces=False)

.. testoutput::

    <EmailMessageObj:EmailMessageObjectType xsi:type="EmailMessageObj:EmailMessageObjectType">
        <EmailMessageObj:Header>
            <EmailMessageObj:From xsi:type="AddressObj:AddressObjectType" category="e-mail">
                <AddressObj:Address_Value>spammer@spam.com</AddressObj:Address_Value>
            </EmailMessageObj:From>
            <EmailMessageObj:Subject>This is not spam</EmailMessageObj:Subject>
            <EmailMessageObj:Date>2012-01-17T08:35:06</EmailMessageObj:Date>
        </EmailMessageObj:Header>
    </EmailMessageObj:EmailMessageObjectType>

.. testcode::

    from cybox.objects.email_message_object import EmailMessage
    e = EmailMessage()
    e.date = "Mon, 14 Oct, 2013 12:32:03 -0500"
    print e.to_xml(include_namespaces=False)

.. testoutput::

    <EmailMessageObj:EmailMessageObjectType xsi:type="EmailMessageObj:EmailMessageObjectType">
        <EmailMessageObj:Header>
            <EmailMessageObj:Date>2013-10-14T12:32:03-05:00</EmailMessageObj:Date>
        </EmailMessageObj:Header>
    </EmailMessageObj:EmailMessageObjectType>


Windows File Object example
---------------------------

The WindowsFile object is a subclass of the File object.  As you can see,
the correct namepaces for the various properties are set.

.. testcode::

    from cybox.objects.win_file_object import WinFile
    f = WinFile()
    f.file_name = "blah.exe"
    f.drive = "C:\\"
    print f.to_xml(include_namespaces=False)

.. testoutput::

    <WinFileObj:WindowsFileObjectType xsi:type="WinFileObj:WindowsFileObjectType">
        <FileObj:File_Name>blah.exe</FileObj:File_Name>
        <WinFileObj:Drive>C:\</WinFileObj:Drive>
    </WinFileObj:WindowsFileObjectType>


Hashes
------
In many cases you can pass a dictionary or a list to create an instance of a
CybOX type.

.. testcode::

    from cybox.common import HashList
    h = HashList.from_list([{'type' : 'MD5', 'simple_hash_value' : 'FFFFFF'},
                            {'type' : 'SHA1', 'simple_hash_value' : 'FFFFFF'}])
    print h.to_xml(include_namespaces=False)

.. testoutput::

    <cyboxCommon:HashListType>
        <cyboxCommon:Hash>
            <cyboxCommon:Type xsi:type="cyboxVocabs:HashNameVocab-1.0">MD5</cyboxCommon:Type>
            <cyboxCommon:Simple_Hash_Value>FFFFFF</cyboxCommon:Simple_Hash_Value>
        </cyboxCommon:Hash>
        <cyboxCommon:Hash>
            <cyboxCommon:Type xsi:type="cyboxVocabs:HashNameVocab-1.0">SHA1</cyboxCommon:Type>
            <cyboxCommon:Simple_Hash_Value>FFFFFF</cyboxCommon:Simple_Hash_Value>
        </cyboxCommon:Hash>
    </cyboxCommon:HashListType>

This can easily be incorporated into constructing objects as well.

.. testcode::

    from cybox.objects.win_file_object import WinFile
    f = WinFile()
    f.file_name = "foo.exe"
    f.drive = "C:\\"
    f.hashes = h
    print f.to_xml(include_namespaces=False)

.. testoutput::

    <WinFileObj:WindowsFileObjectType xsi:type="WinFileObj:WindowsFileObjectType">
        <FileObj:File_Name>foo.exe</FileObj:File_Name>
        <FileObj:Hashes>
            <cyboxCommon:Hash>
                <cyboxCommon:Type xsi:type="cyboxVocabs:HashNameVocab-1.0">MD5</cyboxCommon:Type>
                <cyboxCommon:Simple_Hash_Value>FFFFFF</cyboxCommon:Simple_Hash_Value>
            </cyboxCommon:Hash>
            <cyboxCommon:Hash>
                <cyboxCommon:Type xsi:type="cyboxVocabs:HashNameVocab-1.0">SHA1</cyboxCommon:Type>
                <cyboxCommon:Simple_Hash_Value>FFFFFF</cyboxCommon:Simple_Hash_Value>
            </cyboxCommon:Hash>
        </FileObj:Hashes>
        <WinFileObj:Drive>C:\</WinFileObj:Drive>
    </WinFileObj:WindowsFileObjectType>


Parsing example
---------------

Just as you can call ``to_xml()`` to generate XML, you can call ``parseString``
to parse an XML string.

.. doctest::

    >>> import cybox.bindings.file_object as file_binding
    >>> from cybox.objects.file_object import File
    >>> a = """
    ... <FileObj:FileObjectType 
    ...     xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    ...     xmlns:FileObj="http://cybox.mitre.org/objects#FileObject-2"
    ...     xsi:type="FileObj:FileObjectType">
    ...     <FileObj:File_Name condition="Contains">bad.exe</FileObj:File_Name>
    ... </FileObj:FileObjectType>
    ... """
    >>> file_obj = file_binding.parseString(a)
    >>> type(file_obj)
    <class 'cybox.bindings.file_object.FileObjectType'>
    >>> f = File.from_obj(file_obj)
    >>> f.file_name.value
    'bad.exe'
    >>> str(f.file_name)
    'bad.exe'
    >>> f.file_name.condition
    'Contains'


Comparisons
-----------

CybOX objects can be compared for equality using the standard Python equality
operator. By default, every field must be equal between the two objects.
However, you can explicitly say that some fields should not be considered.

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
