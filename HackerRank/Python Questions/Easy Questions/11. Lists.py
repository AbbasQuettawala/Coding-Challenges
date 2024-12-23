if __name__ == '__main__':
    N = int(input())

    result_list = []
    # N is the amount of times a command will be given
    for i in range(N):
        split_words = []
        command = input()

        # We want to split the command string into each word or number
        split_words = command.split()

        print(split_words)

        if split_words[0] == "insert":
            result_list.insert(split_words[2], split_words[1])

        elif split_words[0] == "print":
            print(result_list)
        
        elif split_words[0] == "remove":
            temp_list = []  
            for i in range(len(result_list)):
              if split_words[1] == result_list[i]:
                  pass
              else:
                   
    