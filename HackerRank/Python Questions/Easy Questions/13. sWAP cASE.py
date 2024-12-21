def swap_case(s):
    # s is the string we get as the input

    # Split the string as there may be multiple words
    split_string = s.split()

    # Making new array to store word
    new_array = []

    for j in range(len(split_string)):
        for i in range(len(split_string[j])):
            if split_string[j][i].islower(): # if the letter is lowercase then append it as uppercase
                new_array.append(split_string[j][i].upper())
            elif split_string[j][i].isupper():
                new_array.append(split_string[j][i].lower())
            else: 
                new_array.append(split_string[j][i])
        # Once the word is ended, we need to add a space:
        new_array.append(" ")
    

    # Now convert back to string
    new_string =  ''.join(new_array)# this join function will take all the elements in the iterable, in this case, an array, and join them into a string. Between each iterable, it will include in the separator, which we have set to '' since we dont want anything in between them

    return new_string

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
