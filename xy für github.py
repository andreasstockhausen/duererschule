"""Matheaufgaben, Umstellungen,
unendlich viele Aufgaben,
die immer schwerer werden"""

import random
import time

class Mat():

    def __init__(self, y, z):
        self.y = y
        self.z = z

    y = 1.0
    z = 2.0

    while True:
        # x am Ende
        a = random.uniform(1.0, y)
        b = random.uniform(1.0, y)
        a = int(a)
        b = int(b)
        c = b + a
        print(a, "+ x =", c)
        time.sleep(6)
        print("x =", b)
        print()
        time.sleep(2)

        a = random.uniform(1.0, y)
        b = random.uniform(1.0, y)
        a = int(a)
        b = int(b)
        c = a + b
        print(c, "− x =", b)
        time.sleep(6)
        print("x =", a)
        print()
        time.sleep(2)

        a = random.uniform(1.0, z)
        b = random.uniform(1.0, z)
        a = int(a)
        b = int(b)
        c = a * b
        print(a, "· x =", c)
        time.sleep(6)
        print("x =", b)
        print()
        time.sleep(2)

        a = random.uniform(1.0, z)
        b = random.uniform(1.0, z)
        a = int(a)
        b = int(b)
        a = c * b
        print(a, ": x =", c)
        time.sleep(6)
        print("x =", b)
        print()
        time.sleep(2)

        # x am Anfang
        a = random.uniform(1.0, y)
        b = random.uniform(1.0, y)
        a = int(a)
        b = int(b)
        c = a + b
        print("x +", a, "=", c)
        time.sleep(6)
        print("x =", b)
        print()
        time.sleep(2)

        a = random.uniform(1.0, y)
        b = random.uniform(1.0, y)
        a = int(a)
        b = int(b)
        c = a + b
        print("x -", a, "=", b)
        time.sleep(6)
        print("x =", c)
        print()
        time.sleep(2)

        a = random.uniform(1.0, z)
        b = random.uniform(1.0, z)
        a = int(a)
        b = int(b)
        c = a * b
        print("x ·", b, "=", c)
        time.sleep(6)
        print("x =", a)
        print()
        time.sleep(2)

        a = random.uniform(1.0, z)
        b = random.uniform(1.0, z)
        a = int(a)
        b = int(b)
        a = c * b
        print("x :", c, "=", b)
        time.sleep(6)
        print("x =", a)
        print()
        time.sleep(2)

        y = y + 0.9
        z = z + 0.2

mat = Mat
