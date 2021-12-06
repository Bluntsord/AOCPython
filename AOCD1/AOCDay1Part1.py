import functools
import io

# Processing line by line
f = io.open("Data.txt", "r")
data = f.readlines()

count = 0

two_Line_Previous = 0
previousLine = 0

previousSum = 0
for line in data:
    currentLine = int(line)

    currentSum = currentLine + previousLine + two_Line_Previous
    if currentSum > previousSum:
        count += 1
    two_Line_Previous = previousLine
    previousLine = currentLine
    previousSum = currentSum

print(count - 3)

