def sort_list(arrays):
    for x in arrays:
        for y in arrays:
            if len(arrays[x]) < len(arrays[y]):
                temp = arrays[x]
                arrays[x] = arrays[y]
                arrays[y] = temp
    return arrays


print(sort_list([1, 4, 2, 6, 3, 7, 4]))
