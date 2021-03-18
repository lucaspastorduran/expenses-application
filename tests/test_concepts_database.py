# to import a file in oher folder, do this procedure
import sys
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, '/home/lucas/Documents/Cursos/expenses-application/src')

import concepts_database   # The code to test
import unittest   # The test framework

import pathlib
pathlib.Path(__file__).parent.absolute()

class Test_ConceptsDatabase(unittest.TestCase):
    _tests_path = str(pathlib.Path(__file__).parent.absolute())

    def test_1_load_database(self):
        # define a db of concepts
        my_concepts_db = concepts_database.ConceptsDatabase()

        # load a testing one
        file_name = self._tests_path + "/simple_file_1.csv"
        my_concepts_db.load_concepts(file_name, ";")
        my_concepts_db.print_db()
        self.assertTrue(True, "Concepts loaded succesfully")


if __name__ == '__main__':
    unittest.main()

