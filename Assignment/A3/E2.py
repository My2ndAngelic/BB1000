def main():
    with open('composers.txt') as f:
        return '\n'.join([line.rstrip('\n') for line in f.readlines()])


if __name__ == '__main__':
    _ = '''\
dufay
ockeghem
josquin
'''
    print(_)
    print(main() == _)
