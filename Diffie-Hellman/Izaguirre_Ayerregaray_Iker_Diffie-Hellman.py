import random


def mod_exp(b: int, e: int, p: int) -> int:
    x: int
    power: int
    x = 1
    power = b % p

    while e:

        if (e & 1):
            x = (x * power) % p

        e >>= 1
        power = (power * power) % p

    return x


p: int = 761
g: int = 6

# random.randint(1, 10**100)
# randomIker: int = random.randint(1, 10**100)
# randomElena: int = random.randint(1, 10**100)

randomIker: int = 9979219203731601911928975844281701173308623973473067026329084015674262449505355025435932129284870203
randomElena: int = 7088383412973965963172339874534569047505976494686124697935777470950518994119586399903473171323486681

xIker: int = mod_exp(g, randomIker, p)
yElena: int = mod_exp(g, randomElena, p)

kIker = mod_exp(yElena, randomIker, p)
kElena = mod_exp(xIker, randomElena, p)
