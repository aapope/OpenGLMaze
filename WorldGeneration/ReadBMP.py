import ImageTk, Image, random

WHITE = (255,255,255)
BLACK = (0,0,0)
GREEN = (0,255,0)
ZOMBIE_GRAY = (100,100,100)
YELLOW = (255,255,0)
BLUE = (0,0,255)
BLOCK_SIZE = 2
BLOCK_Y = .5
KEY_Y = .5
DOOR_Y = .5

class ReadBMP():
    
    def __init__(self, filename, f_out_name):
        '''Open the given file (should be a .bmp), create xml, and write the xml to the other filename
        @type  filename:   String
        @param filename:   The .bmp file -- the map
        @type  f_out_name: String
        @param f_out_name: The name of the .xml file to be written
        '''
        print "Reading %s and writing to %s" % (filename, f_out_name)

        f = Image.open(filename)
        xml = self.make_xml(f)
        f = open(f_out_name, "wb")
        f.write(xml)
        f.close()

    def make_xml(self, f):
        '''Given an Image object, creates xml
        @type  f: Image        
        @param f: The map of the world to be created
        '''
        self.id_colors = {}
        xml = "<WORLD>\n"
        for x in range(f.size[0]):
            for y in range(f.size[1]):
               color = f.getpixel((x, y))                   #3-tuple of range 0-255
               xml += self.handle_pixel(x, y, color)

        xml += "</WORLD>"
        return xml
            
    def handle_pixel(self, x, y, color):
        ''' Given x, y, and color, create an object based on which colors mean what.
        @type  x:     int
        @param x:     The x-coordinate of the current pixel
        @type  y:     int
        @param y:     The y-coordinate of the current pixel, corresponding to the
                      z-coordinate of the object to be created
        @type  color: 3-tuple
        @param color: The red, green, blue values of the pixel-- determines the
                      object type and some aspects of keys, doors
        '''
        if color == BLACK:
            return self.make_block_xml(x*BLOCK_SIZE, BLOCK_Y, 
                                  y*BLOCK_SIZE, color[0], color[1], color[2])

        #if red value is 255 and green is 0, object is a key and the id is blue value
        elif color[0] == 255 and color[1] == 0 : 
            obj_id = color[2]
            if obj_id in self.id_colors:
                color = self.id_colors[obj_id]
            else:
                color = (random.randrange(1,255),random.randrange(1,255),random.randrange(1,255))
                self.id_colors[obj_id] = color
            #print "Made a key of id " + str(obj_id) + " and color " + str(color)
            return self.make_key_or_door_xml("KEY", x*BLOCK_SIZE, KEY_Y, 
                                     y*BLOCK_SIZE, color[0], 
                                     color[1], color[2], obj_id)

        elif color[0] == 0 and color[1] == 255: #if red value is 0 and green is 255, object is a door and the id is blue value
            obj_id = color[2]
            if obj_id in self.id_colors:                      #TODO: make this code less redundant
                color = self.id_colors[obj_id]
            else:
                color = (random.randrange(1,255),random.randrange(1,255),random.randrange(1,255))
                self.id_colors[obj_id] = color
            #print "Made a door of id " + str(obj_id) + " and color " + str(color)
            return self.make_key_or_door_xml("DOOR", x*BLOCK_SIZE, DOOR_Y, 
                                     y*BLOCK_SIZE, color[0], 
                                     color[1], color[2], obj_id)
        elif color == ZOMBIE_GRAY:
            return self.make_zombie_xml(x*BLOCK_SIZE, 0, y*BLOCK_SIZE)
        elif color == BLUE:
            return self.make_player_location_xml(x*BLOCK_SIZE, y*BLOCK_SIZE)
        elif color == YELLOW:
            return self.make_chest_xml(x*BLOCK_SIZE, y*BLOCK_SIZE)
        else:
            return ""


    def make_block_xml(self, x, y, z, r, g, b):
        ''' Make the xml for a block, given the parameters
        @type  x: int
        @param x: The x-coordinate
        @type  y: int
        @param y: The y-coordinate
        @type  z: int
        @param z: The z-coordinate
        @type  r: int
        @param r: The red value (0-255)
        @type  g: int
        @param g: The green value (0-255)
        @type  b: int
        @param b: The blue value (0-255)
        '''
        string = "\t<BLOCK>\n"
        string += "\t\t<X>%s</X>\n" % str(x)
        string += "\t\t<Y>%s</Y>\n" % str(y)
        string += "\t\t<Z>%s</Z>\n" % str(z)
        string += "\t\t<RED>%s</RED>\n" % str(r)
        string += "\t\t<GREEN>%s</GREEN>\n" % str(g)
        string += "\t\t<BLUE>%s</BLUE>\n" % str(b)
        string += "\t</BLOCK>\n"
        return string

    def make_key_or_door_xml(self, obj_type, x, y, z, r, g, b, obj_id):
        '''
        @type  x: int
        @param x: The key/door's x-coordinate
        @type  y: int
        @param y: The key/door's y-coordinate
        @type  z: int
        @param z: The key/door's z-coordinate
        @type  r: int
        @param r: The red value (0-255)
        @type  g: int
        @param g: The green value (0-255)
        @type  b: int
        @param b: The blue value (0-255)
        @type  obj_id int
        @param obj_id The key/door's id
        '''
        string = "\t<%s>\n" % obj_type
        string += "\t\t<X>%s</X>\n" % str(x)
        string += "\t\t<Y>%s</Y>\n" % str(y)
        string += "\t\t<Z>%s</Z>\n" % str(z)
        string += "\t\t<RED>%s</RED>\n" % str(r)
        string += "\t\t<GREEN>%s</GREEN>\n" % str(g)
        string += "\t\t<BLUE>%s</BLUE>\n" % str(b)
        string += "\t\t<ID>%s</ID>\n" % str(obj_id)
        string += "\t</%s>\n" % obj_type
        return string

    def make_zombie_xml(self, x, y, z):
        '''
        @type  x: int
        @param x: The x-coordinate
        @type  y: int
        @param y: The y-coordinate
        @type  z: int
        @param z: The z-coordinate
        '''
        string = "\t<ZOMBIE>\n"
        string += "\t\t<X>%s</X>\n" % str(x)
        string += "\t\t<Y>%s</Y>\n" % str(y)
        string += "\t\t<Z>%s</Z>\n" % str(z)
        string += "\t</ZOMBIE>\n"
        return string

    def make_player_location_xml(self, x, z):
        '''
        @type  x: int
        @param x: The player's starting x-coordinate
        @type  z: int
        @param z: The player's starting z-coordinate
        '''
        string = "\t<PLAYERLOCATION>\n"
        string += "\t\t<X>%s</X>\n" % str(x)
        string += "\t\t<Z>%s</Z>\n" % str(z)
        string += "\t</PLAYERLOCATION>\n"
        return string

    def make_chest_xml(self, x, z):
        '''
        @type  x: int
        @param x: The x-coordinate
        @type  y: int
        @param y: The y-coordinate
        @type  z: int
        @param z: The z-coordinate
        '''
        string = "\t<CHEST>\n"
        string += "\t\t<X>%s</X>\n" % str(x)
        string += "\t\t<Y>%s</Y>\n" % str(0)   #y is baked in as 0
        string += "\t\t<Z>%s</Z>\n" % str(z)
        string += "\t</CHEST>\n"
        return string


if __name__ ==  "__main__":
    rb = ReadBMP("realMaze1.bmp", "realMaze1.xml")
