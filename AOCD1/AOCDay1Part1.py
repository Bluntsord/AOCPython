import functools
import io
import Reader

data = Reader.read()
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

