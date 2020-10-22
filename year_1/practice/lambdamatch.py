from collections import namedtuple

ExprArg = namedtuple("ExprArg", ["base_name", "state", "time_offset"])
UnnamedNote = namedtuple("UnnamedNote", ["time", "state"])


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
