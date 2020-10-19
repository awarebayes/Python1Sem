from func_MIDI import parse_func, Arg

match_tests = [
    ("a ON, a ON -> a ON", [(10, True), (10, True)], True),
    ("a ON, a ON -> a ON", [(9, True), (10, True)], False),
    ("a ON, a ON -> a ON", [(10, True), (11, True)], False),
    ("a OFF, a OFF -> a OFF", [(10, False), (10, False)], True),
    ("a OFF, a OFF -> a OFF", [(9, False), (10, False)], False),
    ("a OFF, a OFF -> a OFF", [(10, False), (11, False)], False),
    ("a OFF, b OFF -> b OFF", [(10, False), (12, False)], True),
    ("a OFF, a ON -> a-1 OFF, a ON", [(10, False), (10, True)], True),
    ("a OFF, a ON -> a-1 OFF, a ON", [(10, True), (10, False)], False),
    ("a OFF, a ON -> a-1 OFF, a ON", [(10, True), (11, False)], False),
    ("a ON, a OFF -> a-1 OFF, a ON", [(10, True), (10, False)], True),
]

print("Running match tests...")
for func, args, target_res in match_tests:
    match_f, _ = parse_func(func)
    args_turple = [Arg(arg[0], arg[1], 0) for arg in args]
    match_res = match_f(args_turple)
    if match_res != target_res:
        print("Error while running test!")
        print("args:", args)
        print("match result:", match_res)
        print("target result:", target_res)
        exit()

print("All match tests successfully passed!")