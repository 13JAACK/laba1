import random
from dopolnenie1 import multiply
def add(a, b):
    return a + b
def main():
    a = random.randint(1, 100)
    b = random.randint(1, 100)

    print(f"случайное число A = {a}")
    print(f"случайное число B = {b}")
    print(f"сумма A + B = {add(a, b)}")
    print(f"произведение A * B = {multiply(a, b)}")


if __name__ == "__main__":
    main()