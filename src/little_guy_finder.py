from src.util import *


def build_db():
    """Create the tables to initialize the db"""
    exec_sql_file('src/schema.sql')
