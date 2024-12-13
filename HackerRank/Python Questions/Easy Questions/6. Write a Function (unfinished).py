def is_leap(year):
    leap = True

    # Write your logic here
    if year % 4 == 0:
        leap = True
        if leap % 100 == 0:
            leap = False
            if leap % 400 == 0:
                leap = True
            else: 
                leap = False
        else: 
            leap = True
    else:
        leap = False

    print(leap)
    return leap 

year = int(input())