from datetime import date
from tabulate import tabulate
import pandas as pd

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
        print(tabulate(self._saved_concepts, headers='keys', tablefmt='psql'))
        return None