if __name__ == '__main__':
    f1 = open('result.txt', 'r')
    f2 = open('result2.txt', 'r')

    a = f1.read().split(', ')
    b = f2.read().split(', ')

    candidates = list(set(a) & set(b))
    print(candidates)

    f = open('candidates.txt', 'w')
    f.write(', '.join(candidates))
    f.close()
