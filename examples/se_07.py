import io
from pprint import pprint
import cybox.bindings.cybox_core_1_0 as cybox_core_binding
from cybox.core import Observables, ObservableComposition

def main():
    fn = 'se_07.xml'
    print "parsing input xml document..."
    observables_obj = cybox_core_binding.parse(fn) # build a binding object
    observables = Observables.from_obj(observables_obj) # build an api object from binding
    observables_dict = observables.to_dict() # create dictionary from api object
    
    pprint(observables_dict)

    print "building xml from dictionary..."
    
    observables_two = Observables.from_dict(observables_dict) # create copy api object from dictionary
    xml = observables_two.to_xml() # generate xml from copied api object
    print xml

if __name__ == '__main__':
    main()

