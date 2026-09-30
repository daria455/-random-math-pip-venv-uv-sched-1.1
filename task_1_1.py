import sys

print("Версия Piton:", sys.version.split()[0])
print("Интерпритатор:", sys.executable)

print("Количество путей поиска:", len(sys.path))
for p in sys.path[:4]:
    print("  ", p)

import math, random

print("math.pi=", math.pi)
print("random.random() =", random.random())

mods = sorted(sys.modules)
print("всего загружено модулей:", len(mods))
print("Пример:", mods[:5])

public = [n for n in dir(math) if not n.startswith('__')]
print("Публичных иммён в math:", len(public))
print("Первые 8:", public[:8])

print("Мой __name__=", __name__)
print("Мой __file__=", __file__)