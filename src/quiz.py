def is_friend_shaped():
    response = input(
        'Do you want a friend-shaped lil guy? Enter \'yes\' or \'no\': ')

    match response:
        case 'yes':
            return True
        case 'no':
            return False
        case _:
            return is_friend_shaped()


def is_inanimate():
    response = input()


def take_quiz():
    print('LOL')
#     match is_friend_shaped():
#         # case True:

#         # case False:
