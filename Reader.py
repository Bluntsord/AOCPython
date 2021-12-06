import io

def read():
    # Processing line by line
    f = io.open("Data.txt", "r")
    data = f.readlines()
    return data