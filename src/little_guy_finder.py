from src.util import *


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
    return traits


def get_lil_guys():
    lil_guys = exec_get_all("""
    SELECT name FROM Little_Guys
    """, args={})
    if (lil_guys == []):
        return "No traits accessible at this time."
    return lil_guys


def get_lil_guys_by_prim_trait(trait_id):
    lil_guys = exec_get_all("""
    SELECT name
    FROM Little_Guys
    INNER JOIN traits ON Little_Guys.primary_trait = traits.id
    WHERE Little_Guys.primary_trait = %(trait_id)s
    """, args={"trait_id": trait_id})
    return lil_guys


def get_lil_guys_by_secondary_trait(trait_id):
    lil_guys = exec_get_all("""
    SELECT name
    FROM Little_Guys
    INNER JOIN traits ON Little_Guys.primary_trait = traits.id
    WHERE Little_Guys.secondary_trait = %(trait_id)s
    """, args={"trait_id": trait_id})
    return lil_guys


def get_lil_guys_by_tertiary_trait(trait_id):
    lil_guys = exec_get_all("""
    SELECT name
    FROM Little_Guys
    INNER JOIN traits ON Little_Guys.primary_trait = traits.id
    WHERE Little_Guys.tertiary_trait = %(trait_id)s
    """, args={"trait_id": trait_id})
    return lil_guys
