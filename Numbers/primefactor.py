from __future__ import print_function

__author__ = 'sun.haixuan'


def primefactor(num):
    assert num > 0
    results = []
    div = 2
    while num >= div:
        if num % div == 0:
            results.append(div)
            num /= div
        else:
            div += 1
    print(','.join(map(str, results)))


def main():
    primefactor(int(raw_input("Input a positive number:")))

if __name__ == '__main__':
    main()
