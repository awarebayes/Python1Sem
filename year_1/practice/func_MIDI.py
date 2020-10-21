from collections import namedtuple, defaultdict
import heapq

ExprArg = namedtuple("ExprArg", ["base_name", "state", "time_offset"])
UnnamedNote = namedtuple("UnnamedNote", ["time", "state"])

# time function is a lambda which maps time relatively to coeficient
programs = [
    ["0 ON 60", "10 ON 60", "12 OFF 60", "20 OFF 60"],
    [
        "0 ON 60",
        "5 ON 70",
        "10 ON 60",
        "10 OFF 60",
        "15 OFF 70",
        "15 ON 70",
        "15 OFF 70",
        "15 ON 70",
        "20 OFF 60",
        "20 OFF 70",
    ],
    ["0 ON 60", "1 OFF 60", "1 ON 60", "10 OFF 60"],
]

rules_str = [
    # 1 time, on
    "a ON, a ON -> a ON",
    "a-1 ON, a ON -> ? ?",  # i don't know what should happen there
    # 1 time, off
    "a OFF, a OFF -> a OFF",
    # 2 times, off (a-1 doesnt matter)
    "a OFF, b OFF -> b OFF",
    # 2 times, on
    "a ON, b ON -> a ON, b-1 ON, b ON",
    # 1 time, on off at the same time
    "a OFF, a ON -> a-1 OFF, a ON",
    "a ON, a OFF -> a-1 OFF, a ON"
    # identity functions
    # "a ON, b ON -> a ON, b ON"
    # "a OFF, b OFF -> "
]

def unique_heap_push(heap, elem):
    elem = (elem.time, elem.state) 
    if elem in heap:
        return heap
    else:
        heapq.heappush(heap, elem)
        return heap

def unique_heap_update(heap, elems):
    for elem in elems:
        heap = unique_heap_push(heap, elem)
    return heap


# get time functions and states for named args:
# time1: { time_function: \x -> x-1, True }, ...
def parse_expr(expr_args):
    target_args = []
    base_times = {}  # where names like a appear
    for idx, arg in enumerate(expr_args):
        name, state = arg.strip().split(" ")
        state = True if state == "ON" else False
        if "+" in name:
            base_name, const_add = name.split("+")  # name: a+1, base_name: a
            time_offset = int(const_add)
        elif "-" in name:
            base_name, const_sub = name.split("-")
            time_offset = -int(const_sub)
        else:
            base_name = name
            base_times[name] = idx
            time_offset = 0
        target_args.append(ExprArg(base_name, state, time_offset))
    return target_args, base_times

# parse a function (rule), get functions for matching and evaluation 
def parse_func(expr):
    expr_args, expr_res = expr.split("->")
    expr_args, expr_res = expr_args.split(","), expr_res.split(",")
    expr_args, arg_times = parse_expr(expr_args)
    expr_res, _ = parse_expr(expr_res)
    args_len = len(expr_args)

    # matched args and parsed: time1: 10, time2: 11, ...
    def match(args):
        if len(args) != args_len:
            return False
        for arg, expr_arg in zip(args, expr_args):
            time, state = arg.time, arg.state
            base_arg_time = args[arg_times[expr_arg.base_name]].time
            if base_arg_time + expr_arg.time_offset != time or state != expr_arg.state:
                return False
        return True

    def results(args):
        out = []
        for res in expr_res:
            base_res_time = args[arg_times[res.base_name]].time
            res_time = base_res_time + res.time_offset
            out.append(UnnamedNote(res_time, res.state))
        return out

    return match, results, args_len


# set [match_f, results_f] for each rule in rules_str
rules = list(map(parse_func, rules_str))
max_arg_len = max(map(lambda x: x[2], rules))

# do guard pattern matching, like in haskell
# if matched then evaluate and return
# otherwise False
def match_evaluate(args):
    for match_f, results_f, args_len in rules:
        if match_f(args[:args_len]):
            return results_f(args)
    return False

def fix_program(program):
    notes_trees = defaultdict(list)
    notes_trees_idx = defaultdict(dict)
    notes_unfixed = defaultdict(list) 
    for line in program:
        time, state, note = line.split()
        time, state, note = int(time), True if state == "ON" else False, int(note)
        notes_unfixed[note].append(UnnamedNote(time, state))
    for note in notes_unfixed.keys():
        for i in range(len(notes_unfixed[note])):
            notes_slice = notes_unfixed[note][i:i+max_arg_len]
            notes_evaluated = match_evaluate(notes_slice)
            if not notes_evaluated:
                unique_heap_push( notes_trees[note], notes_unfixed[note][i])
            else:
                unique_heap_update( notes_trees[note], notes_evaluated)
        print(note, notes_trees[note])
    print()


def main():
    p = list(map(fix_program, programs))


if __name__ == "__main__":
    main()
