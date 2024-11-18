# Since XML is very verbose, you are given a way of encoding it where each tag gets
# mapped to a pre-defined integer value. The language/grammar is as follows:
# Element --> Tag Attributes END Children END
# Attribute --> Tag Value
# END --> 0
# Tag --> some predefined mapping to int
# Value --> string value
# For example, the following XML might be converted into the compressed string below (assuming a
# mapping of family - > 1, person - >2, firstName - > 3, lastName - > 4, state
# -> 5).
# <family lastName="McDowell" state="CA">
# <person firstName="Gayle">Some Message</person>
# </family>
# Becomes:
# 1 4 McDowell 5 CA 0 2 3 Gayle 0 Some Message 0 0
# Write code to print the encoded version of an XML element (passed in Element and Attribute
# objects).


class Element:
    def __init__(self, name, value):
        self.name = name
        self.attributes = []
        self.children = []
        self.value = value


class Attribute:
    def __init__(self, tag, value):
        self.tag = tag
        self.value = value

# encode each part of the XML in slightly different ways and add to string
def encode(root : Element, encoding):
    encode_str(root.name, encoding)
    for attribute in root.attributes:
        encode_attribute(attribute, encoding)
    encoding += '0'
    if(root.value is not None and root.value is not ''):
        encode_attribute(root.value, encoding)
    else:
        for element in root.children:
            encode(element, encoding)
    encoding += '0'
    return encoding


def encode_str(s : str, encoding):
    encoding += s
    encoding += ' '
        

def encode_attribute(attribute : Attribute, encoding):
    encoding += attribute.tag + ' '
    encoding += attribute.value
    

def encode_XML(element):
    return encode(element, '')


root = Element("family", "family")
mapping = {"family" : '1', "person" : '2', "firstName" : '3', "lastName" : '4', "state": '5'}
attr1 = Attribute(mapping["family"], "McDowell")
attr2 = Attribute(mapping["state"], "CA")
root.attributes = [attr1, attr2]
child1 = Attribute(mapping["firstName"], "Gayle")
root.children = [child1]

print(encode_XML(root))