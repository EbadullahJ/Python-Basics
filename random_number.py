import random

N_NUMBERS: int = 10
MIN_VALUE: int = 1
MAX_VALUE: int = 100

def main():
    for num in range(N_NUMBERS):  # print 10 random num b/w min & max value
        value = random.randint(MIN_VALUE, MAX_VALUE)
        print(value, end= " ")


if __name__ == '__main__':
    main()
