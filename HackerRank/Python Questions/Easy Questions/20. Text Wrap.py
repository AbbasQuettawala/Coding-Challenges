# You are given a string  and width .
# Your task is to wrap the string into a paragraph of width .

# Function Description

# Complete the wrap function in the editor below.

# wrap has the following parameters:

# string string: a long string
# int max_width: the width to wrap to
# Returns

# string: a single string with newline characters ('\n') where the breaks should be


import textwrap

def wrap(string, max_width):

    empty = []

    for i in range(0, len(string), max_width): # This creates a range of numbers starting at 0, ending at len(string), and incrementing by max_width. Example for string = "ABCDEFGHIJKL" and max_width = 4: range(0, 12, 4) -> [0, 4, 8]. The loop iterates through the string in chunks of size max_width.
        empty.append(string[i:i + max_width]) # This line slices the string from index i to i + max_width and appends the resulting substring to the empty list.


    result = "\n".join(empty) # Joins all elemnts in the list together, separated with newline character per element

    return result

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)