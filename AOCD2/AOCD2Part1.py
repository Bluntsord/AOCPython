import Vector
import Reader
import typing

data = Reader.read("Data.txt")
answer = Vector.Vector(0,0)

def parse(input: str):
    temp = input.split(" ")
    keyword = temp[0]
    value = int(temp[1])

    if keyword == "forward":
        return lambda x: x.addX(value)
    elif keyword == "down":
        return lambda x: x.addY(value)
    elif keyword == "up":
        return lambda x: x.addY(value * -1)

for line in data:
    func = parse(line)
    func(answer)

print(answer)
print(answer.x * answer.y)



