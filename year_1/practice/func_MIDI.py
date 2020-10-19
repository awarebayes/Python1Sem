from collections import namedtuple

ExprArg = namedtuple("ExprArg", ["name", "base_name", "state", "time_func"])
Arg = namedtuple("Arg", ["time", "state", "chord"])

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

# ignore structs
# time1 OFF, time2 OFF -> time2 OFF
# time1 ON, time1 ON-> time1 ON
# ~ time1 ON, time1+1 ON -> time1-1 ON, time1 OFF, time1+1 ON
# time1 ON, time2 ON -> time1 ON, time2-1 OFF, time2 ON  | time1 != time2+1

rules = [
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
            const_add = int(const_add)
            time_func = lambda t: t + const_add
            base_name = name.split("+")[0]
        elif "-" in name:
            base_name, const_sub = name.split("-")
            const_sub = int(const_sub)
            time_func = lambda t: t - const_sub
        else:
            base_name = name
            base_times[name] = idx
            time_func = lambda t: t
        target_args.append(ExprArg(name, base_name, state, time_func))
    return target_args, base_times


def parse_func(expr):
    expr_args, expr_res = expr.split("->")
    expr_args, expr_res = expr_args.split(","), expr_res.split(",")
    expr_args, arg_times = parse_expr(expr_args)
    expr_res, res_times = parse_expr(expr_res)
    args_len = len(expr_args)

    # matched args and parsed: time1: 10, time2: 11, ...
    def match(args):
        if len(args) < args_len:
            return False
        for arg, expr_arg in zip(args, expr_args):
            time, state = arg.time, arg.state
            base_arg_time = args[arg_times[expr_arg.base_name]].time
            if expr_arg.time_func(base_arg_time) != time or state != expr_arg.state:
                return False
        return True

    def results(args):
        pass

    return match, None


def main():
    print(rules[0])


if __name__ == "__main__":
    main()
