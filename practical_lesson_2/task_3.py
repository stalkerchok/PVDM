# coding=utf-8
import unittest
from practical_lesson_1 import task_1, task_2, task_3


class TestTasks(unittest.TestCase):
    # --------------------
    # Реализовать юнит-тесты с использованием пакета unittest для задач первой лекции (1,2,3).
    # --------------------
    def test_task_1(self):
        input_array = [4, 156, 65, 77, 90, 986, 537, 3423, 11, 237, 1234, 523, 3456]
        output_array = [4, 156, 90, 986]
        self.assertEqual(output_array, task_1.get_even_before_237(input_array))
        input_array = [4, 156, 65, 77, 90, 986, 537, 3423, 11, 1234, 523, 3456]
        output_array = [4, 156, 90, 986, 1234, 3456]
        self.assertEqual(output_array, task_1.get_even_before_237(input_array))
        input_array = []
        output_array = []
        self.assertEqual(output_array, task_1.get_even_before_237(input_array))

    def test_task_2(self):
        input_string = 'One Two'
        output_string = 'Two One'
        self.assertEqual(output_string, task_2.swap_two_words(input_string))
        input_string = 'One Two Three'
        output_string = 'Two Three One'
        self.assertEqual(output_string, task_2.swap_two_words(input_string))

    def test_task_3(self):
        sequence = [1, 2, 3, 4, 5, 6, 7, 8]
        self.assertTrue(task_3.is_unique_sequence(sequence))
        sequence = [1, 2, 3, 4, 5, 6, 7, 8, 8]
        self.assertFalse(task_3.is_unique_sequence(sequence))
        sequence = []
        self.assertTrue(task_3.is_unique_sequence(sequence))


if __name__ == '__main__':
    unittest.main()
