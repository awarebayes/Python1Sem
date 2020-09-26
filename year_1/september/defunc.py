import re

f_table = {
    "v_new": {
        "name": "v_new",
        "args": ["__point1", "__point2"],
        "vars": [],
        "body": "res = (__point1[0] - __point2[0], __point1[1] - __point2[1], (__point1, __point2))\n",
    },
    "v_dot": {
        "name": "v_dot",
        "args": ["__vector1", "__vector2"],
        "vars": [],
        "body": "res = __vector1[0] * __vector2[0] + __vector1[1] * __vector2[1]\n",
    },
    "v_len": {
        "name": "v_len",
        "args": ["__vector"],
        "body": "res = (__vector[0] ** 2 + __vector[1] ** 2) ** 0.5\n",
        "vars": [],
    },
    "v_ang": {
        "name": "v_ang",
        "args": ["__vector1", "__vector2"],
        "vars": ["__len1", "__len2"],
        "body": """
__len1, __len2 = (__vector1[0] ** 2 + __vector1[1] ** 2) ** 0.5, (__vector2[0] ** 2 + __vector2[1] ** 2) ** 0.5
res = 0
if __len1 != 0 and __len2 != 0:
res = acos((__vector1[0] * __vector2[0] + __vector1[1] * __vector2[1]) / (__len1 * __len2))

        """,
    },
    "triangle_angle": {
        "name": "triangle_angle",
        "args": ["side1", "side2"],
        "vars": ["points1", "points2", "center", "start", "end"],
        "body": """
points1 = set(side1[2])
points2 = set(side2[2])
center = points1.intersection(points2)
start, end = (points1 - center).pop(), (points2 - center).pop()
center = center.pop()
res = v_ang(v_new(center, start), v_new(center, end))

        """,
    },
}

fn_names = list(f_table.keys())
fn_processed = dict([(fn_name, False) for fn_name in fn_names])
call_count = dict([(fn_name, 0) for fn_name in fn_names])


def substitude_function(name, args):
    f_template = f_table[name]
    fstr = ""
    fstr += "# begin function {}\n".format(name) + "\n"
    fstr += "{} = {}".format(", ".join(f_template["args"]), ", ".join(args)) + "\n"
    fstr += f_template["body"] + "\n"
    if f_template["vars"]:
        fstr += "del {}".format(", ".join(f_template["vars"])) + "\n"
    fstr += "# end function {}\n".format(name)
    fstr += "\n"
    return fstr


def eval_fn_expr(fn_str):
    matches = list(
        re.finditer(r"(?P<name>\w+)\s?\((?P<arg>(?P<args>\w+(,\s?)?)+)\)", fn_str)
    )
    if not matches:
        return fn_str
    matched_funcs = [fn_str[m.start() : m.end()] for m in matches]
    fn_dicts = [m.groupdict() for m in matches]
    call_res = {}
    fstr = ""
    for fn_dict, fn_content in zip(fn_dicts, matched_funcs):
        name = fn_dict["name"]
        if name not in fn_names:
            continue
        del fn_dict["args"]
        fn_dict["args"] = [arg.strip() for arg in fn_dict["arg"].split(",")]
        del fn_dict["arg"]
        if not fn_processed[name]:
            process_body(name)
        fstr += substitude_function(**fn_dict)
        res_name = "res_{}_{}".format(name, call_count[name])
        fstr += res_name + " = res \n\n"
        call_count[name] += 1
        call_res[fn_content] = res_name

    final_call = fn_str
    for call, res in call_res.items():
        final_call = final_call.replace(call, res)
    fstr += "res = " + final_call + "\n"
    return fstr


def process_body(name):
    body, outb = f_table[name]["body"],  ""
    for line in body.splitlines(keepends=True):
        outb += eval_fn_expr(line)
    f_table[name]["body"] = outb
    fn_processed[name] = True
    return outb


print(eval_fn_expr("triangle_angle(some_vec, v_new((0, 0), (1, 2)) / v_len(arg1))"))
