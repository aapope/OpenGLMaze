#! /usr/bin/env python
'''Run the program from here! This will test whether everything is
working together and running correctly. You can specify whether you
want to run it with a separate xml file (loooking at you, world
generation people), but the default is the keys_and_blocks.xml
file.'''

from Player import Camera
from Graphics import RenderWorld
import sys

if __name__ == '__main__':
    try:
        RENDER = RenderWorld(sys.argv[1])
    except:
        RENDER = RenderWorld('WorldGeneration/testAll.xml')
