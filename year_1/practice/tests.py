from func_MIDI import parse_func, UnnamedNote

#                  _       _
#  _ __ ___   __ _| |_ ___| |__
# | '_ ` _ \ / _` | __/ __| '_ \
# | | | | | | (_| | || (__| | | |
# |_| |_| |_|\__,_|\__\___|_| |_|


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
    match_f, _, _ = parse_func(func)
    args_turple = [UnnamedNote(arg[0], arg[1]) for arg in args]
    match_res = match_f(args_turple)
    if match_res != target_res:
        print("Error while running test!")
        print("args:", args)
        print("match result:", match_res)
        print("target result:", target_res)
        exit()

print("All match tests successfully passed!\n")

#  _ __ ___  ___ _   _| | |_ ___
# | '__/ _ \/ __| | | | | __/ __|
# | | |  __/\__ \ |_| | | |_\__ \
# |_|  \___||___/\__,_|_|\__|___/

match_tests = [
    ("a ON, a ON -> a ON", [(10, True), (10, True)], [(10, True)]),
    ("a OFF, a OFF -> a OFF", [(10, False), (10, False)], [(10, False)]),
    ("a OFF, b OFF -> b OFF", [(10, False), (12, False)], [(12, False)]),
    (
        "a OFF, a ON -> a-1 OFF, a ON",
        [(10, False), (10, True)],
        [(9, False), (10, True)],
    ),
    (
        "a ON, a OFF -> a-1 OFF, a ON",
        [(10, True), (10, False)],
        [(9, False), (10, True)],
    ),
]
print("Running results tests...")
for func, args, target_res in match_tests:
    _, results_f, _ = parse_func(func)
    args_turple = [UnnamedNote(arg[0], arg[1]) for arg in args]
    res_turple = [UnnamedNote(res[0], res[1]) for res in target_res]
    results = results_f(args_turple)
    if results != res_turple:
        print("Error while running test!")
        print("args:", args)
        print("result:", results)
        print("target result:", res_turple)
        exit()

print("All retults tests successfully passed!\n")
print("All tests successfully passed!")
