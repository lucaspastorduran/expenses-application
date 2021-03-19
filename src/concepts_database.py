from datetime import date
from tabulate import tabulate
import pandas as pd

class ConceptElement:
    _AVAILABLE_FIELDS = ["Concept Name", "Alias", "Category"]

    def __init__(self, name="", alias="", category=""):
        self._name = name
        self._alias = alias
        self._category = category

    def __str__(self):
        message = f"Concept:\nName: {self._name}. Alias: {self._alias}. Category: {self._category}"
        return message

class ConceptsDatabase:

    def __init__(self):
        self._creation_date = date.today()

    def load_concepts(self, file_path, delimiter):
        # Load concepts saved as .csv in a pd.Dataframe
        self._saved_concepts = pd.read_csv(file_path, delimiter=delimiter)

    def __str__(self):
        message = f"""
        Creation date: {self._creation_date}
        {self._saved_concepts.to_string()}
        """
        return message
    
    def print_db(self):
        print("\n",tabulate(self._saved_concepts, headers='keys', tablefmt='psql'),sep="")
        return None