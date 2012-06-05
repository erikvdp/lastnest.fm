'''
Created on 20-mei-2012

@author: Erik
'''
from pyechonest import track
class notegrabber(object):
    '''
    classdocs
    '''

    def parse(self):
        t = track.track_from_filename(self.path);
        #select most relevant notes
        self.notes = []
        self.times = []
        for segments in getattr(t, 'segments'):
            keys = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B'];
            pitches = zip(keys,segments['pitches'])
            self.notes.append([p[0] for p in pitches if p[1]>0.8]) #only add notes with certain confidence lvl
            self.times.append(segments['start'])
        return zip(self.times, self.notes)   
    def __init__(self, path):
        '''
        Constructor
        '''
        self.path = path
        
if __name__ == '__main__':
    path = "define path"
    x = notegrabber(path)
    lijst = x.parse()
    for keys in lijst:
        print keys
    print len(x.notes)