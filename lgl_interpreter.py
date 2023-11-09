import sys
import json

import csv
from datetime import datetime
import functools
import argparse

######## CREATE THE TRACE ########################

def trace(trace_file):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            call_id = id(args) + id(kwargs)
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
            with open(trace_file, 'a', newline='') as f:
                writer = csv.writer(f)
                writer.writerow([call_id, func.__name__, 'start', timestamp])
            result = func(*args, **kwargs)
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
            with open(trace_file, 'a', newline='') as f:
                writer = csv.writer(f)
                writer.writerow([call_id, func.__name__, 'stop', timestamp])
            return result
        return wrapper
    return decorator

#####################################################

def main():
    parser = argparse.ArgumentParser(description='LGL Interpreter with optional tracing.')
    parser.add_argument('filename', help='The LGL script file to interpret.')
    parser.add_argument('--trace', help='Enable tracing and specify the trace file.', default='')
    args = parser.parse_args()

    if args.trace:
        global trace
        trace = trace(args.trace)
    else:
        def trace(func):
            return func

    with open(args.filename, "r") as source_file:
        program = json.load(source_file)
    print(program)
    assert isinstance(program, list)
    envs = [{}]
    result = do(envs, program)
    print(f"Last result => {result}")
################################################
in_use = None

def do_funktion(envs,args): # TODO: Review what this does
    assert len(args) == 2
    params = args[0]
    body = args[1]
    return ["funktion",params,body]

def do_method(envs, args):
    #import pdb; pdb.set_trace()
    assert len(args) >= 1
    func = do(envs, args[0])
    arguments = args[1:]
    values = [do(envs,arg) for arg in arguments]
    assert isinstance(func,list)
    assert func[0] == "funktion"
    func_params = func[1]
    assert len(func_params) == len(values)

    local_frame = dict(zip(func_params,values))
    envs.append(local_frame)
    body = func[2]
    result = do(envs,body)
    envs.pop()
    return result

def do_aufrufen(envs,args): 
    #import pdb; pdb.set_trace()
    assert len(args) >= 1
    name = args[0]
    arguments = args[1:]
    # eager evaluation
    values = [do(envs,arg) for arg in arguments]

    func = envs_get(envs,name)
    assert isinstance(func,list)
    assert func[0] == "funktion"
    func_params = func[1]
    assert len(func_params) == len(values)

    local_frame = dict(zip(func_params,values))
    envs.append(local_frame)
    body = func[2]
    result = do(envs,body)
    envs.pop()

    return result

def envs_get(envs, name):
    global in_use
    assert isinstance(name,str)
    #import pdb; pdb.set_trace()
    for e in reversed(envs):
        if name in e.keys():
            in_use = name
            return e[name]
        
    # python like version
    # if name in envs[-1]:
    #    return e[name]
    #if name in envs[0]:
    #    return e[name]
    assert False, f"Unknown variable name {name}"

def envs_set(envs,name,value):
    assert isinstance(name,str)
    # for e in reversed(envs):
    #     if name in e:
    #         e[name] = value
    #         return
    if isinstance(value, str):
        exec("{}={}".format(name, "\'"+value+"\'"))
    else:
        exec("{}={}".format(name, value))
    envs[-1][name] = value        


def do_setzen(envs,args): # Set a value
    assert len(args) == 2
    assert isinstance(args[0],str)
    var_name = args[0]
    value = do(envs,args[1])
    envs_set(envs,var_name, value)
    print("Created instance {} with value {}".format(var_name, value))
    return value

def do_abrufen(envs,args): # Obtain value of variable
    assert len(args) == 1
    return envs_get(envs,args[0])
@trace('trace_file.log')
def do_addieren(envs,args):
    assert len(args) == 2
    left = do(envs,args[0])
    right = do(envs,args[1])
    return left + right

def do_absolutwert(envs,args):
    assert len(args) == 1
    value = do(envs,args[0])
    return abs(value)

def do_subtrahieren(envs,args):
    assert len(args) == 2
    left = do(envs,args[0])
    right = do(envs,args[1])
    return left - right

