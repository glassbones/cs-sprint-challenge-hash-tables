def makeDict(files):
    d = {}                                          # Declare dict
    for filePath in files:                          # For each filepath in the list of filepaths

        f = ''                                          
        for char in reversed(filePath):             # Take that file path and get rid of everything that occurs before the last '/'
            if char == '/':                         # For instance: "Home/tacos/pizza/eggs.jpg" would now just be "eggs.jpg"
                f = f[::-1] # reversing string
                break
            else: f += char
        if f in d.keys(): d[f].append(filePath)     # If that reduced string is a key in the dict add it's path to the values list
        else: d.update({f: [filePath]})             # If its not, make it a key then add it's path to the values list
                     
    return d                                        # Return the dict                                       


def finder(files, queries):
    d = makeDict(files)                 # Make a dict of files and file paths
    results = []                        # Declare a results list
    for file in queries:                # For each file in the queries list
        if file in d.keys():            # If the file is in the dict
            for path in d[file]:        # Add the file's filepaths to the results list
                results.append(path)
    return results                      # Return results list


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
