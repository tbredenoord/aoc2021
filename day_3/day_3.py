def get_inputs():
    with open("day_3/input.txt", "r") as f:
        inputs = []
        for i in f:
            if len(i) == 0:
                continue
            inputs.append(i.strip())
    return inputs

def process_inputs(inputs):
    ninputs = len(inputs)
    result_one= []
    result_zero = []
    for i in range(len(inputs[0])):
        ones = len([1 for k in inputs if k[i] == '1'])
        if (ninputs - ones) > ones:
            result_one.append("0")
            result_zero.append("1")
        else:
            result_one.append("1")
            result_zero.append("0")
    return ["".join(result_one), "".join(result_zero)]

inputs = get_inputs()
results = process_inputs(inputs)
print("power consumption:", int(results[0],2) * int(results[1], 2))

#Part 2
def process_inputs2(inputs, eq):
    ninputs = len(inputs)
    result_one= []
    result_zero = []
    for i in range(len(inputs[0])):
        ones = len([1 for k in inputs if k[i] == '1'])
        if (ninputs - ones) == ones:
            result_one.append(eq)
            result_zero.append(eq)
            continue
        if (ninputs - ones) > ones:
            result_one.append("0")
            result_zero.append("1")
        else:
            result_one.append("1")
            result_zero.append("0")
    return ["".join(result_one), "".join(result_zero)]

def find_rating(inputs, str_if_equal, index):
    common = process_inputs2(inputs, str_if_equal)[index]
    for i in range(len(common)):
        inputs = [value for value in inputs if value[i] == common[i]]
        if len(inputs) == 1:
            return inputs[0]
        common = process_inputs2(inputs, str_if_equal)[index]
    return ""

print("life support rating:", int(find_rating(inputs, '1', 0), 2) * int(find_rating(inputs, '0', 1), 2))