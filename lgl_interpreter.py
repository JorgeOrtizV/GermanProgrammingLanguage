from functools import reduce
import json
import sys

def multiplication(elements):
    assert len(elements) > 1
    elements = list(map(do, elements))
    return reduce(lambda x,y : x*y, elements)


def do(instruction):
    if isinstance(instruction, int):
        return instruction
    try:
        func = dict(globals().items())[instruction[0]]
        return func(instruction[1:])
    except Exception as e:
        print(e)


if __name__ == "__main__":
    args = sys.argv[1:]
    assert len(args) == 1, "Script only expects a .gsc file as argument"
    with open(args[0], 'r') as source_file:
        instructions = json.load(source_file)
    for instruction in instructions:
        assert isinstance(instruction, list)
        result = do(instruction)
        print(result)