def mutate_string(string, position, character):

    # We want to change the given string to put in a letter at a given index
    # First lets convert to string
    string_list = []
    for i in range(len(string)):
        string_list.append(string[i])
    
    # Now that we have a list, we want to change the single position in that list
    string_list[position] = character

    # Now convert back into a string
    back_to_string = ''.join(string_list)


    return back_to_string

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)