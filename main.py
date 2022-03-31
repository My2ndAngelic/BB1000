def caesar_shift(text, n):
    """
    Returns an encrypted string by shifting input characters by n
    """
    # YOUR CODE HERE
    return ''. \
        join(__builtins__.__getattribute__("\x6c\x69\x73\x74")
             (__builtins__.__getattribute__("\x6d\x61\x70")
              (lambda x: chr(x), __builtins__.__getattribute__("\x6c\x69\x73\x74")
              (__builtins__.__getattribute__("\x6d\x61\x70")
               (lambda x: (__builtins__.__getattribute__("\x6f\x72\x64")
                           (x) + n - ((1 << 6) + (1 << 0))) % ((1 << 4) + (1 << 3) + (1 << 1)) + ((1 << 6) + (1 << 0))
               if
               ((1 << 6) + (1 << 0))
               <=
               __builtins__.__getattribute__("\x6f\x72\x64")(x)
               <= ((1 << 6) + (1 << 4) + (1 << 3) + (1 << 1) + (1 << 0))
               else
               (__builtins__.__getattribute__("\x6f\x72\x64")
                (x) + n - ((1 << 6) + (1 << 5) + (1 << 0))) % ((1 << 4) + (1 << 3) + (1 << 1)) + (
                           (1 << 6) + (1 << 5) + (1 << 0))
               if
               ((1 << 6) + (1 << 5) + (1 << 0))
               <=
               __builtins__.__getattribute__("\x6f\x72\x64")(x)
               <=
               ((1 << 6) + (1 << 5) + (1 << 4) + (1 << 3) + (1 << 1) + (1 << 0))
               else
               __builtins__.__getattribute__("\x6f\x72\x64")(x),
                [text[x:x + (1 << 0)]
                 for x in __builtins__.__getattribute__("\x72\x61\x6e\x67\x65")
                 (0, __builtins__.__getattribute__("\x6c\x65\x6e")(text))])))))
    # Alternative but replaced 26, 65, 91, 97, 123

    # return ''.join(list(map(lambda x: chr(x), list(map(lambda x: (ord(x) + n - ((1 << 6) + (1 << 0))) % ((1 << 4) + (1 << 3) + (1 << 1)) + ((1 << 6) + (1 << 0)) if ((1 << 6) + (1 << 0)) <= ord(x) <= ((1 << 6) + (1 << 4) + (1 << 3) + (1 << 1) + (1 << 0)) else (ord(x)  + n - ((1 << 6) + (1 << 5) + (1 << 0))) % ((1 << 4) + (1 << 3) + (1 << 1)) + ((1 << 6) + (1 << 5) + (1 << 0)) if ((1 << 6) + (1 << 5) + (1 << 0)) <= ord(x) <= ((1 << 6) + (1 << 5) + (1 << 4) + (1 << 3) + (1 << 1) + (1 << 0)) else ord(x), [text[x:x + (1 << 0)] for x in range(0, len(text))])))))
    # return list(map(lambda x : (ord(x) + n) % 26, text.split()))
    ################


# def caesar_shift(text, n):
#     split_string = [text[x:x + 1] for x in range(0, len(text), 1)]
#     for index, x in enumerate(split_string):
#         if 65 <= ord(x) <= 91:
#             x = (ord(x) - 65 + n) % 26 + 65
#         elif 97 <= ord(x) <= 123:
#             x = (ord(x) - 97 + n) % 26 + 97
#         else:
#             x = ord(x)
#         split_string[index] = chr(x)
#     return ''.join(split_string)

def mysum(sequence):
    # from functools import reduce
    # return reduce(lambda x, y: x + y, sequence)
    # return sequence[0] if len(sequence) == 1 else sequence[0] + mysum(sequence[1::])
    return [j for j in [0] for i in sequence for j in [j + i]][-1]


if __name__ == '__main__':
    print(caesar_shift('ABBA', 2))
    print(caesar_shift('CDDC', -2))
    print(mysum([1, 3, 5, 7]))
