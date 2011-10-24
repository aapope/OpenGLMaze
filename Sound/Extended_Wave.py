'''This program contains the Wave class, which has methods to read in a .wav file, modify it, and then save it to another file'''
__author__ = "Andrew Pope"
__date__ = "11 October 2011"
__version__ = "1.0.0"
__credits__ = "This program was written for CP215 Application Design at Colorado College"

import struct, math


class Wave:
    '''This class has a method to read in a .wav file and its attributes, read the data from the file, change the scaling of the volume, normalize the volume, and save the file out to the disk'''
    notes = {'A0': 27.5000 , 'C4': 261.626 , 'G#3': 207.652 , 'G#2': 103.826 , 'G#5': 830.609 , 'G#4': 415.305 , 'G#7': 3322.44 , 'G#6': 1661.22 , 'G7': 3135.96 , 'G6': 1567.98 , 'G5': 783.991 , 'G4': 391.995 , 'G3': 195.998 , 'G2': 97.9989  , 'Eb4': 311.127 , 'Eb5': 622.254 , 'Eb6': 1244.51 , 'Eb7': 2489.02 , 'Eb1': 38.8909 , 'Eb2': 77.7817 , 'Eb3': 155.563 , 'C5': 523.251 , 'Db1': 34.6478 , 'E7': 2637.02 , 'E1': 41.2034 , 'B4': 493.883 , 'B5': 987.767 , 'B6': 1975.53 , 'B7': 3951.07 , 'B0': 30.8677 , 'E3': 164.814 , 'B2': 123.471 , 'B3': 246.942 , 'E2': 82.4069 , 'A4': 440 , 'C6': 1046.50 , 'F#2': 92.4986 , 'F#3': 184.997 , 'F#4': 369.994 , 'F#5': 739.989 , 'F#6': 1479.98 , 'F#7': 2959.96 , 'E5': 659.255 , 'E4': 329.628 , 'Db3': 138.591 , 'E6': 1318.51 , 'Db5': 554.365 , 'Db4': 277.183 , 'Db7': 2217.46 , 'Db6': 1108.73 , 'A#3': 233.082 , 'A#2': 116.541 , 'A#0': 29.1352 , 'A#7': 3729.31 , 'A#6': 1864.66 , 'A#5': 932.328 , 'A#4': 466.164 , 'C7': 2093.00  , 'Gb6': 1479.98 , 'Gb7': 2959.96 , 'Gb4': 369.994 , 'Gb5': 739.989 , 'Gb2': 92.4986 , 'Gb3': 184.997 , 'Bb7': 3729.31 , 'Bb6': 1864.66 , 'Bb5': 932.328 , 'Bb4': 466.164 , 'Bb3': 233.082 , 'Bb2': 116.541 , 'Bb0': 29.1352 , 'F2': 87.3071 , 'F3': 174.614 , 'F4': 349.228 , 'F5': 698.456 , 'F6': 1396.91 , 'F7': 2793.83 , 'C3': 130.813 , 'C2': 65.4064 , 'A3': 220.000 , 'A2': 110.000 , 'A5': 880.000 , 'A7': 3520.00  , 'A6': 1760.00  , 'D#6': 1244.51 , 'D#7': 2489.02 , 'D#4': 311.127 , 'D#5': 622.254 , 'D#2': 77.7817 , 'D#3': 155.563 , 'D#1': 38.8909 , 'C#5': 554.365 , 'C#4': 277.183 , 'C#7': 2217.46 , 'C#6': 1108.73 , 'C#1': 34.6478 , 'C#3': 138.591 , 'Ab2': 103.826 , 'Ab3': 207.652 , 'Ab4': 415.305 , 'Ab5': 830.609 , 'Ab6': 1661.22 , 'Ab7': 3322.44 , 'C8':4186.01, 'D6': 1174.66 , 'D7': 2349.32 , 'D4': 293.665 , 'D5': 587.330 , 'D2': 73.4162 , 'D3': 146.832 , 'D1': 36.7081, 'Db2': 69.30}
    just_notes = {'G#3':206.25, 'G#2':103.125, 'G#5':825.0, 'G#4':412.5, 'G#7':3300.0, 'G#6':1650.0, 'G7':3168.0, 'G6':1584.0, 'G5':792.0, 'G4':396.0, 'G3':198.0, 'G2':99.0, 'Eb4':309.375, 'Eb5':618.75, 'Eb6':1237.5, 'Eb7':2475.0, 'Eb2':77.34375, 'Eb3':154.6875, 'E7':2640.0, 'Db2':68.75, 'B4':495.0, 'B5':990.0, 'B6':1980.0, 'B1':61.875, 'B2':123.75, 'B3':247.5, 'E2':82.5, 'F#2':91.6666666667, 'F#3':183.333333333, 'F#4':366.666666667, 'F#5':733.333333333, 'F#6':1466.66666667, 'F#7':2933.33333333, 'E5':660.0, 'E4':330.0, 'Db3':137.5, 'E6':1320.0, 'Db5':550.0, 'Db4':275.0, 'E3':165.0, 'Db6':1100.0, 'A#3':234.666666667, 'A#2':117.333333333, 'A#1':58.6666666667, 'A#6':1877.33333333, 'A#5':938.666666667, 'A#4':469.333333333, 'Gb6':1466.66666667, 'Gb7':2933.33333333, 'Gb4':366.666666667, 'Gb5':733.333333333, 'Gb2':91.6666666667, 'Gb3':183.333333333, 'C3':132.0, 'C2':66.0, 'C7':2112.0, 'C6':1056.0, 'C5':528.0, 'C4':264.0, 'Bb6':1877.33333333, 'Bb5':938.666666667, 'Bb4':469.333333333, 'Bb3':234.666666667, 'Bb2':117.333333333, 'Bb1':58.6666666667, 'F2':88.0, 'F3':176.0, 'F4':352.0, 'F5':704.0, 'F6':1408.0, 'F7':2816.0, 'Db7':2200.0, 'A1':55.0, 'A3':220.0, 'A2':110.0, 'A5':880.0, 'A4':440.0, 'A6':1760.0, 'D#6':1237.5, 'D#7':2475.0, 'D#4':309.375, 'D#5':618.75, 'D#2':77.34375, 'D#3':154.6875, 'C#5':550.0, 'C#4':275.0, 'C#7':2200.0, 'C#6':1100.0, 'C#3':137.5, 'C#2':68.75, 'Ab1':103.125, 'Ab2':206.25, 'Ab3':412.5, 'Ab4':825.0, 'Ab5':1650.0, 'Ab6':3300.0, 'D6':1173.33333333, 'D7':2346.66666667, 'D4':293.333333333, 'D5':586.666666667, 'D2':73.3333333333, 'D3':146.666666667}

    def __init__(self):
        '''Sets up the default values for the class'''
        self.num_channels = 1
        self.sample_width = 2
        self.sampling_rate = 44101
        self.number_frames = 0
        self.frames = []
        self.bits_per_sample = 16
        self.format = '<h'
        self.long_frames = []
        self.junk = []
        self.data_length = 1

    def load(self, filename):
        '''Reads in the file, only parsing the necessary information. Calls readFrames() to read the actual file data'''
        #22
        f = open(filename, 'r')
        self.junk.append(f.read(22))
        self.num_channels, = struct.unpack('<h', f.read(2))
        self.sampling_rate, = struct.unpack('<i', f.read(4))
        self.junk.append(f.read(6))
        self.bits_per_sample, = struct.unpack('<h', f.read(2))
        self.sample_width = (self.bits_per_sample / 8) * self.num_channels
        self.junk.append(f.read(4))
        self.data_length, = struct.unpack('<i', f.read(4))
        self.number_frames = self.data_length / self.sample_width
        if self.bits_per_sample / 8 == 2:
            self.format = '<h'
        elif self.bits_per_sample / 8 == 4:
            self.format = '<i'
        self.readFrames(f)

    def readFrames(self, in_file):
        '''Reads samples based on the sample width and the number of channels. Only one channel is read for use at this point. The other(s) (along with the first channel) are placed in a list of tuples for use when writing the file.'''
        #TODO: Read more efficiently
        data = []
        numbers = []
        data.append(in_file.read(self.sample_width/self.num_channels))
        while data[0]:
            numbers.append(struct.unpack(self.format, data[0])[0])
            for i in range(1,self.num_channels):
                data.append(in_file.read(self.sample_width/self.num_channels))
                if data[i]:
                    numbers.append((struct.unpack(self.format, data[i])[0]))
            #Just use the first channel!
            self.frames.append(numbers[0])
            self.long_frames.append(tuple(numbers))
            data = []
            numbers = []
            data.append(in_file.read(self.sample_width/self.num_channels))


    def get_max_frame(self):
        '''Gets the largest frame!'''
        biggest_index = 0
        for i in range(0, self.number_frames):
            if abs(self.frames[i]) > abs(self.frames[biggest_index]):
                biggest_index = i
        return self.frames[biggest_index] 

    def adjustVolume(self, amt):
        '''Adjusts the volume by multiplying by a parameter'''
        for i in range(len(self.frames)):
            self.frames[i] = int(round(amt * self.frames[i]))

    def normalizeVolume(self):
        '''Normalizes the volume, making the largest frame the largest possible'''
        largest = self.get_max_frame()
        scale = abs(float(2**(self.bits_per_sample) - 1) / largest)
        for i in range(len(self.frames)):
            self.frames[i] = int(round(scale * self.frames[i]))

    def save(self):
        '''Saves to a file. First writes out the saved header information, then puts the modified frames back into the tuples (containing the other channels), then writes them back out to a file'''
        # TODO: Write more robustly
        # junk numchannels samplerate junk bitspersample junk data
        f = open('outfile.wav', 'w')
        #Static .wav header information
        static_header_1 = '\x52\x49\x46\x46\xf0\x45\x9e\x01\x57\x41\x56\x45\x66\x6d\x74\x20\x10\x00\x00\x00\x01\x00'
        static_header_2 = '\x64\x61\x74\x61'
        self.data_length = len(self.frames) * self.num_channels * self.bits_per_sample / 8
        to_write = static_header_1+struct.pack('<h', self.num_channels)+struct.pack('<i', self.sampling_rate)+struct.pack('<i', (self.sampling_rate * self.num_channels * self.bits_per_sample/8))+struct.pack('<h', (self.num_channels*self.bits_per_sample/8))+struct.pack('<h', self.bits_per_sample)+static_header_2+struct.pack('<i', self.data_length)
        f.write(to_write)
        #put the new data into the rest of the channels
        to_write = ''
        for i in range(len(self.frames)):
            lst = list(self.long_frames[i])
            lst[0] = self.frames[i]
            self.long_frames[i] = tuple(lst)
        for i in self.long_frames:
            for j in i:
                to_write += struct.pack(self.format, j)
        f.write(to_write)
        f.close()
            
    def echo(self, delay, decay):
        '''Puts an echo in the recording by saving the previous sample, multiplying it by a decay factor, and adding it to the next delay samples'''
        echo_buffer = []
        for i in range(len(self.frames)):
            for j in range(len(echo_buffer)):
                echo_buffer[j] *= decay
                self.frames[i] += echo_buffer[j]
            if len(echo_buffer) == delay:
                echo_buffer.pop(0)
            echo_buffer.append(self.frames[i])

        for i in range(len(self.frames)):
            self.frames[i] = int(round(self.frames[i]))

    def chipmunkify(self, num):
        '''Speeds up the recording by removing every n samples'''
        new_frames = []
        for i in range(0, len(self.frames), num):
            new_frames.append(self.frames[i])
        self.frames = new_frames

        new_frames = []
        for i in range(0, len(self.long_frames), num):
            new_frames.append(self.long_frames[i])
        self.long_frames = new_frames
        
        self.number_frames = len(new_frames) / self.sample_width

    def make_sine(self, start, duration, note, amplitude):
        '''Constructs a sine wave of duration seconds, note (in the form C1 or D#4, etc.), and amplitude... amplitude'''
        start_length = int(start * self.sampling_rate)
        length = int(duration * self.sampling_rate)
        if length+start_length > len(self.frames):
            for i in range(len(self.frames), length+start_length):
                self.frames.append(0)
                self.long_frames.append((0,))

        for i in range(start_length, length + start_length):
            self.frames[i] += int(round(math.sin(i*2*math.pi*float(self.notes[note])/self.sampling_rate)*amplitude))


    def make_sawtooth(self, start, duration, note, amplitude):
        '''Constructs a sawtooth wave of duration seconds, note (in the form C1 or D#4, etc.), and amplitude... amplitude'''
        frequency = self.just_notes[note]
        start_length = int(start * self.sampling_rate)
        length = int(duration * self.sampling_rate)
        if length+start_length > len(self.frames):
            for i in range(len(self.frames), length+start_length):
                self.frames.append(0)
                self.long_frames.append((0,))
        wavelength = int(self.sampling_rate / frequency)
        for i in range(start_length, start_length+length, wavelength):
            for j in range(0, wavelength):
                if len(self.frames) > (i+j):
                    self.frames[i+j] += (-amplitude + (2*amplitude/float(self.sampling_rate/frequency))*j)

        for i in range(start_length, length+start_length):
            self.frames[i] = int(round(self.frames[i]))
                           
        

if __name__ == "__main__":
    '''Runner class. Current form makes a sine wave of pitch A3 (220Hz)'''
    WAVE_CLASS = Wave()
    WAVE_CLASS.make_sine(0, 10, 'Eb4', 1000)
    WAVE_CLASS.make_sine(0, 10, 'G4', 1000)
    WAVE_CLASS.make_sine(0, 10, 'Bb4', 1000)
    WAVE_CLASS.make_sine(0, 10, 'Eb5', 1000)
    WAVE_CLASS.save()
