def is_friend_shaped():
    response = input(
        'Do you want a friend-shaped lil guy? Enter \'yes\' or \'no\': ')

    match response.lower():
        case 'yes':
            return True
        case 'no':
            return False
        case _:
            return is_friend_shaped()


def is_inanimate():
    response = input(
        'Do you want an inanimate lil guy? Enter \'yes\' or \'no\': ')

    match response.lower():
        case 'yes':
            return True
        case 'no':
            return False
        case _:
            return is_inanimate()


def is_common():
    response = input(
        'Do you want a more traditional lil guy or something a little more uncommon? Enter \'traditional\' or \'uncommon\': ')

    match response.lower():
        case 'traditional':
            return True
        case 'uncommon':
            return False
        case _:
            return is_common()


def is_introverted():
    response = input(
        'Do you want an introverted or extroverted lil guy? Enter \'introverted\' or \'extroverted\': ')

    match response.lower():
        case 'introverted':
            return True
        case 'extroverted':
            return False
        case _:
            return is_introverted()


def is_high_maintainence():
    response = input(
        'Do you mind a lil guy that is more high maintainence or do you want a low maintainence lil guy? Enter \'high\' or \'low\': ')

    match response.lower():
        case 'high':
            return True
        case 'low':
            return False
        case _:
            return is_high_maintainence()


def size():
    print('Lil guys don\'t necessarily have to be little.')
    response = input(
        'What size of lil guy would you like? Enter \'small\', \'medium\', or \'large\': ')

    match response.lower():
        case 'small':
            return response.lower()
        case 'medium':
            return response.lower()
        case 'large':
            return response.lower()
        case _:
            return is_inanimate()


def take_quiz():
    lil_guy = None
    match is_friend_shaped():
        case True:
            match size():
                case 'small':
                    match is_high_maintainence():
                        case True:
                            # Hamster
                            lil_guy = 'Hamster'
                        case False:
                            # Bird
                            lil_guy = 'Bird'
                case 'medium':
                    match is_common():
                        case True:
                            # Puppy
                            lil_guy = 'Puppy'
                        case False:
                            # Raccoon
                            lil_guy = 'Raccoon'
                case 'Large':
                    # Bear
                    lil_guy = 'Bear'
        case False:
            match is_inanimate():
                case True:
                    match is_common():
                        case True:
                            # Kitten
                            lil_guy = 'Kitten'
                        case False:
                            match is_introverted():
                                case True:
                                    # Snake
                                    lil_guy = 'Snake'
                                case False:
                                    # Rat
                                    lil_guy = 'Rat'
                case False:
                    match is_high_maintainence():
                        case True:
                            # Brick
                            lil_guy = 'Brick'
                        case False:
                            # Plant
                            lil_guy = 'Plant'
    return lil_guy
