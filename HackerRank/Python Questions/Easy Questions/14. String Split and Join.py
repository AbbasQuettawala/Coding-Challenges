def split_and_join(line):

    # First split the string using the split function
    split_line = line.split()

    # Then, we just need to rejoin back into one string, but put hyphens instead of spaces. The question specifically asks to use a the join method, instead of using any for loops
    joint_line = "-".join(split_line)  # We recall that the join function will join the iterables, in this case, the words in the array, and then join them with a separator, which we have set to "-" hyphen.

    return joint_line

# Main function
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)