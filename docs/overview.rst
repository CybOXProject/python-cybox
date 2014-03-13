Overview
========

This page provides a quick overview needed to understand the inner workings
of the python-cybox library. If you prefer a more hands-on approach, browse the
:doc:`examples`.

CybOX Entities
--------------

Each type within CybOX is represented by a class which derives from
:class:`cybox.Entity`. In general, there is one Python class per CybOX type,
though in some cases classes which would have identical functionality have
been reused rather than writing duplicating classes. One example of this is
that many enumerated values are implemented using the
:class:`cybox.common.properties.String`, since values aren't checked to make
sure they are valid enumeration values. 

.. note:: Not all CybOX types have yet been implemented.
