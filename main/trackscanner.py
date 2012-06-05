'''
Created on 13-mei-2012

@author: Erik
'''
from pyechonest import track
class trackscanner(object):
    '''
    classdocs
    '''

    def parse(self):
        t = track.track_from_filename("test.mp3");
        for attr in ['analysis_channels', 'analysis_sample_rate', 'analysis_url', 'artist', 'audio_md5', 'danceability', 'duration', 'end_of_fade_in', 'energy', 'id', 'key', 'key_confidence', 'loudness', 'md5', 'meta', 'mode', 'mode_confidence', 'num_samples', 'sample_md5', 'start_of_fade_out', 'status', 'tempo', 'tempo_confidence', 'time_signature', 'time_signature_confidence', 'title']:
            print '%-30s %s' % (attr, getattr(t, attr))
        print ''

        for dicts_attr in ['bars', 'beats', 'sections', 'segments', 'tatums']:
            print '"%s" example dict:' % (dicts_attr)
            if getattr(t, dicts_attr):
                for key, val in getattr(t, dicts_attr)[0].iteritems():
                    print '    %-26s %s' % (key, val)
                print ''

        print 'segment pitches:'
        print ('%8s    ' + '%-4s ' * 12) % ('start', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B')
        for a_dict in t.segments:
            print ('%8.2f    ' + '%4.2f ' * 12) % ((a_dict['start'], ) + tuple(a_dict['pitches']))
    def __init__(self, input_filename):
        '''
        Constructor
        '''
        self.input_filename = input_filename
        
if __name__ == '__main__':
    x = trackscanner("test.mp3")
    x.parse()