from concepts_database import ConceptsDatabase, ConceptElement

class ExpensesApp:

    def __init__ (self, db_path:str, db_delimiter:str):
        my_concepts = ConceptsDatabase(db_path, db_delimiter)
        self._concepts_database = my_concepts

    def __str__(self):
        message = f"""
        Expenses Application (by Lucas Pastor)
        {self._concepts_database}
        """
        return message
    
    def print_app(self):
        self._concepts_database.print_db()
        return None