'''
5.1.2
receive input of notes to play in the form "note,playtime-note,playtime..."
split the string and iterate over the objects, playing each note with the winsound module
'''

from winsound import Beep

freqs = {"la": 220,
         "si": 247,
         "do": 261,
         "re": 293,
         "mi": 329,
         "fa": 349,
         "sol": 392,
         }


def main():
    notesstring = "sol,250-mi,250-mi,500-fa,250-re,250-re,500-do,250-re,250-mi,250-fa,250-sol,250-sol,250-sol,500"
    notes = notesstring.split('-')
    for note in notes:
        n, dur = note.split(',')
        Beep(freqs[n], int(dur))


if __name__ == "__main__":
    main()
