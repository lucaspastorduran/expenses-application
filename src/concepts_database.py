from datetime import date
from tabulate import tabulate
import pandas as pd

class ConceptElement:
    # class static variables (shared among all instances)
    _AVAILABLE_FIELDS = ["Concept Name", "Alias", "Category"]

    def __init__(self, name, alias="", category=""):
        # class instance attributes
        self._name = name
        self._alias = alias
        self._category = category

    def __str__(self):
        message = f"Concept:\nName: {self._name}. Alias: {self._alias}. Category: {self._category}"
        return message

class ConceptsDatabase:
    # class static variables (shared among all instances)
    _DEFAULT_DATABASE_PATH = "/home/lucas/Documents/Cursos/expenses-application/src/saved_concepts.csv"
    _DEFAULT_DELIMITER = ";"
    _CONCEPT_FIELDS

    def __init__(self):
        # class instance attributes
        self._creation_date = date.today()
        self._saved_concepts = pd.read_csv(self._DEFAULT_DATABASE_PATH, delimiter=self._DEFAULT_DELIMITER)

    def load_concepts(self, file_path, delimiter):
        # Load concepts saved as .csv in a pd.Dataframe
        self._saved_concepts = pd.read_csv(file_path, delimiter=delimiter)

    def add_concept(self, concept_element):
        # Check if concept already exists
        # Add concept if is not already
        return None

    def __str__(self):
        message = f"""
        Creation date: {self._creation_date}
        {self._saved_concepts.to_string()}
        """
        return message
    
    def print_db(self):
        print("\n",tabulate(self._saved_concepts, headers='keys', tablefmt='psql'),sep="")
        return None