'''A class containing static methods for loading World xml files'''
__author__ = "the World Generator Team (Zach, Ethan, Emily), based on LoadBlocks.py by Andrew and Emily"
__date__ = "21 October 2011"

from Block import Block
from Key import Key
from xml.dom.minidom import parse

class LoadWorld:
    '''A class containing static methods for loading blockworld xml files'''

    @staticmethod
    def load(f_name):
        '''Call this static method to load a list of blocks, keys, etc from an xml file (f_name). Returns a list of Blocks.'''
        dom1 = parse(f_name)
        block_list = LoadWorld.load_blocks(dom1)
        key_list = LoadWorld.load_keys(dom1)
        object_list = block_list + key_list
        return object_list

    @staticmethod
    def load_blocks(dom1):
        block_list = []
        xml_blocks = dom1.getElementsByTagName('BLOCK')
        for block in xml_blocks:
            block_list.append(LoadWorld.add_object(block, "block"))
        return block_list
        
    @staticmethod
    def load_keys(dom1):
        key_list = []
        xml_keys = dom1.getElementsByTagName('KEY')
        for key in xml_keys:
            key_list.append(LoadWorld.add_object(key, "key"))
        return key_list
        
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
                       (tags['RED'], tags['GREEN'], tags['BLUE']),0)
        return block

