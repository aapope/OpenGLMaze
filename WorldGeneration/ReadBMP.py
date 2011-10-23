import ImageTk, Image, os

WHITE = (255,255,255)
BLACK = (0,0,0)
GREEN = (255,0,0)
BLOCK_SIZE = 50
BLOCK_Z = 0
KEY_Z = 0


class ReadBMP():
    
    def __init__(self, filename, f_out_name):
        f = Image.open(filename)
        xml = self.make_xml(f)

        f = open(f_out_name, "w")
        f.write(xml)
        print "writing " + f_out_name

        f.close()


    def make_xml(self, f):
        xml = ""
        for x in range(f.size[0]):
            for y in range(f.size[1]):
               color = f.getpixel((x, y))                   #3-tuple of range 0-255
               xml += self.handle_pixel(x, y, color)

        return xml
            
    def handle_pixel(self, x, y, color):
        ''' Given x, y, and color, create an object based on which colors mean what.
        '''

        if color == WHITE:
            return ""
        elif color == BLACK:
            return self.make_block_xml(x*BLOCK_SIZE, y*BLOCK_SIZE, 
                                  BLOCK_Z, color[0], color[1], color[2])
        elif color == GREEN:
            return self.make_key_xml(x*BLOCK_SIZE, y*BLOCK_SIZE, 
                                  KEY_Z, color[0], color[1], color[2])

    def make_block_xml(self, x, y, z, r, g, b):
        string = "\t<BLOCK>\n"
        string += "\t\t<X>%s</X>\n" % str(x)
        string += "\t\t<Y>%s</Y>\n" % str(y)
        string += "\t\t<Z>%s</Z>\n" % str(z)
        string += "\t\t<R>%s</R>\n" % str(r)
        string += "\t\t<G>%s</G>\n" % str(g)
        string += "\t\t<B>%s</B>\n" % str(b)
        string += "\t</BLOCK>\n"
        return string

    def make_key_xml(self, x, y, z, r, g, b):
        string = "\t<KEY>\n"
        string += "\t\t<X>%s</X>\n" % str(x)
        string += "\t\t<Y>%s</Y>\n" % str(y)
        string += "\t\t<Z>%s</Z>\n" % str(z)
        string += "\t\t<R>%s</R>\n" % str(r)
        string += "\t\t<G>%s</G>\n" % str(g)
        string += "\t\t<B>%s</B>\n" % str(b)
        string += "\t</KEY>\n"
        return string


if __name__ ==  "__main__":
    rb = ReadBMP("testWorld.bmp", "testWorld.xml")
