'''
5.3.2
Define class MusicNotes
La	    55	    110 	220	    440 	880
Si	    61.74	123.48	246.96	493.92	987.84
Do	    65.41	130.82	261.64	523.28	1046.56
Re	    73.42	146.84	293.68	587.36	1174.72
Mi	    82.41	164.82	329.64	659.28	1318.56
Fa	    87.31	174.62	349.24	698.48	1396.96
Sol	    98	    196	    392	    784	    1568

each iteration on a MusicNotes object will return the frequency of the next note
'''


class MusicNotes:

    def __init__(self, max=5):
        self._max_octaves = max
        self.octave_idx = 0
        self.note_idx = -1
        self._notes_base = [55, 61.74, 65.41, 73.42, 82.41, 87.31, 98]

    def __iter__(self):
        return self

    def __next__(self):
        if self.note_idx >= len(self._notes_base) - 1:
            self.note_idx = -1
            self.octave_idx += 1
        if self.octave_idx >= self._max_octaves:
            raise StopIteration
        self.note_idx += 1
        return self._notes_base[self.note_idx] * (2**self.octave_idx)


music_iter = MusicNotes()
for freq in music_iter:
    print(freq)