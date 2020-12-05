import operator as op
from collections import namedtuple

# operation tree structure
Tree = namedtuple("Expr", ["left", "right", "op"])


# evaluates tree
def execute_tree(tree):
    if not isinstance(tree, Tree):
        return tree
    left, right = tree.left, tree.right
    if isinstance(tree.left, Tree):
        left = execute_tree(tree.left)
    if isinstance(tree.right, Tree):
        right = execute_tree(tree.right)
    return tree.op(left, right)


# turns tree to string
def stringify_tree(tree):
    if not isinstance(tree, Tree):
        return str(tree)
    return (
        f"({stringify_tree(tree.left)} {op_map[tree.op]} {stringify_tree(tree.right)})"
    )


priority = ["+", "-", "%", "//", "/", "*", "√", "^"]
symb_map = {
    "+": op.add,
    "-": op.sub,
    "%": op.mod,
    "//": op.floordiv,
    "/": op.truediv,
    "*": op.mul,
    "^": op.pow,
    "√": lambda x: op.pow(x, 2),
}
# maps functions back to symbols
op_map = dict((v, k) for k, v in symb_map.items())

# split array by delimiter
def split_by(arr, delim):
    out = [
        [],
    ]
    for i in arr:
        if i != delim:
            out[-1].append(i)
        else:
            out.append([])
            continue
    return out

# make tree from array of string symbols
def make_tree(tree_arr, op_code=0):
    # print("make tree was called", tree_arr, "opcode", priority[op_code])

    # sqrt loperand
    if tree_arr[0] == "√":
        tree_arr = [tree_arr[1], "^", 0.5]

    # tree is one single node
    if len(tree_arr) == 1:
        if isinstance(tree_arr[0], Tree):
            return tree_arr[0]
        return float(tree_arr[0])

    symbol = priority[op_code]
    tree_arr = split_by(tree_arr, symbol)

    # nothing happened upon split
    if len(tree_arr) == 1:
        return make_tree(tree_arr[0], op_code + 1)

    operator = symb_map[symbol]
    out = Tree(make_tree(tree_arr[0]), make_tree(tree_arr[1]), operator)
    for i in range(2, len(tree_arr)):
        out = Tree(out, make_tree(tree_arr[i]), operator)
    return out

# find closing paranthesis starting from idx
def find_closing_par(tree_arr, start_idx):
    opened_parr = 0
    for i in range(start_idx, len(tree_arr)):
        if tree_arr[i] == "(":
            opened_parr += 1
        elif tree_arr[i] == ")":
            opened_parr -= 1
        if opened_parr == 0:
            return i
    return None

# split expression by parentheses 
def use_parentheses(tree_arr):
    if "(" not in tree_arr or ")" not in tree_arr:
        return tree_arr
    left_par = tree_arr.index("(")
    right_par = find_closing_par(tree_arr, left_par)
    left, inside, right = (
        tree_arr[:left_par],
        tree_arr[left_par + 1 : right_par],
        tree_arr[right_par + 1 :],
    )
    return (
        use_parentheses(left)
        + [
            make_tree(use_parentheses(inside)),
        ]
        + use_parentheses(right)
    )

# parse string to array of str symbols
def parse_string(inp):
    out = []
    for i in inp:
        if i.isdigit():
            if out and out[-1].isdigit():
                out[-1] = out[-1] + i
            else: # appand new expr_arr
                out.append(i)
        elif i in "+-/*%^√()":
            if i == "/" and out[-1] == "/": # replace /, / -> //
                out.pop()
                out.append("//")
            else:
                out.append(i)
    return out

# evaluate string
def eval_string(expr_str):
    expr_arr = parse_string(expr_str)
    tree_arr = use_parentheses(expr_arr)
    tree = make_tree(tree_arr)
    result = execute_tree(tree)

    # test result
    if result.is_integer():
        return int(result)
    return result

# testing
def main():
    expr_str = "( ( ( 82 * 3 ) - √(6%3)))"
    expr_arr = parse_string(expr_str)
    tree_arr = use_parentheses(expr_arr)
    tree = make_tree(tree_arr)
    print(">>", stringify_tree(tree))
    print("<<", execute_tree(tree))


if __name__ == "__main__":
    main()
