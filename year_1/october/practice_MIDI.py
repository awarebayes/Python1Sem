# Write a MIDI fixer which turns
# 0  ON  60   | 0  ON  60
# 10 ON  60   | 10 OFF 60
# 10 OFF 60   | 10 ON  60
# 20 OFF 60   | 20 OFF 60

from collections import defaultdict, namedtuple


def write_note(note):
    return " ".join([str(note.time), "ON" if note.state else "OFF", note.chord])


Note = namedtuple("Note", ["time", "state", "chord"])

programs = []

"""
while True:
    line = input()
    if line == '-1':
        programs.append([])
    elif line == '-2':
        break
    else:
        programs.append(line)
"""

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
        if notes[chord]: # whether there are notes in stack
            last_note = notes[chord][-1]
            # 10 ON -> 10 ON, add one trailing off
            if last_note.state == note.state == True:
                note_off = Note(note.time - 1, False, note.chord)
                notes[chord].append(note_off)
            # 10 OFF -> 10 OFF, ignore the last off
            elif last_note.state == note.state == False:
                notes[chord].pop()
            # 10 ON -> 10 OFF
            elif last_note.time == note.time and not last_note.state and note.state:
                if (
                    notes[chord][-2].time == last_note.time - 1
                ):  # cant fix,  ignore and pop trailing
                    notes[chord].pop(-1)
                    should_ignore = True
                else:  # shift previous one timestep and set OFF
                    notes[chord][-1] = Note(last_note.time - 1, False, chord)
        if not should_ignore:
            notes[chord].append(note)

    for line in program:
        time, state, chord = line.split()
        last_time = notes[chord][0].time

        # clear stack of notes with time less than ours
        while notes[chord][0].time < int(time) - 1:
            notes[chord].pop(0)

        if int(time) - 1 == last_time:
            note_fixed1, note_fixed2 = notes[chord].pop(0), notes[chord].pop(0)
            fixed.append(write_note(note_fixed1))
            fixed.append(write_note(note_fixed2))

        if int(time) == last_time:
            note_fixed = notes[chord].pop(0)
            fixed.append(write_note(note_fixed))

    print("\n".join(fixed))
    print("-1")

print("-2")
