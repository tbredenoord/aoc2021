with open("input.txt", "r") as f:
    last = None
    increasing = 0
    for i in f:
        if len(i) == 0:
            continue
        depth = int(i)
        if last == None:
            last = depth
            print(str(depth)+  " N/A")
            continue
        if depth > last:
            increasing += 1
            print(str(depth)+  " increasing")
        else:
            print(str(depth) + " decreasing")
        last = depth
    print("incr: " + str(increasing))