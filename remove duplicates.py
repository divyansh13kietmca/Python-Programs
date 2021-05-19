def remove_duplicates(value):
    elements = [value[i] for i in range(len(value))]
    results = []
    res = ""
    for i in range(len(elements)):
        if elements[i] not in results:
            results.append(elements[i])

    for result in results:
        res += result
    return res
print(remove_duplicates("11223445566666ababzzz@@@123#*#*"))
