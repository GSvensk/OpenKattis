import sys

# int to word dictionary and word to int dictionary
dictionary = {}
dictionary2 = {}

for lines in sys.stdin:
    # remove newlines and format
    lines = str(lines).replace('\n', '')
    line = lines.split()

    if line[0] == 'def':
        # if previously defined
        if dictionary.__contains__(line[1]):
            # remove old definition
            del dictionary2[dictionary[line[1]]]

        # add definition
        dictionary2[int(line[2])] = line[1]
        dictionary[line[1]] = int(line[2])

    # if calculation is required
    elif line[0] == 'calc':
        counter = 2
        try:
            # add initial number
            total = dictionary[line[1]]
            character = line[counter]
            # check sign
            while character != '=':
                if character == '+':
                    total += int(dictionary[line[counter+1]])
                elif character == '-':
                    total -= int(dictionary[line[counter+1]])

                # jump to the signs
                counter += 2
                character = line[counter]

            print(lines[5:] + ' ' + dictionary2[total])

        # if any key is undefined in the dictionary, print request and unknown
        except KeyError:
            print(lines[5:] + ' unknown')

    # clear dictionaries
    else:
        dictionary = {}
        dictionary2 = {}
