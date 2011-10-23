'''A class for randomly generating a blockworld xml file'''
__author__ = "Emily and Andrew"
__date__ = "21 October 2011"
import random, sys

class GenerateField:
    '''A class for randomly generating a blockworld xml file'''

    def __init__(self, num, filename):
        '''Takes a number of blocks to make and a filename to save them in. Always puts the blocks in the range -50,50 for x and z and .5 for y'''
        x_range = 50
        z_range = 50
        y = .5

        blocks = []
        for i in range(num):
            blocks.append((x_range-random.random()*x_range*2, y, 
            z_range - random.random()*z_range*2, random.random(), random.random(), random.random()))

        self.save(blocks, filename)
        

    def save(self, blocks, filename):
        '''Saves the list of blocks (x, y, z, r, g, b)'''
        string = "<BLOCKWORLD>\n"
        for b in blocks:
            string += "\t<BLOCK>\n"
            string += "\t\t<X>" + str(b[0]) + "</X>\n"
            string += "\t\t<Y>" + str(b[1]) + "</Y>\n"
            string += "\t\t<Z>" + str(b[2]) + "</Z>\n"
            string += "\t\t<RED>" + str(b[3]) + "</RED>\n"
            string += "\t\t<GREEN>" + str(b[4]) + "</GREEN>\n"
            string += "\t\t<BLUE>" + str(b[5]) + "</BLUE>\n"
            string += "\t</BLOCK>\n"
        string += "</BLOCKWORLD>"

        f = open(filename, "w")
        f.write(string)
        f.close()

if __name__ == '__main__':    
    '''Takes command arguments number of blocks and filename'''
    try:
        g = GenerateField(int(sys.argv[1]), sys.argv[2])
    except:
        print 'Usage: GenerateField.py: python GenerateField.py num_blocks filename'
        exit(0)
