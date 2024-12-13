if __name__ == '__main__':
    n = int(input())


    # Creating empty string
    result = ""

    for i in range(1, n + 1): # Range function starts is inclusive but stop is exclusive
        result += str(i)

    print(result)