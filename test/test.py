from xml.dom import minidom, xmlbuilder
from xml.sax import xmlreader

reader = xmlreader

builder  = xmlbuilder

mini = minidom

doc = mini.parse("test\\test.xml")