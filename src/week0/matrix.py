def matrix():
    x = y.array([[1, 2, 3], [3, 4, 5], [7, 8, 9]])
    for line in x:
        print('  '.join(map(str, line)))

def test():
    matrix()

if __name__ == "__main__":
    matrix()
