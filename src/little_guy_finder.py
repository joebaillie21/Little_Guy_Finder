from util import *


def build_db():
    """Create the tables to initialize the db"""
    exec_sql_file('src/schema.sql')
    exec_sql_file('src/initial_data.sql')


def get_traits():
    traits = exec_get_all("""
    SELECT trait FROM traits
    """, args={})
    if (traits == []):
        return "No traits accessible at this time."
    data = []
    for t in traits:
        data.append(t[0])
    return data


def get_lil_guys():
    lil_guys = exec_get_all("""
    SELECT name, info, friend_shaped, primary_trait, secondary_trait, tertiary_trait FROM Little_Guys
    """, args={})
    if (lil_guys == []):
        return "No lil guys accessible at this time."
    return lil_guys


def get_lil_guys_by_prim_trait(trait):
    lil_guys = exec_get_all("""
    SELECT name, info, friend_shaped, primary_trait, secondary_trait, tertiary_trait
    FROM Little_Guys
    INNER JOIN traits ON Little_Guys.primary_trait = traits.id
    WHERE traits.trait = %(trait)s
    """, args={"trait": trait})
    return lil_guys


def get_lil_guys_by_secondary_trait(trait):
    lil_guys = exec_get_all("""
    SELECT name, info, friend_shaped, primary_trait, secondary_trait, tertiary_trait
    FROM Little_Guys
    INNER JOIN traits ON Little_Guys.secondary_trait = traits.id
    WHERE traits.trait = %(trait)s
    """, args={"trait": trait})
    return lil_guys


def get_lil_guys_by_tertiary_trait(trait):
    lil_guys = exec_get_all("""
    SELECT name, info, friend_shaped, primary_trait, secondary_trait, tertiary_trait
    FROM Little_Guys
    INNER JOIN traits ON Little_Guys.tertiary_trait = traits.id
    WHERE traits.trait = %(trait)s
    """, args={"trait": trait})
    return lil_guys


def get_trait_by_id(id):
    trait = exec_get_one("""
    SELECT trait FROM Traits
    WHERE id = %(id)s""", args={"id": id})
    if trait != None:
        return trait[0]
    return None


def get_lil_guy_by_name(name):
    guy = exec_get_one("""
    SELECT name, info, friend_shaped, primary_trait, secondary_trait, tertiary_trait
    FROM Little_Guys
    WHERE name = %(name)s
    """,  args={"name": name})
    data = [guy[0], guy[1], guy[2]]
    data.append(get_trait_by_id(guy[3]))
    data.append(get_trait_by_id(guy[4]))
    data.append(get_trait_by_id(guy[5]))
    return data
