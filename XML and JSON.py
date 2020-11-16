
# XML eXtensible Markup Language (XML)
# Note from FreeCodeCamp
# Primary purpose is to help information systems share structured data
# It started as a simplified subset of the Standard Generalized Markup Language(SGML), and is designed to be relatively
# human-legible

# Tags indicate the beginning and ending of elements
# Attributes - Keywords/value pairs on the opening tag of XML
# Serialize/ De-Serialize - Convert data in one program into a common format that can be storted and/or transmitted between systems
# in a programming language-independent manner

# Start Tag              <person>
# End Tag                     <name>Chuck</name>
# Text Content                <phone type="intl">
#                                 +1 734 303 4456
# Attributes                  </phone>
#                             <email hide="yes" />
# Self Closing Tag        </person>

# XML Schema

# commonly XSD structure
# xs:element
# xs:sequence
# xs:complex Type

# for instance

# <xs:complexType name = "person">
#     <xs:sequence>
#         <xs:element name="lastname" type="xs:string"/>
#         <xs:element name="age" type="xs:integer"/>
#         <xs:element name="dateborn" type="xs:data"/>
#     <xs:sequence>
# <xs:complexType>
# this is like a contract

# with the contract above, here is a piece of XML
# <person>
#     <lastname>Severance</lastname>
#     <age>17</age>
#     <dateborn>2001-4-17</dateborn>
# </person>

import xml.etree.ElementTree as ET
data = '''<person>
    <name>Chuck</name>
    <phone type="int1">
        +1 734 303 4456
    </phone>
    <email hide="yes"/>
</person>'''

tree = ET.fromstring(data)
print('Name:', tree.find('name').text)
print('Attr:', tree.find('email').get('hide'))

# JavaScript Object Notation--(JSON)

import json
data1 = '''{
"name" : "chuck",
"phone" : {
    "type" : "int1",
   "number": "+1 734 303 4456"
            },
"email" : {
    "hide" : "yes"
            }
}'''

info = json.loads(data1)
print("name:", info["name"])
print("hide:", info["email"]["hide"])
print(info)