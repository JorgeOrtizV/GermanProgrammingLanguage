import sys
import json

def do_func(env, args):
    assert len(args) == 2
    params = args[0]
    body = args[1]
    return ["func", params, body]

def do_get(env, args):
    assert len(args) == 1
    assert isinstance(args[0], str)
    assert args[0] in env, f"Unknown variable {args[0]}"
    return env[args[0]]

def do_set(env, args):
    assert len(args) == 2
    assert isinstance(args[0], str)
    value = do(env, args[1])
    env[args[0]] = value
    return value

def do_seq(env, args):
    assert len(args) > 0
    for item in args:
        result = do(env, item)
    return result
###############################################################
def do_multiplication(envs,args):
    assert len(args) == 2
    left = do(envs,args[0])
    right = do(envs,args[1])
    return left * right

def do_division(envs,args):
    assert len(args) == 2
    assert args[1] != 0
    left = do(envs,args[0])
    right = do(envs,args[1])
    return left/right

def do_power(envs,args):
    assert len(args) == 2
    left = do(envs,args[0])
    right = do(envs,args[1])
    return left ** right

def do_print(envs,args):
    assert len(args) >1
    print(args[0])

def do_array(envs,args):
    assert len(args) == 1
    N = args[0]
    array = [_] * N 
    return array

def do_get_array(envs,args):
    assert len(args) == 2
    value = args[0][args[1]]
    print(value)

def do_set_array(envs,args):
    assert len(args) ==3
    value = args[0][args[1]]
    args[2] = value

def do_get_dict(envs,args):
    assert len(args) == 2
    value = args[0][args[1]]
    print(value)

def do_set_dict(envs,args):
    assert len(args) ==3
    value = args[0][args[1]]
    args[2] = value

#################################################################
OPERATIONS = {
    func_name.replace("do_",""): func_body
    for (func_name, func_body) in globals().items()
    if func_name.startswith("do_")
}


def do(envs,expr):
    if isinstance(expr,int):
        return expr
   
    assert isinstance(expr,list)
    assert expr[0] in OPERATIONS, f"Unknown operation {expr[0]}"
    func = OPERATIONS[expr[0]]
    return func(envs, expr[1:])

def do_call(env, args):
    # Set up the call.
    assert len(args) >= 1
    name = args[0]
    values = [do(env, a) for a in args[1:]]

    # Find the function.
    func = env_get(env, name)
    assert isinstance(func, list) and (func[0] == "func")
    params, body = func[1], func[2]
    assert len(values) == len(params)

    # Run in new environment.
    env.append(dict(zip(params, values)))
    result = do(env, body)
    env.pop()

    # Report.
    return result

def main():
    assert len(sys.argv) == 2, "Usage: lgl interpreter.py filename.gsc"
    with open(sys.argv[1], "r") as source_file:
        program = json.load(source_file)
    assert isinstance(program,list)
    envs = [{}]
    result = do(envs,program)
    print(f"=> {result}")

if __name__ == "__main__":
    main()