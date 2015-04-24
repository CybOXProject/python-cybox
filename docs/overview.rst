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

Controlled Vocabulary Strings
-----------------------------

Controlled Vocabulary strings are a concept originally designed for STIX and
adapted for use in CybOX as well. For background, see the `STIX
documentation`_. Controlled Vocabulary strings are implemented in the ``cybox``
Python package very similarly to how they are implemented in the ``stix``
package, so viewing the `python-stix documentation`_ should help explain how to
work with CybOX Controlled Vocabulary strings as well. CybOX vocabularies are
defined in the :mod:`cybox.common.vocabs` module.

.. _STIX documentation: https://stixproject.github.io/documentation/concepts/controlled-vocabularies/
.. _python-stix documentation: https://stix.readthedocs.org/en/latest/examples/index.html#controlled-vocabularies-vocabstring

