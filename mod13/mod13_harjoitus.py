with open("save.txt", "w") as tiedosto:
    tiedosto.write("taso:3")

with open("save.txt", "r") as tiedosto:
    data = tiedosto.read()
    print(data)