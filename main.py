def caesar_shift(text, n):
    """
    Returns an encrypted string by shifting input characters by n
    """
    # YOUR CODE HERE
    return ''.join(list(map(lambda x: chr(x), list(
        map(lambda x: (ord(x) + n - ((1 << 6) + (1 << 0))) % ((1 << 4) + (1 << 3) + (1 << 1)) + (
                    (1 << 6) + (1 << 0)) if ((1 << 6) + (1 << 0)) <= ord(x) <= (
                    (1 << 6) + (1 << 4) + (1 << 3) + (1 << 1) + (1 << 0)) else (ord(x) + n - (
                    (1 << 6) + (1 << 5) + (1 << 0))) % ((1 << 4) + (1 << 3) + (1 << 1)) + ((1 << 6) + (1 << 5) + (
                    1 << 0)) if ((1 << 6) + (1 << 5) + (1 << 0)) <= ord(x) <= (
                    (1 << 6) + (1 << 5) + (1 << 4) + (1 << 3) + (1 << 1) + (1 << 0)) else ord(x),
            [text[x:x + (1 << 0)] for x in range(0, len(text))])))))
    # return list(map(lambda x : (ord(x) + n) % 26, text.split()))
    ################


def mysum(sequence):
    # from functools import reduce
    # return reduce(lambda x, y: x + y, sequence)
    # return sequence[0] if len(sequence) == 1 else sequence[0] + mysum(sequence[1::])
    return [j for j in [0] for i in sequence for j in [j + i]][-1]


def lesum(sequence):
    return [j for j in [0] for i in sequence for j in [j + i]][-1]


if __name__ == '__main__':
    print(caesar_shift('ABBA', 2))
    print(caesar_shift('abba', 2))
    print(mysum([1, 3, 5, 7]))
    print(lesum([6, 9, 4, 2, 1]))
