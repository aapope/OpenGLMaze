import ImageTk, Image

class ReadBMP():
    
    self.WHITE = (255,255,255)
    self.BLACK = (0,0,0)
    self.GREEN = (255,0,0)
    self.BLOCK_SIZE = 50
    self.BLOCK_Z = 0
    self.KEY_Z = 0

    def __init__(self):      
        f = Image.open("testWorld.bmp")
        xml = self.make_xml(f)

    def make_xml(self, f):
        xml = ""
        for x in range(f.size[0]):
            for y in range(f.size[1]):
               color = f.getpixel((i, j))                   #3-tuple of range 0-255
               xml += handle_pixel(i, j, color)
            
    def handle_pixel(self, x, y, color):
        ''' Given x, y, and color, 
        '''

        if color == self.WHITE:
            return ""
        elif color == self.BLACK:
            return make_block_xml(x*self.BLOCK_SIZE, y*self.BLOCK_SIZE, 
                                  self.BLOCK_Z, color[0], color[1], color[2])
        elif color == self.GREEN:
            return make_key_xml(x*self.BLOCK_SIZE, y*self.BLOCK_SIZE, 
                                  self.KEY_Z, color[0], color[1], color[2])

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
    rb = ReadBMP()
