import random

# Definir el método que ejecute el exponencial modular.


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


# El número primo y la base
p: int = 761
g: int = 6

# random.randint(1, 10**100)

# Número aleatorio o x, el que se usará para pasar a binario.
randomIker: int = random.randint(1, 10**100)

# Clave parcial, o publica para compartir.
xIker: int = mod_exp(g, randomIker, p)
# Enviar al compañero
print(f"Envía el número X: {xIker} a tu compañero.")
# Recibir la clave del compañero
y: int = int(input("Ingrese el número Y que su compañero le ha enviado: "))

# Calcular la clave final para cifrar
kIker = mod_exp(y, randomIker, p)

print(f"La clave secreta compartida es: {kIker}")
