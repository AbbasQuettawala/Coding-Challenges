if __name__ == '__main__':

    # Creating an empty variable to store data in
    Data = []

    # This for loop is ran an "x" amount of times, upto the discretion of the user, for example if they type 3, it will iterate 3 times
    for _ in range(int(input())):  # Using _ is used when the value of the loop variable is not needed inside the loop. Its a convention for "throwaway" variables
        name = input()
        score = float(input())

        # need to save this input somehow
        Data.append((name, score))

    #print(Data)
    # Now, to sort them in order of grades (Using Bubble Sort)
    # The thinking behind this is if there are 4 names, we need to compare the first 2 names at once, then the next 2 names and so on, thus j is numberofdata - 1. Then, since there are 4 names, we do it 4 times to make sure they are in order, 
    # which is why i is number_of_data

    # In a tuple that is set up as Data = [('Abbas', 90.0), ('Salman', 100.0)], to access the name Abbas, we do Data[0][0], and if I want to access the name Salman, i do Data[1][0]
    #print(Data[1][0])

    # Making the order descending, which will help later

    number_of_data = len(Data)
    for i in range(number_of_data):
        for j in range(number_of_data-1):
            if Data[j][1] < Data[j+1][1]:
                # Making temp variable to save
                temp = Data[j]
                Data[j] = Data[j+1]
                Data[j+1] = temp

    # Printing the data    
    #print(Data)
            
    # OK Now, need to check if any two numbers are the same, then i need to list them alphabetically. 
    # Will do ANOTHER Bubble Sort but for names, but ONLY if scores are the same
    for i in range(number_of_data):
        for j in range(number_of_data-1):
            # FIRST check if the scores are the same
            if Data[j][1] == Data[j+1][1]:
                # Now make the conversion to swap names
                if Data[j][0].lower() > Data[j+1][0].lower():  # This is very interesting. Python compares letters in order of its alphabetical (lexographical) order. So technically, if asked Murtaza > Abbas, this will be true, since M comes after A in the alphabet
                    temp = Data[j]                              # SO, in my logic, if we are presented with a tuple of [(Murtaza, 100), (Abbas, 100)], in lexographic number, M is e.g 10 and A is 1. I ask python, if 10 > 1, then swap, cause 1, in this case A, needs to come before M
                    Data[j] = Data[j+1]
                    Data[j+1] = temp



    # Printing the data    
    #print(Data)


    lowest_num = float("inf")
    second_lowest_num = float("inf")
    # Now finally, need to print the second lowest scores
    # Before that, we need to find what the second lowest score actually is. For this, lets iterate through the tuples list, this was throwing errors when done ascended, so made it descending instead
    for i in range(number_of_data):
        if Data[i][1] < lowest_num:
            #print(Data[i][1])
            temp = lowest_num
            lowest_num = Data[i][1]
            second_lowest_num = temp
            
            #print("second Lowest num:", second_lowest_num)
            #print("Lowest num:", lowest_num)


  
    # Now, if any of the tuples have that score, append it to this new variable
    second_lowest_students = []
    for i in range(number_of_data):
        #print("in this loop")
        if Data[i][1] == second_lowest_num:
            #print("Something found")
            second_lowest_students.append(Data[i][0])

   
    # Now printing out the names
    for i in range(len(second_lowest_students)):
        print(second_lowest_students[i])


        



    
