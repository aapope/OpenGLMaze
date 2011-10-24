'''A class containing static methods for loading World xml files'''
__author__ = "the World Generator Team (Zach, Ethan, Emily), based on LoadBlocks.py by Andrew and Emily"
__date__ = "21 October 2011"

from Block import Block
from Key import Key
from Door import Door
from Zombie import Zombie
from Chest import Chest
from xml.dom.minidom import parse
import string

class LoadWorld:
    '''A class containing static methods for loading xml files'''

    @staticmethod
    def load(f_name):
        '''Call this static method to load a list of blocks, keys, etc from an xml file (f_name). Returns a list of Blocks.
        @type  f_name: String
        @param f_name: The name of the xml file to read
        @return:       A 2-tuple: the list of objects and the player location (itself a 2-tuple)
        '''
        dom1 = parse(f_name)
        player_location = LoadWorld.get_player_location(dom1)
        object_list = LoadWorld.load_objects(dom1, ("block", "key", "door", "zombie", "chest"))
        #return object_list
        return (object_list, player_location)

    @staticmethod
    def get_player_location(dom1):
        '''
        @type   dom1: Mini XML Document Object Model
        @param  dom1: The DOM we're reading from
        @return:      The player's location as a 2-tuple (x,z)
        '''
        player_location_nodes = dom1.getElementsByTagName("PLAYERLOCATION")
        if player_location_nodes:
            location = LoadWorld.add_object(player_location_nodes[0], "playerlocation")
            return location
        else:                               #default location is 0,0,0
            return (0,0,0)

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
                tags[i.nodeName] = float(i.firstChild.nodeValue)
                
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
            return Zombie((tags['X'], tags['Y'], tags['Z']))
        elif obj_type == "playerlocation":
            return (tags['X'], tags['Z'])
        elif obj_type == "chest":
            return Chest((tags['X'], tags['Y'], tags['Z']))
        else:
            return None

