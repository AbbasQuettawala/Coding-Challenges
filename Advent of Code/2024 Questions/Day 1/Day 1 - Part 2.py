"""
--- Part Two ---
Your analysis only confirmed what everyone feared: the two lists of location IDs are indeed very different.

Or are they?

The Historians can't agree on which group made the mistakes or how to read most of the Chief's handwriting, but in the commotion you notice an interesting detail: a lot of location IDs appear in both lists! Maybe the other numbers aren't location IDs at all but rather misinterpreted handwriting.

This time, you'll need to figure out exactly how often each number from the left list appears in the right list. Calculate a total similarity score by adding up each number in the left list after multiplying it by the number of times that number appears in the right list.

Here are the same example lists again:

3   4
4   3
2   5
1   3
3   9
3   3
For these example lists, here is the process of finding the similarity score:

The first number in the left list is 3. It appears in the right list three times, so the similarity score increases by 3 * 3 = 9.
The second number in the left list is 4. It appears in the right list once, so the similarity score increases by 4 * 1 = 4.
The third number in the left list is 2. It does not appear in the right list, so the similarity score does not increase (2 * 0 = 0).
The fourth number, 1, also does not appear in the right list.
The fifth number, 3, appears in the right list three times; the similarity score increases by 9.
The last number, 3, appears in the right list three times; the similarity score again increases by 9.
So, for these example lists, the similarity score at the end of this process is 31 (9 + 4 + 0 + 0 + 9 + 9).

Once again consider your left and right lists. What is their similarity score?
"""
import pandas as pd

# Accessing and reading file
data_file_path = "Advent of Code/2024 Questions/Day 1/data.xlsx"

data = pd.read_excel(data_file_path, header=None) # Making header none so that it doesnt skip the first entry
print(data.head())

# Convert columns to Python lists
left = data.iloc[:, 0].tolist()  # First column
right = data.iloc[:, 1].tolist()  # Second column

# Print the lists
#print("Array 1:", array1)
#print("Array 2:", array2)

# Now, need to arrange from smallest to largest: # Am cheating by using in build function, maybe in the future I will do it with an algorithm
left_sorted = sorted(left)
right_sorted = sorted(right)
#print("Left sorted:", left_sorted)
#print("Right sorted:", right_sorted)

# Finding all matches in numbers. If there is one, add one to found, and save it

found = [0] * len(left_sorted)
for i in range(len(left_sorted)):
    for j in range(len(left_sorted)):
        if left_sorted[i] == right_sorted[j]:
            found[i] += 1

print(found)

#Now, using all the found values, we multiply it by the number in the left column.

similarity_score = 0
for i in range(len(left_sorted)):
    similarity_score += left_sorted[i] * found[i]

print("The Similarity Score:", similarity_score)

# Completed!!!