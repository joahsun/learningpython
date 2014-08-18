from __future__ import print_function

__author__ = 'sun.haixuan'


def gen_fibo(num):
    assert (num >= 0)
    a, b = 0, 1
    n = 0
    while 1:
        tmp = a + b
        a = b
        b = tmp
        n += 1
        if n == num:
            print(a)
            break
        print(a, end=',')


def main():
    gen_fibo(int(input("How many numbers:")))


if __name__ == '__main__':
    main()
