import pandas as pd 
import unittest
from pandas.testing import assert_frame_equal
from results import isn_max_total_cost, max_min_average

datapath = "D:/Project/NBPC_modify/data/"
NB = pd.read_csv(datapath+'NB.csv')
PC = pd.read_csv(datapath+'PC.csv')

# unittest
class TestResults(unittest.TestCase):

    def test_result_1(self):
        # actual result 1
        ans1_NB = isn_max_total_cost(NB)
        ans1_PC = isn_max_total_cost(PC)
        ans1 = pd.concat([ans1_NB, ans1_PC], ignore_index=True)
        # Define the result_1
        expected_ans1 = {'ISN': ['NB13', 'PC20']}
        expected_ans1_df = pd.DataFrame(expected_ans1)
        # Compare the actual result with the expected DataFrame
        assert_frame_equal(ans1, expected_ans1_df)

    def test_result_2(self):
        # actual result 2
        ans2_NB = max_min_average(NB,"Total Cost","NB")
        ans2_PC = max_min_average(PC,"Total Cost","PC")
        ans2 = ans2_NB.merge(ans2_PC, on='Total Cost')
        ans2["NB"] = ans2["NB"].astype(float)
        ans2["PC"] = ans2["PC"].astype(float)
        # Define the result_2
        expected_ans2 = {'Total Cost': ['Max', 'Min', 'Average'],
                            'NB': [11626.00, 8675.00, 9728.33],
                            'PC': [7862.00, 5854.00, 6858.00]}
        expected_ans2_df = pd.DataFrame(expected_ans2)
        # Compare the actual result with the expected DataFrame
        assert_frame_equal(ans2, expected_ans2_df)


    def test_result_3(self):
        # actual result 3
        ans3 = max_min_average(NB,"Battery Cost","NB")
        ans3["NB"] = ans3["NB"].astype(float)
        # Define the result_3
        expected_ans3 = {'Battery Cost': ['Max', 'Min', 'Average'],
                            'NB': [1506.00, 1136.00, 1291.00]}
        expected_ans3_df = pd.DataFrame(expected_ans3)
        # Compare the actual result with the expected DataFrame
        assert_frame_equal(ans3, expected_ans3_df)        

if __name__ == '__main__':
    unittest.main()


