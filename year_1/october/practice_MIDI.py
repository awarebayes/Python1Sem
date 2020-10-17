# Write a MIDI fixer which turns
# 0  ON  60   | 0  ON  60
# 10 ON  60   | 10 OFF 60
# 10 OFF 60   | 10 ON  60
# 20 OFF 60   | 20 OFF 60

from collections import defaultdict, namedtuple
from copy import copy

Note = namedtuple("Note", ["time", "state", "chord"])

programs = [
    ["0 ON 60", "10 ON 60", "12 OFF 60", "20 OFF 60"],
    [
        "0 ON 60",
        "5 ON 70",
        "10 ON 60",
        "10 OFF 60",
        "15 OFF 70",
        "15 ON 70",
        "20 OFF 60",
        "20 OFF 70",
    ],
    ["0 ON 60", "1 OFF 60", "1 ON 60", "10 OFF 60"],
]

for program in programs:
    notes = defaultdict(list)
    fixed = []
    for line in program:
        should_ignore = False
        time, state, chord = line.split()
        note = Note(int(time), True if state == "ON" else False, chord)
        print("Current", note)
        if notes[chord]:
            print("Last", notes[chord][-1])
            last_note = notes[chord][-1]
            # 10 ON -> 10 ON
            if last_note.state == note.state == True:
                note_off = Note(note.time-1, False, note.chord)
                print("Double on, adding correcting node", note_off)
                notes[chord].append(note_off)
            # 10 OFF -> 10 OFF
            elif last_note.state == note.state == False:
                print("Double off, popping the last one")
                notes[chord].pop()
            # 10 ON -> 10 OFF
            elif last_note.time == note.time and not last_note.state and note.state:
                if notes[chord][-2].time == last_note.time-1:
                    notes[chord].pop(-1)
                    should_ignore = True
                else:
                    notes[chord][-1] = Note(last_note.time-1, False, chord)
        if not should_ignore:
            notes[chord].append(note)
        

    #print("Notes:")
    #print(notes)
    #print('____')
    for line in program:
        time, state, chord = line.split()
        last_time = notes[chord][0].time
        #print("time, last time", time, last_time)
        #print("current times in stack", list(map(lambda x: x.time, notes[chord])))
        while notes[chord][0].time < int(time)-1:
            notes[chord].pop(0)
        #print("current times in stack, after clearning", list(map(lambda x: x.time, notes[chord])))
        if int(time)-1 == last_time:
            note_fixed1, note_fixed2 = notes[chord].pop(0), notes[chord].pop(0)
            fixed.append(' '.join([str(note_fixed1.time), "ON" if note_fixed1.state else "OFF", chord]))
            fixed.append(' '.join([str(note_fixed2.time), "ON" if note_fixed2.state else "OFF", chord]))


        if int(time) == last_time:
            note_fixed = notes[chord].pop(0)
            fixed.append(' '.join([str(note_fixed.time), "ON" if note_fixed.state else "OFF", chord]))
            

    print("\n".join(fixed))
    print("-1")

print("-2")