from collections import namedtuple
from typing import Callable, List, Tuple, Dict, Union

# structs go here
ExprArg = namedtuple("ExprArg", ["base_name", "state", "time_offset"])
ConstArg = namedtuple("ConstArg", ["time", "state"])
TemplateArg = Union[ExprArg, ConstArg]
UnnamedNote = namedtuple("UnnamedNote", ["time", "state"])

# types go here
time_name = str  # name of time
time_index = int  # where time occurs

# expression args is of form: b-1 ON, a+1 OFF
# when expression arg does not have time offset, its called "basic arg"
def parse_expr_arg(name: str, state_str: str) -> ExprArg:
    state = True if state_str == "ON" else False
    if "+" in name:
        basic_name, const_add = name.split("+")  # name: a+1, basic_name: a
        time_offset = int(const_add)
    elif "-" in name:
        basic_name, const_sub = name.split("-")  # name: b-1, basic_name: b
        time_offset = -int(const_sub)
    else:  # this is a basic arg
        basic_name = name
        time_offset = 0
    return ExprArg(basic_name, state, time_offset)


def parse_const_arg(name: str, state_str: str) -> ConstArg:
    state = True if state_str == "ON" else False
    return ConstArg(int(name), state)


# get time functions and states for args:
def parse_expr(expr_args: List[str]) -> Tuple[List[TemplateArg], Dict[str, int]]:
    result_args: List[TemplateArg] = []
    basic_times: Dict[time_name, time_index] = {}  # ties where basic args appear
    for idx, arg in enumerate(expr_args):
        name, state_str = arg.strip().split(" ")
        if all(map(str.isdigit, name)):  # this is const arg
            result_args.append(parse_const_arg(name, state_str))
        else:  # this is expession arg
            expr_arg = parse_expr_arg(name, state_str)
            result_args.append(expr_arg)
            if expr_arg.time_offset == 0:  # this is base expr arg
                basic_times[name] = idx

    return result_args, basic_times


# parse a function (rule), get functions for matching and evaluation
def parse_rule(rule_str) -> Tuple[Callable, Callable, int]:
    args, res = rule_str.split("->")
    args, res = args.split(","), res.split(",")
    args, basic_times = parse_expr(args)
    res, _ = parse_expr(res)
    args_len = len(args)

    # check if matches
    def match(notes: List[UnnamedNote]) -> Tuple[bool, int]:
        if len(notes) != args_len:
            return False, 0
        for note, arg in zip(notes, args):
            time, state = note.time, note.state
            if isinstance(arg, ExprArg):
                base_arg_time = notes[basic_times[arg.base_name]].time
                if (
                    base_arg_time + arg.time_offset != time
                    or state != arg.state
                ):
                    return False, 0
            elif isinstance(arg, ConstArg):
                if arg.time != time or arg.state != state:
                    return False, 0
        return True, len(notes)

    # evaluate
    def results(notes: List[UnnamedNote]) -> List[UnnamedNote]:
        out = []
        for r in res:
            if isinstance(r, ExprArg):
                base_res_time = notes[basic_times[r.base_name]].time
                res_time = base_res_time + r.time_offset
                out.append(UnnamedNote(res_time, r.state))
            elif isinstance(r, ConstArg):
                out.append(UnnamedNote(r.time, r.state))
        return out

    return match, results, args_len


# also returns max_arg_len
def read_rules(rules_path="./rules"):
    f = open(rules_path, "r")
    rules = []
    for line in f:
        line = line.strip()
        if not line or line[0] == "#":  # comment / blank line
            continue
        if "#" in line:
            line = line.split("#")[0]
        rules.append(line)

    f.close()
    rules = list(map(parse_rule, rules))
    max_arg_len = max(map(lambda x: x[2], rules))
    return rules, max_arg_len
