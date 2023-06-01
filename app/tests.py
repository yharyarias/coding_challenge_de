import unittest
import pandas as pd
import utils.df_utils as utils

def convertToDataFrame(columns, lst):
    df = pd.DataFrame(lst, columns=columns)
    return df

class TestConvertToDataFrame(unittest.TestCase):
    def test_convertToDataFrame(self):
        # Test case 1: empty columns and list
        columns = []
        lst = []
        result = utils.convertToDataFrame(columns, lst)
        self.assertIsInstance(result, pd.DataFrame)
        self.assertEqual(len(result), 0)

        # Test case 2: columns and list with values
        columns = ['A', 'B', 'C']
        lst = [[1, 'Hello', True], [2, 'World', False]]
        result = utils.convertToDataFrame(columns, lst)
        self.assertIsInstance(result, pd.DataFrame)
        self.assertEqual(len(result), 2)
        self.assertEqual(list(result.columns), columns)
        self.assertEqual(result.iloc[0].tolist(), [1, 'Hello', True])
        self.assertEqual(result.iloc[1].tolist(), [2, 'World', False])

if __name__ == '__main__':
    unittest.main()