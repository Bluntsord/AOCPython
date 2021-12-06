import io

def read(filename):
    # Processing line by line
    f = io.open(filename, "r")
    data = f.readlines()
    return data