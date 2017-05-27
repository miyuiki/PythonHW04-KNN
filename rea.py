import re

pattern = r"[0-9]*"

f = open("buffer.txt")
st = f.readline()

data = re.search(pattern, st)

print(str(data.group(0)))