"""
An Intcode memory is a list of integers separated by commas (like 1,0,0,3,99). To run one, start by looking at the first integer (called pointerition 0). Here, you will find an opcode - either 1, 2, or 99. The opcode indicates what to do; for example, 99 means that the memory is finished and should immediately halt. Encountering an unknown opcode means something went wrong.

Opcode 1 adds together numbers read from two pointeritions and stores the result in a third pointerition. The three integers immediately after the opcode tell you these three pointeritions - the first two indicate the pointeritions from which you should read the input values, and the third indicates the pointerition at which the output should be stored.

Opcode 2 works exactly like opcode 1, except it multiplies the two inputs instead of adding them. Again, the three integers after the opcode indicate where the inputs and outputs are, not their values.

Once you're done processing an opcode, move to the next one by stepping forward 4 pointeritions.
"""

from itertools import combinations

from util import *

data = get_data(2, split=False)

ADD = 1
MULT = 2
HALT = 99


def intcode(memory):
    memory = list(map(int, memory))
    pointer = 0

    while memory[pointer] != HALT:
        input1 = memory[pointer + 1]
        input2 = memory[pointer + 2]
        output = memory[pointer + 3]
        if memory[pointer] == ADD:
            memory[output] = memory[input1] + memory[input2]
        elif memory[pointer] == MULT:
            memory[output] = memory[input1] * memory[input2]
        pointer += 4

    return memory[0]


def p1(data):
    memory = data.split(",")
    memory[1] = 12
    memory[2] = 2
    return intcode(memory)


def p2(data):
    """
    What is 100 * noun + verb?
    """
    target = 19690720

    data = data.split(",")

    nums = range(0, 100)
    combos = combinations(nums, 2)

    for combo in combos:
        program1 = data[:]
        program1[1] = combo[0]
        program1[2] = combo[1]

        if intcode(program1) == target:
            return 100 * combo[0] + combo[1]

        program2 = data[:]
        program2[1] = combo[1]
        program2[2] = combo[0]

        if intcode(program2) == target:
            return 100 * combo[1] + combo[0]


def test():

    run_tests(intcode, [("1,9,10,3,2,3,11,0,99,30,40,50", 3500)], delim=",")
    run_tests(intcode, [("1,0,0,0,99", 2)], delim=",")
    run_tests(intcode, [("2,3,0,3,99", 2)], delim=",")
    run_tests(intcode, [("2,4,4,5,99,0", 2)], delim=",")
    run_tests(intcode, [("1,1,1,4,99,5,6,0,99", 30)], delim=",")


test()
print("Result1:", p1(data))
print("Result2:", p2(data))
