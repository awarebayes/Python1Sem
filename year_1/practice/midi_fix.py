from typing import Dict, List, Optional, OrderedDict, Tuple
from lambdamatch import read_rules
from collections import namedtuple, defaultdict
from sortedcontainers import SortedDict, SortedList

# structs
UnnamedNote = namedtuple("UnnamedNote", ["time", "state"])

# types
note_str = str
note_time = int
note_state = bool
note_id = int

# set [match_f, results_f] for each rule in rules_str
rules, max_arg_len = read_rules("/home/mike/Documents/uni/year_1/practice/rules.txt")

# do guard pattern matching, like in haskell
# | matched = evaluate and return
# | otherwise = False
# complexity: O(n * max_arg_len)
def match_evaluate(args: List[UnnamedNote]) -> Tuple[Optional[List[UnnamedNote]], int]:
    for match_f, results_f, args_len in rules:
        matched, n_args = match_f(args[:args_len])
        if matched:
            return results_f(args), n_args
    return None, 0


# parse program strings line by line, O(N)
def parse_by_line(program):
    notes_unfixed: Dict[note_id, List[UnnamedNote]] = defaultdict(list)
    for line in program:
        time, state, note = line.split()
        time, state, note = int(time), True if state == "ON" else False, int(note)
        notes_unfixed[note].append(UnnamedNote(time, state))
    return notes_unfixed


# apply fix ONCE, O(N*log N)
def fix_note(note_unfixed):
    i = 0
    while i < len(note_unfixed):
        notes_slice = note_unfixed[i : i + max_arg_len]
        notes_evaluated, n_args = match_evaluate(notes_slice)
        if notes_evaluated:  # pattern was matched, multiple notes were returned
            note_unfixed = (
                note_unfixed[:i] + notes_evaluated + note_unfixed[i + n_args :]
            )

        i += 1
    return note_unfixed


# rewrite perpetually, until not fixed
def rewrite_note(note_unfixed):
    last_rewrite = fix_note(note_unfixed)
    while note_unfixed != last_rewrite:
        note_unfixed = last_rewrite
        last_rewrite = fix_note(last_rewrite)
    return last_rewrite


# rewrite all notes then order them by time, O(N*log N)
def rewrite(notes_unfixed):
    notes_fixed: Dict[note_str, Dict[note_time, note_state]] = {}
    for note in notes_unfixed.keys():
        notes_unfixed[note] = rewrite_note(notes_unfixed[note])

    for note in notes_unfixed.keys():
        if note not in notes_fixed:
            notes_fixed[note] = SortedDict()
        for n in notes_unfixed[note]:
            notes_fixed[note][n.time] = n.state

    return notes_fixed


def order_by_time(notes_fixed):
    # now order by time, O(N * log N)
    fixed_by_time: Dict[
        note_time, List[Tuple[note_str, note_state]]
    ] = SortedDict()  # dict: { time: (note, state) }

    for note in notes_fixed.keys():
        for time, state in notes_fixed[note].items():
            if time not in fixed_by_time:
                fixed_by_time[time] = []
            fixed_by_time[time].append((note, state))
    return fixed_by_time


def rewrite_program(program):
    notes_unfixed = parse_by_line(program)
    notes_fixed = rewrite(notes_unfixed)
    fixed_by_time = order_by_time(notes_fixed)
    del notes_fixed, notes_unfixed

    fixed = []  # out program
    # assemble back again, O(N)
    for time, notes in fixed_by_time.items():
        for note in notes:
            # make serialized copy
            serialized_note = str(time), "ON" if note[1] else "OFF", str(note[0])
            fixed.append(" ".join(serialized_note))
    return fixed


def main():
    programs = [
        [],
    ]
    for line in open("/home/mike/Documents/uni/year_1/practice/programs.txt", "r"):
        line = line.strip()
        if line == "-1":
            programs.append([])
        elif line == "-2":
            break
        else:
            programs[-1].append(line)

    for program in programs:
        fixed = rewrite_program(program)
        for line in fixed:
            print(line)
        print("-1")
    print("-2")


if __name__ == "__main__":
    main()
