def count_substring(string, sub_string):

    # Initialize a counter to track the number of occurrences
    count = 0
    
    # Loop through the string to check for matches
    for i in range(len(string) - len(sub_string) + 1):      # We do this to ensure we extract text that is part of the string, and does not go out of bounds. So for example, a 10 letter string and 3 letter sub string, we go 1:3, then 2:4, then 3:5, and so on, and we do this and we need to go over it 8 times
        # Extract part of the string that matches the length of the substring
        part = string[i:i + len(sub_string)]     # This line of code will splice a part of the string at i, and then go to the length of the substring.    
        
        # Compare the extracted part with the substring
        if part == sub_string:
            count += 1  # Increment the count if there's a match
    
    return count 


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)