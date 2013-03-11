import cybox
import cybox.bindings.cybox_core_1_0 as core_binding
import cybox.bindings.cybox_common_types_1_0 as common_binding


class StructuredGroup(cybox.Entity):
    LANG_C = 'C'
    LANG_CPP = 'C++'
    LANG_C_SHARP = 'C#'
    LANG_JAVA = 'Java'
    LANG_JSP = 'JSP'
    LANG_JAVASCRIPT = 'Javascript'
    LANG_ASP_NET = 'ASP.NET'
    LANG_SQL = 'SQL'
    LANG_PYTHON = 'Python'
    LANG_PERL = 'Perl'
    LANG_PHP = 'PHP'
    LANG_SOAP = 'SOAP'
    LANG_RUBY = 'RUBY'
    LANG_SHELL = 'SHELL'
    LANG_PSEUDO_CODE = 'PseudoCode'
    LANG_DOT_NET = '.NET'
    LANG_ASSEMBLY = 'ASSEMBLY'
    LANG_XML = 'XML'
    LANG_HTML = 'HTML'
    
    CODE_LANUAGES = (LANG_ASP_NET, LANG_ASSEMBLY, LANG_C, LANG_C_SHARP, LANG_CPP, LANG_DOT_NET, LANG_HTML,
                     LANG_JAVA, LANG_JAVASCRIPT, LANG_JSP, LANG_PERL, LANG_PHP, LANG_PSEUDO_CODE, LANG_PYTHON,
                     LANG_RUBY, LANG_SHELL, LANG_SOAP, LANG_SQL, LANG_XML)
    
    def __init__(self, titles=[], text=[], code_example_languages=[], code=[], comments=[], images=[]):
        self.titles = []
        self.text = []
        self.code_example_languages = []
        self.code = []
        self.comments = []
        #self.images = [] # not implemented
        
        for ti in titles:
            self.add_title(ti)
            
        for t in text:
            self.add_text(t)
            
        for cl in code_example_languages:
            self.add_code_example_language(cl)
        
        for c in code:
            self.add_code(c)
            
        for co in comments:
            self.add_comment(co)
        
    def add_text(self, value):
        self.text.append(value)
    
    def add_title(self, value):
        self.titles.append(value)
    
    def add_code_example_language(self, value):
        if value not in self.CODE_LANUAGES:
            raise ValueError('value must be one of: %s' % ' '.join(self.CODE_LANUAGES))
            
        self.code_example_languages.append(value)
    
    def add_code(self, value):
        self.code.append(value)
    
    def add_comment(self, value):
        self.comments.append(value)

    def to_dict(self, return_dict={}):
        if self.titles:
            for ti in self.titles:
                return_dict.setdefault('titles', []).append(ti)
        
        if self.text:
            for t in self.text:
                return_dict.setdefault('text', []).append(t)
                
        if self.code_example_languages:
            for cl in self.code_example_languages:
                return_dict.setdefault('code_example_languages', []).append(cl)
        
        if self.code:
            for c in self.code:
                return_dict.setdefault('code', []).append(c)
                
        if self.comments:
            for co in self.comments:
                return_dict.setdefault('comments', []).append(co)
                
        return return_dict
        
    @classmethod
    def from_dict(cls, dict_repr, return_obj):
        if not isinstance(return_obj, StructuredGroup):
            raise ValueError('return_obj must be instance of StructuredGroup')
        
        for ti in dict_repr.get('titles', []):
            return_obj.add_title(ti)
        
        for t in dict_repr.get('text', []):
            return_obj.add_text(t)
            
        for cl in dict_repr.get('code_example_language', []):
            return_obj.add_code_example_language(cl)
            
        for c in dict_repr.get('code', []):
            return_obj.add_code(c)
            
        for co in dict_repr.get('comments', []):
            return_obj.add_comment(co)
            
        return return_obj

    def to_obj(self, return_obj):
        if not (isinstance(return_obj, common_binding.StructuredTextType) or
                isinstance(return_obj, common_binding.Block)):
            raise ValueError('return_obj must be instance of common_binding.StructuredTextType or common_binding.Block')
        
        if self.text:
            for t in self.text:
                return_obj.add_Text(t)
        
        if self.titles:
            for ti in self.titles:
                return_obj.add_Text_Title(ti)
        
        if self.code_example_languages:
            for cl in self.code_example_languages:
                return_obj.add_Code_Example_Language(cl)
        
        if self.code:
            for c in self.code:
                return_obj.add_Code(c)
                
        if self.comments:
            for co in self.comments:
                return_obj.add_Comment(co)
                 
        return return_obj

    @classmethod
    def from_obj(cls, obj, return_obj):
        if not (isinstance(obj, common_binding.StructuredTextType) or
                isinstance(obj, common_binding.Block)):
            raise ValueError('obj must be instance of common_binding.StructuredTextType or common_binding.Block')
        
        if not isinstance(return_obj, StructuredGroup):
            raise ValueError('return_obj must be instance of StructuredGroup')
        
        if obj.get_Text():
            for t in obj.get_Text():
                return_obj.add_text(t)
        
        if obj.get_Text_Title():
            for ti in obj.get_Text_Title():
                return_obj.add_title(ti)
        
        if obj.get_Code_Example_Language():
            for cl in obj.get_Code_Example_Language():
                return_obj.add_code_example_language(cl)
                
        if obj.get_Code():
            for c in obj.get_Code():
                return_obj.add_code(c)
                
        if obj.get_Comment():
            for co in obj.get_Comment():
                return_obj.add_comment(co)
                
        return return_obj
        
        
