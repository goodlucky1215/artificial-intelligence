import hashlib

with open("min.jpg","rb") as file:
    string = (file.read())
    m = hashlib.md5()
    m.update(string)
    result = m.digest()
    print(result)

