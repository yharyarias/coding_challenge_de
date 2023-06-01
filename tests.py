import unittest
from app.data_type import DataType
import app.csv_manager as mgr
class TestCSVManager(unittest.TestCase):

    def test_readCsv(self):
        csv_manager = mgr.CSVManager()
        file_path = "/Users/yharyarias/Downloads/jobs.csv"
        expected_data_list = [(1, 'Marketing Assistant'), (2, 'VP Sale[5290 chars]IV')]
        
        self.assertEqual(self, csv_manager.readCsv(file_path, DataType.JOBS), expected_data_list)

if __name__ == '__main__':
    unittest.main()
