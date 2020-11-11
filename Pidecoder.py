# name: Pidecoder.py

# Dividing the 26 alphabet into 256 -> R
a1 = int(256 / 26)
d1 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w",
      "x", "y", "z"]

# Creating dictionary for a~z
D1 = {}
count = 0
for e in range(0, 234, 9):
    D = {d1[count]: e}
    count += 1
    D1.update(D)

# Dividing the 26 capital alphabet into 256 -> G
d2 = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W",
      "X", "Y", "Z"]
count2 = 0
D2 = {}
for e in range(0, 234, 9):
    D = {d2[count2]: e}
    count2 += 1
    D2.update(D)

# Diving the 10 numbers into 256 -> B
d3 = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
count3 = 0
D3 = {}
for e in range(0, 250, 25):
    D = {d3[count3]: e}
    count3 += 1
    D3.update(D)


# function to return key from the value
def get_key(val, dic):
    for key, value in dic.items():
        if val == value:
            return key


# Use it to decode the pixel(RGB values) to the string


def decoder(w):
    r = "-"
    while True:
        for j in D1.values():
            if w[0] == j:
                r = get_key(w[0], D1)
                return r
        for h in D2.values():
            if w[1] == h:
                r = get_key(w[1], D2)
                return r
        for k in D3.values():
            if w[2] == k:
                r = get_key(w[2], D3)
                return r
        return r

