from enum import Enum
from tabulate import tabulate
import pandas as pd

from concepts_database import ConceptsDatabase

def read_file(file_name, delimiter):
    df = pd.read_csv(file_name, delimiter=delimiter)
    return df

def print_df(df):
    print(tabulate(df, headers='keys', tablefmt='psql'))
    return None

class ExpensesApp:
    _DATABASE_NAME = "conceptsDatabase.csv"

    def __init__ (self):
        self._concepts_database = ConceptsDatabase()

    def __str__(self):
        message = f"""
        Expenses Application (by Lucas Pastor)
        {self._concepts_database}
        """
        return message