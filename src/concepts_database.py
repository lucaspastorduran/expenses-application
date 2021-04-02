from datetime import date
from tabulate import tabulate
import pandas as pd

class ConceptElement:
    # class static variables (shared among all instances)
    _NAME_FIELD = "Concept Name"
    _ALIAS_FIELD = "Alias"
    _CATEGORY_FIELD = "Category"

    def __init__(self, name, alias="", category=""):
        # class instance attributes
        self._name = name
        self._alias = alias
        self._category = category

    def is_in_database(self, saved_concepts_df):
        # Check if already there is a row with same "Concept Name"
        return self._name in saved_concepts_df[self._NAME_FIELD]

    def convert_to_dict(self):
        return {self._NAME_FIELD : self._name; _ALIAS_FIELD : self._alias; self._CATEGORY_FIELD : self._category}

    def __str__(self):
        message = f"Concept:\nName: {self._name}. Alias: {self._alias}. Category: {self._category}"
        return message

class ConceptsDatabase:
    # class static variables (shared among all instances)
    _DEFAULT_DATABASE_PATH = "/home/lucas/Documents/Cursos/expenses-application/src/saved_concepts.csv"
    _DEFAULT_DELIMITER = ";"
    _CONCEPT_FIELDS = {"name":ConceptElement._NAME_FIELD ;"alias":ConceptElement._ALIAS_FIELD; "category":ConceptElement._CATEGORY_FIELD}

    def __init__(self):
        # class instance attributes
        self._creation_date = date.today()
        self._saved_concepts = pd.read_csv(self._DEFAULT_DATABASE_PATH, delimiter=self._DEFAULT_DELIMITER)

    def load_concepts(self, file_path, delimiter):
        # Load concepts saved as .csv in a pd.Dataframe
        self._saved_concepts = pd.read_csv(file_path, delimiter=delimiter)

    def add_concept(self, concept_element):
        # Check if concept already exists
        if not concept_element.is_in_database(self._saved_concepts):
            # Add concept if is not already
            concept_dict = concept_element.convert_to_dict()
            self._saved_concepts.append(concept_dict)

    def __str__(self):
        message = f"""
        Creation date: {self._creation_date}
        {self._saved_concepts.to_string()}
        """
        return message
    
    def print_db(self):
        print("\n",tabulate(self._saved_concepts, headers='keys', tablefmt='psql'),sep="")
        return None