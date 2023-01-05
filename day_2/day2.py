def get_inputs():
    with open("day_2/input.txt", "r") as f:
        inputs = []
        for i in f:
            if len(i) == 0:
                continue
            inputs.append(i.strip().split(" "))
    return inputs

def calculate_position(inp):
    xpos = 0
    ypos = 0    
    for i in inp:
        if i[0] == 'forward':
            xpos += int(i[1])
            continue
        if i[0] == 'up':
            ypos -= int(i[1])
            continue
        if i[0] == 'down':
            ypos += int(i[1])
            continue
    return [xpos, ypos]


qq = get_inputs()
result = calculate_position(qq)
print(result)
print(result[0] * result[1])

#Day 2
def calculate_position_d2(inp):
    xpos = 0
    ypos = 0   
    aim = 0
    for i in inp:
        val = int(i[1])
        if i[0] == 'forward':
            xpos += val
            ypos += val * aim
            continue
        if i[0] == 'up':
            aim -= val
            continue
        if i[0] == 'down':
            aim += val
            continue
    return [xpos, ypos]

result = calculate_position_d2(qq)
print(result)
print("horizontal * depth =", result[0]*result[1])