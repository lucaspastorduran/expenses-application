# to import a file in oher folder, do this procedure
import sys
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, '/home/lucas/Documents/Cursos/expenses-application/src')

from extracts_manager import ExtractsManager    # The code to test
import unittest   # The test framework

import pathlib
pathlib.Path(__file__).parent.absolute()

class Test_ExtractsManager(unittest.TestCase):
    _TESTS_PATH = str(pathlib.Path(__file__).parent.absolute())

    def test_1_load_custom_extract(self):
        # load a testing exrtact
        file_name = self._TESTS_PATH + "/abanca_extracto.csv"
        my_extracts = ExtractsManager(db_path=file_name, delimiter_char=";")
        my_extracts.print_extracts()
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()