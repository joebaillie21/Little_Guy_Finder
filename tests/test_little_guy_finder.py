import unittest
from src.little_guy_finder import *
from src.util import *


class test_LGF(unittest.TestCase):

    def test_build_db(self):
        # Setup
        build_db()
        expected = [
            [
                (1, 'Brick', 'Just a lil brick guy. A little basic and boring but has a strong foundation and here to support. Stationary so no worries about exploring outside the home. Very cost effective.', False, 11, 9, None),
                (2, 'Raccoon', 'Just a lil trash panda. Likes to wash their hands and food before they eat. Can be a lil bit angry and jittery but can calm down once they get settled and used to their environment.', True, 1, 7, None),
                (3, 'Snake', 'Just a lil nope rope or danger noodle. ', False, 3, 10, 1),
                (4, 'Kitten', 'In the early stages, they will be cute and cuddly. If you are lucky, they will stay that way.', False, 2, 9, 5),
                (5, 'Puppy', 'Some may call it the original service animal. This bundle of joy will become a buddy you will never forget over the years.', True, 4, 6, 9),
                (6, 'Plants', 'They may not be able to talk, but they will listen for hours.', False, 9, 11, 7),
                (7, 'Bear', 'Very large. You may only be able to hug it once. Is it worth it? That is up to you!', True, 1, 4, 5),
                (8, 'Bird', 'A flying birb that will meet all your avion need!',
                 True, 8, 6, 12),
                (9, 'Rat', 'Oh ****, a rat.', False, 8, 6, 13),
                (10, 'Hamster', 'Do not ask your friends what happened to theirs. Or do if you want a horror story.', True, 13, 10, 8)
            ],
            [
                (1, 'Fiesty'),
                (2, 'Sassy'),
                (3, 'Quiet'),
                (4, 'Adventurous'),
                (5, 'Grumpy'),
                (6, 'Excited'),
                (7, 'Tidy'),
                (8, 'Messy'),
                (9, 'Basic'),
                (10, 'Shy'),
                (11, 'Low maintenance'),
                (12, 'High maintenance'),
                (13, 'Friendly')
            ]
        ]

        # Invoke
        result = [
            exec_get_all("""SELECT * FROM Little_Guys""", args={}),
            exec_get_all("""SELECT * FROM Traits""", args={})
        ]

        # Analyze
        self.assertEqual(expected, result)

    def test_get_lil_guys(self):
        # Setup
        build_db()
        expected = [
            ('Brick', 'Just a lil brick guy. A little basic and boring but has a strong foundation and here to support. Stationary so no worries about exploring outside the home. Very cost effective.', False, 11, 9, None),
            ('Raccoon', 'Just a lil trash panda. Likes to wash their hands and food before they eat. Can be a lil bit angry and jittery but can calm down once they get settled and used to their environment.', True, 1, 7, None),
            ('Snake', 'Just a lil nope rope or danger noodle. ', False, 3, 10, 1),
            ('Kitten', 'In the early stages, they will be cute and cuddly. If you are lucky, they will stay that way.', False, 2, 9, 5),
            ('Puppy', 'Some may call it the original service animal. This bundle of joy will become a buddy you will never forget over the years.', True, 4, 6, 9),
            ('Plants', 'They may not be able to talk, but they will listen for hours.', False, 9, 11, 7),
            ('Bear', 'Very large. You may only be able to hug it once. Is it worth it? That is up to you!', True, 1, 4, 5),
            ('Bird', 'A flying birb that will meet all your avion need!', True, 8, 6, 12),
            ('Rat', 'Oh ****, a rat.', False, 8, 6, 13),
            ('Hamster', 'Do not ask your friends what happened to theirs. Or do if you want a horror story.', True, 13, 10, 8)
        ]

        # Invoke
        result = get_lil_guys()

        # Analyze
        self.assertEqual(expected, result)

    def test_get_traits(self):
        # Setup
        build_db()
        expected = [
            ('Fiesty'),
            ('Sassy'),
            ('Quiet'),
            ('Adventurous'),
            ('Grumpy'),
            ('Excited'),
            ('Tidy'),
            ('Messy'),
            ('Basic'),
            ('Shy'),
            ('Low maintenance'),
            ('High maintenance'),
            ('Friendly')
        ]

        # Invoke
        result = get_traits()

        # Analyze
        self.assertEqual(expected, result)

    def test_get_lg_by_prim_trait(self):
        # Setup
        build_db()
        trait = 'Fiesty'
        expected = [('Raccoon', 'Just a lil trash panda. Likes to wash their hands and food before they eat. Can be a lil bit angry and jittery but can calm down once they get settled and used to their environment.',
                     True, 1, 7, None), ('Bear', 'Very large. You may only be able to hug it once. Is it worth it? That is up to you!', True, 1, 4, 5)]

        # Invoke
        result = get_lil_guys_by_prim_trait(trait)

        # Analyze
        self.assertEqual(expected, result)

    def test_get_lg_by_secondary_trait(self):
        # Setup
        build_db()
        trait = 'Tidy'
        expected = [('Raccoon', 'Just a lil trash panda. Likes to wash their hands and food before they eat. Can be a lil bit angry and jittery but can calm down once they get settled and used to their environment.', True, 1, 7, None)]

        # Invoke
        result = get_lil_guys_by_secondary_trait(trait)

        # Analyze
        self.assertEqual(expected, result)

    def test_get_lg_by_tertiary_trait(self):
        # Setup
        build_db()
        trait = 'Tidy'
        expected = [
            ('Plants', 'They may not be able to talk, but they will listen for hours.', False, 9, 11, 7)]

        # Invoke
        result = get_lil_guys_by_tertiary_trait(trait)

        # Analyze
        self.assertEqual(expected, result)

    def test_get_trait_by_id(self):
        # Setup
        build_db()
        id = 1
        expected = 'Fiesty'

        # Invoke
        result = get_trait_by_id(id)

        # Analyze
        self.assertEqual(expected, result)

    def test_get_lg_by_name(self):
        # Setup
        build_db()
        name = 'Raccoon'
        expected = ['Raccoon', 'Just a lil trash panda. Likes to wash their hands and food before they eat. Can be a lil bit angry and jittery but can calm down once they get settled and used to their environment.',
                    True, 'Fiesty', 'Tidy', None]

        # Invoke
        result = get_lil_guy_by_name(name)

        # Analyze
        self.assertEqual(expected, result)
