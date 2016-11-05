#-*- coding: utf-8 -*-

"""
@authors: Daniel Reyes, Ania Pietrzak, Alberto Miedes
"""

from db.create import db_setup
from db.queries import db_run_all_queries

def main():
    db_setup()
    db_run_all_queries()

main()
