# Copyright (c) 2013, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import cybox
import cybox.bindings.cybox_common as common_binding

import datetime
import dateutil.parser

class Time(cybox.Entity):
    '''CybOX Common TimeType object representation'''
    _namespace = 'http://cybox.mitre.org/common-2'
    
    def __init__(self, start_time=None, end_time=None, produced_time=None, received_time=None):
        super(Time, self).__init__()
        self.start_time = start_time
        self.end_time = end_time
        self.produced_time = produced_time
        self.received_time = received_time
    
    def _parse_value(self, value):
        if not value:
            return None
        elif isinstance(value, datetime.datetime):
            return value
        
        return dateutil.parser.parse(value)

    def _serialize_value(self, value):
        if not value:
            return None
        return value.isoformat()
    
    @property
    def start_time(self):
        return self._start_time
    
    @start_time.setter
    def start_time(self, value):
        self._start_time = self._parse_value(value)
    
    @property
    def end_time(self):
        return self._end_time
    
    @end_time.setter
    def end_time(self, value):
        self._end_time = self._parse_value(value)
    
    @property
    def produced_time(self):
        return self._produced_time
    
    @produced_time.setter
    def produced_time(self, value):
        self._produced_time = self._parse_value(value)
    
    @property
    def received_time(self):
        return self._received_time
    
    @received_time.setter
    def received_time(self, value):
        self._received_time = self._parse_value(value)  
    
    @staticmethod
    def from_dict(dict_repr):
        if not dict_repr:
            return None
        return_obj = Time()
        return_obj.start_time = dict_repr.get('start_time', None)
        return_obj.end_time = dict_repr.get('end_time', None)
        return_obj.produced_time = dict_repr.get('produced_time', None)
        return_obj.received_time = dict_repr.get('received_time', None)
        
        return return_obj
    
    def to_dict(self):
        return_dict = {}
        
        if self.start_time:
            return_dict['start_time'] = self._serialize_value(self.start_time)
        
        if self.end_time:
            return_dict['end_time'] = self._serialize_value(self.end_time)
        
        if self.produced_time:
            return_dict['produced_time'] = self._serialize_value(self.produced_time)
        
        if self.received_time:
            return_dict['received_time'] = self._serialize_value(self.received_time)
        
        return return_dict
    
    @staticmethod
    def from_obj(obj):
        if not obj:
            return None
        return_obj = Time()
        return_obj.start_time = obj.get_Start_Time()
        return_obj.end_time = obj.get_End_Time()
        return_obj.produced_time = obj.get_Produced_Time()
        return_obj.received_time = obj.get_Received_Time()
            
        return return_obj
    
    def to_obj(self):
        timetype_obj = common_binding.TimeType()
        timetype_obj.set_Start_Time(self.start_time)
        timetype_obj.set_End_Time(self.end_time)
        timetype_obj.set_Produced_Time(self.produced_time)
        timetype_obj.set_Received_Time(self.received_time)
        
        return timetype_obj
    
    
        
        
        
        
