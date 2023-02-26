from src.quiz import take_quiz


def print_file(filename):
    f = open(filename)
    read_file = f.read()
    print(read_file)
    f.close()


def main():
    print_file('data/name.txt')
    print_file('data/emotional_support.txt')

    bad_val = True
    response = None
    print('Welcome to Lil Guy finder. Please choose an option:')
    print('1. Take the quiz')
    print('2. Search for a lil guy')
    print('3. Exit')
    while (bad_val):
        response = input()
        if (response != '1' and response != '2' and response != '3'):
            print('Please input one of the given values.')
        else:
            bad_val = False

    match response:
        case '1':
            take_quiz()
        case '2':
            """ search() """
        case '3':
            exit()


if __name__ == "__main__":
    main()
