import pandas as pd
from tabulate import tabulate

class ExtractsManager:
    # class static variables (shared among all instances)
    _CONCEPT_COL = "Concepto"
    _AMOUNT_COL = "Importe"

    def __init__(self, db_path=None, delimiter_char=None):
        # initialize saved_concepts database
        delimiter = self._DEFAULT_DELIMITER if delimiter_char == None else delimiter_char
        self._known_extracts = self.load_extract(db_path, delimiter_char)
        return None
    
    @staticmethod
    def load_extract(file_path:str, delim:str):
        # Load concepts saved as .csv in a pd.Dataframe
        full_extract = pd.read_csv(file_path, delimiter=delim)
        # Return only the columns that we need and remove the others
        simple_extract = full_extract[[ExtractsManager._CONCEPT_COL, ExtractsManager._AMOUNT_COL]]
        return simple_extract

    def print_extracts(self):
        print("\n",tabulate(self._known_extracts, headers='keys', tablefmt='psql'),sep="")
        return None