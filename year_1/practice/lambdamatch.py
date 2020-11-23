from collections import namedtuple
from typing import Callable, List, Tuple, Dict, NewType

# structs go here
ExprArg = namedtuple("ExprArg", ["base_name", "state", "time_offset"])
UnnamedNote = namedtuple("UnnamedNote", ["time", "state"])

# types go here
time_name = str  # name of time
time_index = int  # where time occurs

# get time functions and states for named args:
# time1: { time_function: \x -> x-1, True }, ...
def parse_expr(expr_args: List[str]) -> Tuple[List[ExprArg], Dict[str, int]]:
    target_args: List[ExprArg] = []
    base_times: Dict[time_name, time_index] = {}  # where names like a appear
    for idx, arg in enumerate(expr_args):
        name, state_str = arg.strip().split(" ")
        state = True if state_str == "ON" else False
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
def parse_func(expr) -> Tuple[Callable, Callable, int]:
    expr_args, expr_res = expr.split("->")
    expr_args, expr_res = expr_args.split(","), expr_res.split(",")
    expr_args, arg_times = parse_expr(expr_args)
    expr_res, _ = parse_expr(expr_res)
    args_len = len(expr_args)

    # check if matches
    def match(args: List[UnnamedNote]) -> bool:
        if len(args) != args_len:
            return False
        for arg, expr_arg in zip(args, expr_args):
            time, state = arg.time, arg.state
            base_arg_time = args[arg_times[expr_arg.base_name]].time
            if base_arg_time + expr_arg.time_offset != time or state != expr_arg.state:
                return False
        return True


    def results(args: List[UnnamedNote]) -> List[UnnamedNote]:
        out = []
        for res in expr_res:
            base_res_time = args[arg_times[res.base_name]].time
            res_time = base_res_time + res.time_offset
            out.append(UnnamedNote(res_time, res.state))
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
    rules = list(map(parse_func, rules))
    max_arg_len = max(map(lambda x: x[2], rules))
    return rules, max_arg_len
