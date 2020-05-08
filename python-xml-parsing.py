# Created on Jul 24, 2013

# @author: tuna

'''
<?xml version="1.0" encoding="UTF-8"?>
<SERVERCONFIG>
<SERVERS>
<SERVER NAME="server1" ENABLED="Y">
<IP>10.1.2.1</IP>
<USERNAME>admin</USERNAME>
<PASSWORD>12345</PASSWORD>
<DESCRIPTION>Application Server1</DESCRIPTION>
</SERVER>
<SERVER NAME="server2" ENABLED="Y">
<IP>10.1.2.2</IP>
<USERNAME>admin</USERNAME>
<PASSWORD>54321</PASSWORD>
<DESCRIPTION>Application Server1</DESCRIPTION>
</SERVER>
<SERVER NAME="server3" ENABLED="N">
<IP>10.1.2.3</IP>
<USERNAME>admin</USERNAME>
<PASSWORD>012345</PASSWORD>
<DESCRIPTION>Application Server3</DESCRIPTION>
</SERVER>
<SERVER NAME="server4" ENABLED="Y">
<IP>10.1.2.4</IP>
<USERNAME>admin</USERNAME>
<PASSWORD>0123456</PASSWORD>
<DESCRIPTION>Application Server4</DESCRIPTION>
</SERVER>
<SERVER NAME="server5" ENABLED="N">
<IP>10.1.2.5</IP>
<USERNAME>admin</USERNAME>
<PASSWORD>01234567</PASSWORD>
<DESCRIPTION>Application Server5</DESCRIPTION>
</SERVER>
</SERVERS>
</SERVERCONFIG>
'''

# XML Parsing example
from xml.dom.minidom import parse, parseString
import xml.parsers.expat

# loading XML to variable
XML = parse('C://config.xml')

domRunTimeList = parseString('<xmlRunTime><data>hi xml</data></xmlRunTime>')

# format XML runTime
print(domRunTimeList.toprettyxml("\t", "\n", None))

print("\n")  # new line

print("ENABLED SERVER LIST\n")
for node in XML.getElementsByTagName('SERVER'):
    if node.getAttribute("ENABLED") == "Y":
        print("IP --> ", str(node.getElementsByTagName("IP")[0].firstChild.nodeValue), "NAME",
              node.getAttribute("NAME"))

print("\n")  # new line
print("all IP LISTING STARTS\n")
for node in XML.getElementsByTagName('SERVER'):
    print("IP --> ", str(node.getElementsByTagName("IP")[0].firstChild.nodeValue))

print("\n")  # new line


# XML parsing with on the fly events

# Handlers
def start(name, attrs):
    print('Start Element:', name, attrs)


def end(name):
    print('End Element:', name)


def text(txt):
    print('Text:', str(txt))


# create a parser
parser = xml.parsers.expat.ParserCreate()

# map related handlers events
parser.StartElementHandler = start
parser.EndElementHandler = end
parser.CharacterDataHandler = text

parser.Parse("<xmlRunTime><data att='this is attribute1' att2='This is attribute 2'>hi xml</data></xmlRunTime>")
