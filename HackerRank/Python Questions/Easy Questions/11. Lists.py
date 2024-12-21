if __name__ == '__main__':
    # N is how many inputs the user wants to put in
    N = int(input())


    # Making final list
    results = []
    for i in range(N):
        command = input()

        # We want to split the command string into each word
        split_words = []
        split_words = command.split()

        # Implemeting logic ( Have not used commands as much as I can, using organic coding to do this)
        if split_words[0] == "insert":
            results.insert(int(split_words[1]), int(split_words[2]))

        elif split_words[0] == "print":
            print(results)

        elif split_words[0] == "remove":
            value_to_remove = int(split_words[1])
            newlist = []
            found = False

            for i in range(len(results)):
                if results[i] == value_to_remove and not found:
                    found = True
                    continue
                newlist.append(results[i])
            results = newlist

        elif split_words[0] == "append":
            results.append(int(split_words[1]))

        elif split_words[0] == "sort":
            for i in range(len(results)):
                for j in range(len(results) - 1):
                    if results[j] > results[j+1]:
                        temp = results[j]
                        results[j] = results[j+1]
                        results[j+1] = temp

        elif split_words[0] == "pop":
            results.pop()
            
        elif split_words[0] == "reverse":
            results = results[::-1]



 



    