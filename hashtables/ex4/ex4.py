def has_negatives(a):
    d = {}                              # Declare dict
    a = [abs(item) for item in a]       # Change all values in list to positive numbers
    for item in set(a): d[item] = 0     # Add a unique key for each unique value in list to the dict with a value of 0
    for item in a: d[item] += 1         # For each value in list add 1 to its dictionary value when it is itterated over
    return [k for k in d if d[k] > 1]   # For each key in the dict if its corresponding value is greater than one return it

if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
