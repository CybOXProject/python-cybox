Examples
========================

Windows File Object example
---------------------------

This is a simple example of creating a WindowsFile object.

>>> from cybox.common.properties import String
>>> from cybox.objects.win_file_object import WinFile
>>> f = WinFile()
>>> f.file_name = "blah.exe"
>>> f.drive = String("C:\\")
>>> print f.to_xml(include_namespaces=False)
<WinFileObj:WindowsFileObjectType xsi:type="WinFileObj:WindowsFileObjectType">
    <FileObj:File_Name>blah.exe</FileObj:File_Name>
    <WinFileObj:Drive>C:\</WinFileObj:Drive>
</WinFileObj:WindowsFileObjectType>
