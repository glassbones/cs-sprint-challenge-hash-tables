def intersection(arrs):
    d = dict((item, 0) for item in arrs[0])                                             # Create Dict from first list in arrs. {key: list item, value: 0}
    for arr in arrs: d = dict((item, d[item]+1) for item in arr if item in d.keys())    # Itterate over the remaining lists in arrs and if any of their items match the dict keys add 1 to the dict value.
    return [k for k in d if d[k] == len(arrs)]                                          # return the items that appeared in all lists
    
if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
