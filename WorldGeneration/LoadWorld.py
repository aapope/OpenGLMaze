'''A class containing static methods for loading World xml files'''
__author__ = "the World Generator Team (Zach, Ethan, Emily), based on LoadBlocks.py by Andrew and Emily"
__date__ = "21 October 2011"

from Block import Block
from Key import Key
from Door import Door
from xml.dom.minidom import parse
import string

class LoadWorld:
    '''A class containing static methods for loading blockworld xml files'''

    @staticmethod
    def load(f_name):
        '''Call this static method to load a list of blocks, keys, etc from an xml file (f_name). Returns a list of Blocks.'''
        dom1 = parse(f_name)
        object_list = LoadWorld.load_objects(dom1, ("block", "key", "door", "zombie"))
        return object_list

    @staticmethod
    def load_objects(dom1, obj_types):
        objects = []

        for obj_type in obj_types:

            xml_objects = dom1.getElementsByTagName(string.upper(obj_type))
            for obj in xml_objects:
                objects.append(LoadWorld.add_object(obj, obj_type))
        return objects

    @staticmethod
    def add_object(top_node, obj_type):
        '''Method called for each BLOCK, KEY, etc. tag in the xml document. Adds an object of that type to the list with the proper attributes.'''
        tags = {}
        for i in top_node.childNodes:
            if i.hasChildNodes():
                tags[i.nodeName] = i.firstChild.nodeValue

        if obj_type == "block":
            return Block((tags['X'], tags['Y'], tags['Z']),
                         (tags['RED'], tags['GREEN'], tags['BLUE']))
        elif obj_type == "key":
            return Key((tags['X'], tags['Y'], tags['Z']),
                       (tags['RED'], tags['GREEN'], tags['BLUE']), tags['ID'])
        elif obj_type == "door":
            return Door((tags['X'], tags['Y'], tags['Z']),
                       (tags['RED'], tags['GREEN'], tags['BLUE']), tags['ID'])
        elif obj_type == "zombie":
            return Zombie(tags['X'], tags['Y'], tags['Z'])
        else:
            return None

