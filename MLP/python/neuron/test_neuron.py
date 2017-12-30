import unittest
import neuron

NUMBER_INPUTS = 2

class MyTestCase(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(MyTestCase, self).__init__(*args, **kwargs)
        self.n = neuron.Neuron(NUMBER_INPUTS)

    def test_number_inputs(self):
        self.assertEqual(NUMBER_INPUTS + 1, len(self.n.weights))

    def test_something(self):
        print(self.n.weights)
        self.assertEqual(True, True)

    def test_wight_initialize(self):
        for i in self.n.weights:
            self.assertIsNotNone(i)

    def test_calculate_output(self):
        expectedResult = 0.982
        self.n.inputs = [1., 0.]
        self.n.weights = [1., 3., 4.]

        self.assertAlmostEqual(expectedResult, self.n.getOutput(), 3)


if __name__ == '__main__':
    unittest.main()
