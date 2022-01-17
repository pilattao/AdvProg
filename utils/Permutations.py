def permute(data, result, i=0):
    length = len(data)
    if i == length:
        result.append(''.join(data))
        print(''.join(data))
    else:
        for j in range(i, length):
            data[i], data[j] = data[j], data[i]
            permute(data, result, i + 1)
            data[i], data[j] = data[j], data[i]
