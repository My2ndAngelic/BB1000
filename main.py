def caesar_shift(text, n):
    """
    Returns an encrypted string by shifting input characters by n
    """
    # YOUR CODE HERE
    return ''.join(list(map(lambda x: chr(x), list(
        map(lambda x: (ord(x) - 65 + n) % 26 + 65 if 65 <= ord(x) <= 96 else (ord(x) - 97 + n) % 26 + 97,
            [text[x:x + 1] for x in range(0, len(text), 1)])))))
    # return list(map(lambda x : (ord(x) + n) % 26, text.split()))
    ################


def mysum(sequence):
    # from functools import reduce
    # return reduce(lambda x, y: x + y, sequence)
    return sequence[0] if len(sequence) == 1 else sequence[0] + mysum(sequence[1::])


if __name__ == '__main__':
    print(caesar_shift('ABBA', 2))
    print(caesar_shift('abba', 2))
    print(mysum([1, 3, 5, 7]))
