def all_numeric(s):
    return all(map(str.isdigit, s)) 

def fool_proof_int_input(greeting):
    while True:
        x = input(greeting)
        if all_numeric(x):
            return int(x)
        print("Bad input!")

def fool_proof_float_input(greeting):
    while True:
        x = input(greeting)

        n_dots = 0 
        n_exp = 0
        for i in x:
            if i == '.':
                n_dots += 1
            if i == 'e':
                n_exp += 1
            if not i.isdigit() and i not in ["e", "+", "-", "."]:
                print("invalid char in input:", i)
                continue
        if n_dots > 1:
            print("There should be only one dot!")
            continue
        
        if n_exp > 1:
            print("There should be only one exponent!")
            continue

        if x == '':
            print("Input something, you dord!")
            continue
        if all_numeric(x): # of form 123
            return float(x)
        if '.' in x and 'e' not in x: # of form 12.345
            if all(map(all_numeric, x.split("."))):
                return float(x)
        elif '.' not in x and 'e' in x: # of form 10e-5
            integer, exp =  x.split("e")
            if not integer or not exp:
                print("Either of [integer, exponent] do not exist")
                continue
            if not exp:
                print("exponent should exist!")
                continue
            if exp[0] in ['-', '+']: # delete exponent sign
                exp = exp[1:]
            if all_numeric(integer) and all_numeric(exp):
                return float(x)
        elif '.' in x and 'e' in x: # of form 123.45e6
            integer, frac = x.split(".")
            if "e" not in frac:
                print("Wrong exponent in float!")
                continue
            frac, exp = frac.split("e")

            # 123.45e6 -> integer: "123", frac: "45", exp "6"
            if not integer or not exp or not frac:
                print("Either of [integer, exponent, fraction] do not exist")
                continue
            if exp[0] in ['-', '+']: # delete exponent sign
                del exp[0]
            if all(map(all_numeric, [integer, frac, exp])):
                return float(x)
        print("Something is wrong with your float, pal!")


