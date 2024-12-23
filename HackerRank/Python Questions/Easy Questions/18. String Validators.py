if __name__ == '__main__':
    s = input() # I think this challenge wants to be done in the main function

    # Implementing logic 
    split = []
    for i in range(len(s)):
        split.append(s[i])
    
    # making found variables
    found = [0,0,0,0,0]

    # if found alpha numeric, alphabetical, digits, lowercase or uppercase once, then print true
    for i in range(len(split)):
        if split[i].isalnum():
            found[0] = 1
        if split[i].isalpha():
            found[1] = 1
        if split[i].isdigit():
            found[2] = 1
        if split[i].islower():
            found[3] = 1
        if split[i].isupper():
            found[4] = 1
        
    if found[0] == 1:
        print("True")
    else: 
        print("False")
    if found[1] == 1:
        print("True")
    else: 
        print("False")
    if found[2] == 1:
        print("True")
    else: 
        print("False")
    if found[3] == 1:
        print("True")
    else: 
        print("False")
    if found[4] == 1:
        print("True")
    else: 
        print("False")