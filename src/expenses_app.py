from concepts_database import ConceptsDatabase

class ExpensesApp:

    def __init__ (self, db_path, db_delimiter):
        my_concepts = ConceptsDatabase()
        my_concepts.load_concepts(db_path, db_delimiter)
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