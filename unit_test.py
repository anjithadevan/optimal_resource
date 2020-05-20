import unittest
import lowest_resource


class TestGetOptimalResourceMethod(unittest.TestCase):
    def test_resource_output(self):
        lowest_resource_value = lowest_resource.get_optimal_resource("Capacity of 1150 units for 1 Hour")
        required_resource_value = [{'total_cost': '$10150', 'region': 'New York', 'machines': [('8XLarge', 7), ('XLarge', 1), ('Large', 1)]}, {'total_cost': '$9520', 'region': 'India', 'machines': [('8XLarge', 7), ('Large', 3)]}, {'total_cost': '$8570', 'region': 'China', 'machines': [('8XLarge', 7), ('XLarge', 1), ('Large', 1)]}]
        self.assertEqual(lowest_resource_value['Output'], required_resource_value)


if __name__ == '__main__':
    unittest.main()