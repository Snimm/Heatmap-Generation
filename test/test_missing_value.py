import unittest
#import process_data
import numpy as np
import os
import sys
dirname = os.path.dirname(__file__)
path_to_folder = dirname[:-5]
print(f"path: {path_to_folder}")
sys.path.append(path_to_folder)

import process_data



class TestProcessData(unittest.TestCase):


    def test_handle_missing_values(self):
        mock_thermal_data = np.array([[1.0, 2.0, np.nan, 4.0],
                                      [5.0, np.nan, 7.0, 8.0],
                                      [9.0, 10.0, 11 , np.nan]])
        interpolated_data = process_data.handle_missing_values(mock_thermal_data)
        expected_data = np.array([[1.0, 2.0, 3.0, 4.0],
                                  [5.0, 6.0, 7.0, 8.0],
                                  [9.0, 10.0, 11.0, 12.0]])
        np.testing.assert_array_equal(interpolated_data, expected_data)

if __name__ == '__main__':
    unittest.main()