# to import a file in oher folder, do this procedure
import sys
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, '/home/lucas/Documents/Cursos/expenses-application/src')

import concepts_database   # The code to test
import unittest   # The test framework

import pathlib
pathlib.Path(__file__).parent.absolute()

class Test_ConceptsDatabase(unittest.TestCase):
    _TESTS_PATH = str(pathlib.Path(__file__).parent.absolute())

    def test_1_load_default_database(self):
        # define a db of concepts: will load default database in src code
        my_concepts_db = concepts_database.ConceptsDatabase()
        # print database
        my_concepts_db.print_db()
        self.assertTrue(True)

    def test_2_load_custom_database(self):
        # define a db of concepts
        my_concepts_db = concepts_database.ConceptsDatabase()
        # load a testing one
        file_name = self._TESTS_PATH + "/simple_file_1.csv"
        my_concepts_db.load_concepts(file_name, ";")
        my_concepts_db.print_db()
        self.assertTrue(True)

    def test_3_create_simple_concept(self):
        my_concept = concepts_database.ConceptElement("Bismillah kebabish")
        print(my_concept)
        self.assertTrue(True)

    def test_4_create_complete_concept(self):
        my_concept = concepts_database.ConceptElement("00801", "Bismillah", "Restaurante")
        print(my_concept)
        self.assertTrue(True)

    def test_5_add_new_concept(self):
        # define a db of concepts
        file_name = self._TESTS_PATH + "/simple_file_1.csv"
        delimiter = ";"
        my_concepts_db = concepts_database.ConceptsDatabase(file_name, delimiter)
        my_concepts_db.print_db()
        # add new concept
        new_concept = concepts_database.ConceptElement("2019293", "Pizza sports bar", "Restaurante")
        my_concepts_db.add_concept(new_concept)
        my_concepts_db.print_db()
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()

