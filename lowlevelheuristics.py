def firstFit(result, item, capacity):
    allocated = False
    for i, bin in enumerate(result):
        if bin + item <= capacity:
            result[i] += item
            allocated = True
            break

    if not allocated:
        result.append(item)

    return result


def nextFit(result, item, capacity):
    allocated = False
    if len(result) > 0:
        bin = result[len(result) - 1]
        if bin + item <= capacity:
            result[len(result) - 1] += item
            allocated = True

    if not allocated:
        result.append(item)

    return result


def bestFit(result, item, capacity):
    best = float('inf')
    pos = None
    for i, bin in enumerate(result):
        if bin + item <= capacity:
            space = capacity - (bin + item)
            if space < best:
                best = space
                pos = i
                break

    if pos == None:
        result.append(item)
    else:
        result[pos] += item

    return result


def worstFit(result, item, capacity):
    worst = -1
    pos = None
    for i, bin in enumerate(result):
        if bin + item <= capacity:
            space = capacity - (bin + item)
            if space > worst:
                worst = space
                pos = i
                break

    if pos == None:
        result.append(item)
    else:
        result[pos] += item

    return result