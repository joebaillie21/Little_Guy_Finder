from quiz import take_quiz
from little_guy_finder import *


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


def search_by_trait():

    traits = get_traits()
    for t in traits:
        print(t)
    search = input(
        'Please enter a trait from our list you would like to search by: ')

    search = '%s' % search
    to_print = get_lil_guys_by_prim_trait(search), get_lil_guys_by_secondary_trait(
        search), get_lil_guys_by_tertiary_trait(search)
    if to_print == ('', '', ''):
        print('There are no little guys with that given trait')
    else:
        for x in to_print:
            print(x)
    check_done()


def check_done():
    again = input('Would you like to search again? (y/n): ')
    again = again.lower()
    match again:
        case 'y':
            search_by_trait()
        case 'n':
            print('Thank you for using our services!')
        case _:
            print('Invalid response.')
            check_done()


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
            print_lil_guy(get_lil_guy_by_name(take_quiz()))
        case '2':
            print("Lil guys can come in a variety of forms with a variety of personality traits. We have curated a list of common traits")
            print("and ranked our database of lil guys based on how strongly they show given traits. Please refer to the list of traits below and enter")
            print("The trait you would like to search by.")
            search_by_trait()
        case '3':
            exit()


if __name__ == "__main__":
    main()
