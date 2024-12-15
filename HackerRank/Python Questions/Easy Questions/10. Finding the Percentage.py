if __name__ == '__main__':
    n = int(input())    # Telling python how many times want to run the for loop to collect data
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()  # name gets the first element (e.g., 'Alice'). *line gets the remaining elements as a list (e.g., ['85', '90', '95']). This is called "extended unpacking."
        scores = list(map(float, line)) # Converts the list of score strings (e.g., ['85', '90', '95']) to a list of floats: [85.0, 90.0, 95.0].
        student_marks[name] = scores # Adds an entry to the student_marks dictionary with: The student's name ('Alice') as the key The list of scores ([85.0, 90.0, 95.0]) as the value.

    query_name = input() # This input is the name we need to find the average for

    # Finding the student marks with the name we have been asked to query, and saving it to a variable
    query_name_score = student_marks[query_name]
    #print(query_name_score)

    # Now calculating the total score
    added_score = 0
    length_of_scores = len(query_name_score)
    for i in range(len(query_name_score)):
        added_score += query_name_score[i]
    #print(added_score)
        
    # Now calculating average score:
    average_score = added_score / length_of_scores
    print(f"{average_score:.2f}")

