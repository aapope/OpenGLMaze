import ImageTk, Image, os

WHITE = (255,255,255)
BLACK = (0,0,0)
GREEN = (0,255,0)
BLOCK_SIZE = 2
BLOCK_Y = .5
KEY_Y = 0


class ReadBMP():
    
    def __init__(self, filename, f_out_name):
        f = Image.open(filename)
        xml = self.make_xml(f)

        f = open(f_out_name, "wb")
        f.write(xml)
        print "writing " + f_out_name
        f.close()


    def make_xml(self, f):
        xml = "<WORLD>\n"
        for x in range(f.size[0]):
            for y in range(f.size[1]):
               color = f.getpixel((x, y))                   #3-tuple of range 0-255
               xml += self.handle_pixel(x, y, color)

        xml += "</WORLD>"
        return xml
            
    def handle_pixel(self, x, y, color):
        ''' Given x, y, and color, create an object based on which colors mean what.
        '''
        print color

        if color == WHITE:
            return ""
        elif color == BLACK:
            return self.make_block_xml(x*BLOCK_SIZE, BLOCK_Y, 
                                  y*BLOCK_SIZE, color[0], color[1], color[2])
        elif color == GREEN:
            return self.make_key_xml(x*BLOCK_SIZE, KEY_Y, 
                                  y*BLOCK_SIZE, color[0], color[1], color[2])

        else:
            return ""


    def make_block_xml(self, x, y, z, r, g, b):
        string = "\t<BLOCK>\n"
        string += "\t\t<X>%s</X>\n" % str(x)
        string += "\t\t<Y>%s</Y>\n" % str(y)
        string += "\t\t<Z>%s</Z>\n" % str(z)
        string += "\t\t<RED>%s</RED>\n" % str(r)
        string += "\t\t<GREEN>%s</GREEN>\n" % str(g)
        string += "\t\t<BLUE>%s</BLUE>\n" % str(b)
        string += "\t</BLOCK>\n"
        return string

    def make_key_xml(self, x, y, z, r, g, b):
        string = "\t<KEY>\n"
        string += "\t\t<X>%s</X>\n" % str(x)
        string += "\t\t<Y>%s</Y>\n" % str(y)
        string += "\t\t<Z>%s</Z>\n" % str(z)
        string += "\t\t<RED>%s</RED>\n" % str(r)
        string += "\t\t<GREEN>%s</GREEN>\n" % str(g)
        string += "\t\t<BLUE>%s</BLUE>\n" % str(b)
        string += "\t</KEY>\n"
        return string


if __name__ ==  "__main__":
    rb = ReadBMP("testWorld.bmp", "testWorld.xml")
