# to import a file in oher folder, do this procedure
import sys
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, '/home/lucas/Documents/Cursos/expenses-application/src')

import expenses_app   # The code to test
import unittest   # The test framework

import pathlib
pathlib.Path(__file__).parent.absolute()

class Test_ExpensesApp(unittest.TestCase):
    _tests_path = str(pathlib.Path(__file__).parent.absolute())

    def test_1_initialize_app(self):
        file_name = self._tests_path + "/simple_file_1.csv"
        my_app = expenses_app.ExpensesApp(file_name, ";")
        my_app.print_app()
        self.assertTrue(True, "Concepts loaded succesfully")

if __name__ == '__main__':
    unittest.main()

