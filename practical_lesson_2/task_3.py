import unittest
import task_1, task_2


class TestTasks(unittest.TestCase):
    def test_task_1(self):
        sequence = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
        self.assertEqual(sequence, task_1.get_fibonacci_sequence(10))

    def test_task_2(self):
        minimums = -50.0, 2.3379320168714912e-07
        self.assertEqual(minimums, task_2.minimums_of_functions(1, 50))


if __name__ == '__main__':
    unittest.main()
