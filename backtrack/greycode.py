def greycode(n):
    result = list()
    result.append(0)
    if n == 0:
        return result
    for i in range(0, n):
        inc = 1 << i
        for j in range(len(result)-1, -1, -1):
            result.append(inc + result[j])
    return result


if __name__ == '__main__':
    print greycode(4)
