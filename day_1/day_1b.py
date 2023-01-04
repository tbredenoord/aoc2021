def get_inputs():
    with open("input.txt", "r") as f:
        inputs = []
        for i in f:
            if len(i) == 0:
                continue
            inputs.append(int(i))
    return inputs

inputs = get_inputs()
count = 0
combined = [None, None, None]
increased = 0
last = None
for i in inputs:
    modv = count % 3
    count += 1
    combined[modv] = i
    if combined[2] == None:
        combined
        continue
    combined_value = sum(combined)
    if last == None:
        last = combined_value
        continue 
    if combined_value > last:
        increased += 1
    last = combined_value

print("increased " + str(increased))