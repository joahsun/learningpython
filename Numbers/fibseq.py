from __future__ import print_function

__author__ = 'sun.haixuan'


def gen_fibo(num):
    assert (num >= 0)
    seq = [0, 1]
    for n in range(2, num):
        seq.append(seq[n-2] + seq[n-1])
    print(','.join(map(str, seq[:num])))


def main():
    gen_fibo(int(raw_input("How many numbers:")))


if __name__ == '__main__':
    main()
