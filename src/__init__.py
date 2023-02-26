from quiz import take_quiz
import little_guy_finder


def print_file(filename):
    f = open(filename)
    read_file = f.read()
    print(read_file)
    f.close()


def quiz_or_search():
    print('Welcome to Lil Guy finder.')
    print('1. Take the quiz')
    print('2. Search for a lil guy')
    print('3. Exit')
    response = input('Please enter \'1\', \'2\', or \'3\': ')
    match response:
        case '1':
            return response
        case '2':
            return response
        case '3':
            return response
        case _:
            return quiz_or_search()


def print_lil_guy(lil_guy):
    print('Name:', lil_guy[0])
    print('Description:', lil_guy[1])
    if (lil_guy[2]):
        print('Friend Shaped.')
    print('Traits:')
    for x in range(3, len(lil_guy)):
        if lil_guy[x] != None:
            print('\t' + lil_guy[x])


def main():
    print_file('data/name.txt')
    print()
    print_file('data/emotional_support.txt')
    print()

    match quiz_or_search():
        case '1':
            print()
            print_lil_guy(little_guy_finder.get_lil_guy_by_name(take_quiz()))
        case '2':
            """ search() """
        case '3':
            exit()


if __name__ == "__main__":
    main()
