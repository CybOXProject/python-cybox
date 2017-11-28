# Copyright (c) 2017, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest

from cybox.objects.pdf_file_object import PDFFile

from cybox.test.objects import ObjectTestCase


class TestPDFFileInstance(ObjectTestCase, unittest.TestCase):
    object_type = 'PDFFileObjectType'
    klass = PDFFile

    _full_dict = {
        'indirect_objects': [
            {
                'id': {
                    'object_number': 1,
                    'generation_number': 0
                },
                'contents': {
                    'non_stream_contents': '<< /Type /Catalog /Outlines 2 0 R>>'
                }
            },
            {
                'id': {
                    'object_number': 2,
                    'generation_number': 0
                },
                'contents': {
                    'non_stream_contents': '<< /Type Outlines /Count 0>>'
                }
            }
        ],
        'file_name': 'test.pdf',
        'size_in_bytes': 25523,
        'trailers': [{
            'last_cross_reference_offset': 408,
            'root': {
                'object_number': 1,
                'generation_number': 0
            },
            'size': 3
        }],
        'version': 1.4,
        'cross_reference_tables': [{'subsections': [{
            'cross_reference_entries': [
                {
                    'byte_offset': 0,
                    'generation_number': 65535
                },
                {
                    'byte_offset': 9,
                    'generation_number': 0
                },
                {
                    'byte_offset': 74,
                    'generation_number': 0
                }
            ],
            'number_of_objects': 3,
            'first_object_number': 0
        }]}],
        'xsi:type': object_type
    }


class TestPDFFilePattern(ObjectTestCase, unittest.TestCase):
    object_type = 'PDFFileObjectType'
    klass = PDFFile

    _full_dict = {
        'xsi:type': object_type,
        'version': {
            'value': 1.2,
            'condition': 'GreaterThan'
        },
        'metadata': {
            'keyword_counts': {
                'js_count': {
                    'non_obfuscated_count': {
                        'value': 3,
                        'condition': 'GreaterThanOrEqual'
                    }
                }
            }
        }
    }


if __name__ == '__main__':
    unittest.main()