class Block(StructuredGroup):
    NATURE_GOOD_CODE = 'Good_Code'
    NATURE_BAD_CODE = 'Bad_Code'
    NATURE_MITIGATION_CODE = 'Mitigation_Code'
    NATURE_ATTACK = 'Attack'
    NATURE_RESULT = 'Result'
    NATURE_LIST = 'List'
    
    BLOCK_NATURE_TYPES = (NATURE_ATTACK, NATURE_BAD_CODE, NATURE_GOOD_CODE, NATURE_LIST,
                          NATURE_MITIGATION_CODE, NATURE_RESULT)
    
    def __init__(self, block_nature=None, block=None, text=[], titles=[], code_example_languages=[], code=[], comments=[]):
        super(Block, self).__init__(text=text, titles=titles, code_example_languages=code_example_languages, code=code, comments=comments)
        self.block_nature = block_nature
        self.block = block
        
    @property
    def block(self):
        return self._block
    
    @block.setter
    def block(self, value):
        if value and not isinstance(value, Block):
            raise ValueError('value must be instance of Block')
        
        self._block = value
        
    @property
    def block_nature(self):
        return self._block_nature
    
    @block_nature.setter
    def block_nature(self, value):
        if value and value not in self.BLOCK_NATURE_TYPES:
            raise ValueError('value must be one of: %s' % ' '.join(self.BLOCK_NATURE_TYPES))
        
        self._block_nature = value

    def to_obj(self):
        return_obj = common_binding.Block()
        super(Block, self).to_obj(return_obj)
        
        return_obj.set_block_nature(self.block_nature)
        
        if self.block:
            return_obj.set_Block(self.block.to_obj())
            
        return return_obj
    
    @classmethod
    def from_obj(cls, obj):
        return_obj = Block()
        super(Block, cls).from_obj(obj, return_obj) # annotate with StructuredTextGroup field values
        
        return_obj.block_nature = obj.get_block_nature()
        
        if obj.get_Block():
            return_obj.block = Block.from_obj(obj.get_Block())
            
        return return_obj
    
    def to_dict(self):
        return_dict = {}
        super(Block, self).to_dict(return_dict)
        
        if self.block_nature:
            return_dict['block_nature'] = self.block_nature
            
        if self.block:
            return_dict['block'] = self.block.to_dict()
        
        return return_dict
    
    @classmethod
    def from_dict(cls, dict_repr):
        return_obj = Block()
        super(Block, cls).from_dict(dict_repr, return_obj)
        
        return_obj.block_nature = dict_repr.get('block_nature', None)
        
        block_dict = dict_repr.get('block', None)
        if block_dict:
            return_obj.block = Block.from_dict(block_dict)
            
        return return_obj


class StructuredText(StructuredGroup):
    def __init__(self, text=[], titles=[], code_example_languages=[], code=[], comments=[], block=None):
        super(StructuredText, self).__init__(text=text, titles=titles, code_example_languages=code_example_languages, code=code, comments=comments)
        self.block = block
         
    @property
    def block(self):
        return self._block
    
    @block.setter
    def block(self, value):
        if value and not isinstance(value, Block):
            raise ValueError('block must be instance of Block')
        
        self._block = value
        
    @classmethod
    def from_obj(cls, obj):
        return_obj = StructuredText()
        super(StructuredText, cls).from_obj(obj, return_obj)
        
        if obj.get_Block():
            return_obj.block = Block.from_obj(obj.get_Block())
        
        return return_obj
    
    def to_obj(self):
        return_obj = common_binding.StructuredTextType()
        super(StructuredText, self).to_obj(return_obj)
        
        if self.block:
            return_obj.set_Block(self.block.to_obj())
            
        return return_obj
    
    @classmethod
    def from_dict(cls, dict_repr):
        return_obj = StructuredText()
        super(StructuredText, cls).from_dict(dict_repr, return_obj)
    
        block_dict = dict_repr.get('block', None)
        if block_dict:
            return_obj.block = Block.from_dict(block_dict)
        
        return return_obj
    
    def to_dict(self):
        return_dict = {}
        super(StructuredText, self).to_dict(return_dict)
        
        if self.block:
            return_dict['block'] = self.block.to_dict()
            
        return return_dict
         

    