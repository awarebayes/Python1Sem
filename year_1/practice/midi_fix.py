from typing import Dict, List, Tuple
from lambdamatch import read_rules
from collections import namedtuple, defaultdict
from sortedcontainers import SortedDict, SortedList

# structs
UnnamedNote = namedtuple("UnnamedNote", ["time", "state"])

# types
note_str = str
note_time = int
note_state = bool

# time function is a lambda which maps time relatively to coeficient
programs = [
    ["0 ON 60", "10 ON 60", "12 OFF 60", "20 OFF 60"],
    [
        "0 ON 60",
        "5 ON 70",
        "10 ON 60",
        "10 OFF 60",
        "14 OFF 80",
        "14 ON 80",
        "15 OFF 70",
        "15 ON 70",
        "20 OFF 60",
        "20 OFF 70",
    ],
    ["0 ON 60", "1 OFF 60", "1 ON 60", "10 OFF 60"],
]

# set [match_f, results_f] for each rule in rules_str
rules, max_arg_len = read_rules("/home/mike/Documents/uni/year_1/practice/rules")

# do guard pattern matching, like in haskell
# | matched = evaluate and return
# | otherwise = False
# complexity: O(n * max_arg_len)
def match_evaluate(args: List[UnnamedNote]):
    for match_f, results_f, args_len in rules:
        if match_f(args[:args_len]):
            return results_f(args)
    return False


# parse by line, O(N)
def parse_by_line(program):
    notes_unfixed: Dict[note_str, List[UnnamedNote]] = defaultdict(list)
    for line in program:
        time, state, note = line.split()
        time, state, note = int(time), True if state == "ON" else False, int(note)
        notes_unfixed[note].append(UnnamedNote(time, state))
    return notes_unfixed

# apply fix, O(N*log N)
def apply_fix(notes_unfixed):
    notes_fixed: Dict[note_str, SortedDict[note_time, note_state]] = defaultdict(
        SortedDict
    )
    for note in notes_unfixed.keys():
        i = 0
        while i < len(notes_unfixed[note]):
            notes_slice = notes_unfixed[note][i : i + max_arg_len]
            notes_evaluated = match_evaluate(notes_slice)
            if not notes_evaluated:  # everything is ok for this note
                current_note = notes_unfixed[note][i]
                notes_fixed[note][current_note.time] = current_note.state
            else:  # pattern was matched, multiple notes were returned
                notes_unfixed[note] = (
                    notes_unfixed[note][:i]
                    + notes_evaluated
                    + notes_unfixed[note][i + 2 :]
                )
                for n in notes_evaluated:
                    notes_fixed[note][n.time] = n.state
            i += 1
    return notes_fixed

def rewrite_note(note_dict):
    pass

def fix_program(program):
    notes_unfixed = parse_by_line(program)
    notes_fixed = apply_fix(notes_unfixed)

    # now order by time, O(N * log N)
    fixed_by_time: SortedDict[
        note_time, List[Tuple[note_str, note_state]]
    ] = SortedDict()  # dict: { time: (note, state) }

    for note in notes_fixed.keys():
        for time, state in notes_fixed[note].items():
            if time not in fixed_by_time:
                fixed_by_time[time] = []
            fixed_by_time[time].append((note, state))

    fixed = []  # out program
    # assemble back again, O(N)
    for time, notes in fixed_by_time.items():
        for note in notes:
            # make serialized copy
            serialized_note = str(time), "ON" if note[1] else "OFF", str(note[0])
            fixed.append(" ".join(serialized_note))
    return fixed


def main():
    for program in programs:
        fixed = fix_program(program)
        for line in fixed:
            print(line)
        print("-1")
    print("-2")


if __name__ == "__main__":
    main()