def do_abfolge(envs,args):
    assert len(args) > 0
    it = 1
    for operation in args:
        result = do(envs,operation)
        print("Operation {} -> {}".format(it, result))
        it += 1
    return result

###########  extended funcs   #############
def do_multiplication(envs, args):
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
@trace('trace_file.log')
def do_power(envs,args):
    assert len(args) == 2
    left = do(envs,args[0])
    right = do(envs,args[1])
    return left ** right

def do_print(envs,args):
    assert len(args) == 1
    op = do(envs,args[0])
    print(op)
    # Print doesn't return a value


def do_dict(envs,args):
    assert len(args) < 3
    if  len(args) == 0:
        return dict()
    else:
        temp_dict = dict()
        for i in range(len(args[0])):
            if isinstance(args[1][i], list):
                value = do(envs, args[1][i])
            else:
                value = args[1][i]
            temp_dict[args[0][i]] = value
        return temp_dict

def do_get_dict(envs,args):
    assert len(args) == 2
    if isinstance(args[0], list):
        mydict = do(envs, args[0])
    else:
        mydict = args[0]
    value = mydict[args[1]]
    return value

def do_set_dict(envs,args):
    #import pdb; pdb.set_trace()
    assert len(args) == 3
    if isinstance(args[1], list):
        key = do(envs, args[1])
    else:
        key = args[1]
    if isinstance(args[2], list):
        value = do(envs, args[2])
    else:
        value = args[2]
    if isinstance(args[0], list):
        mydict = do(envs, args[0])
        mydict[key] = value
    else:
        args[0][key] = value
    # Setting value in an array doesn't return a function.

def do_merge_dict(envs,args):
    assert len(args) == 3
    value1 = do(envs,args[1])
    value2 = do(envs,args[2])
    value = {**value1, **value2}
    return value

# Create an array
def do_array(envs, args):
    assert len(args) == 1
    N = args[0]
    array = [None] * N 
    return array

# Get N value of array
def do_get_array(envs,args):
    assert len(args) == 2
    if isinstance(args[0], list):
        array = do(envs, args[0])
    else:
        array = args[0]
    value = array[args[1]]
    return value

# Set value of an array
def do_set_array(envs,args):
    assert len(args) == 3
    if isinstance(args[0], list):
        array = do(envs, args[0])
        array[args[1]] = args[2]
    else:
        args[0][args[1]] = args[2]
    # Setting value in an array doesn't return a function.

def do_while(envs, args):
    # condition, body
    assert len(args) == 2
    state_condition = do(envs, args[0])
    if state_condition == True:
        do(envs, args[1])
        do_while(envs, args)
    else:
        return

# ["do_while_condition", 1, "lt", 2]
def do_while_condition(envs, args):
    assert len(args) == 3
    assert isinstance(args[1], str)
    item1 = do(envs, args[0])
    item2 = do(envs, args[2])
    if args[1] == 'lt':
        return item1 < item2
    elif args[1] == 'gt':
        return item1 > item2
    elif args[1] == 'eq':
        return item1 == item2
    
#################  Extended OOP  ##########################




OPERATIONS = {
    func_name.replace("do_",""): func_body
    for (func_name, func_body) in globals().items()
    if func_name.startswith("do_")
}


def do(envs,expr):
    if isinstance(expr,int) or isinstance(expr, str) or isinstance(expr, float):
        return expr
    assert isinstance(expr,list)
    assert expr[0] in OPERATIONS, f"Unknown operation {expr[0]}"
    func = OPERATIONS[expr[0]]
    return func(envs, expr[1:])


#def main():
 #   assert len(sys.argv) == 2, "Usage: funcs-demo.py filename.gsc"
  #  with open(sys.argv[1], "r") as source_file:
   #     program = json.load(source_file)
    #print(program)
    #assert isinstance(program,list)
    #envs = [{}]
    #result = do(envs,program)
    #print(f"Last result => {result}")

if __name__ == "__main__":
    main()