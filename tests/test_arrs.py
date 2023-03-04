import unittest
from utils import arrs


class TestArrs(unittest.TestCase):
    def test_get_normal(self):
        self.assertEqual(arrs.get(['Нулевой', 'Первый', 'Второй', 'Третий', 'Четвертый', 'Пятый'], 2), 'Второй')

    def test_get_negative(self):
        self.assertEqual(arrs.get(['Нулевой', 'Первый', 'Второй', 'Третий', 'Четвертый', 'Пятый'], -3), None)

    def test_my_slice_normal(self):
        self.assertEqual(arrs.my_slice(['Нулевой', 'Первый', 'Второй', 'Третий', 'Четвертый', 'Пятый'], 2),
                         ['Второй', 'Третий', 'Четвертый', 'Пятый'])

    def test_my_slice_negative(self):
        self.assertEqual(arrs.my_slice(['Нулевой', 'Первый', 'Второй', 'Третий', 'Четвертый', 'Пятый'], -2),
                         ['Четвертый', 'Пятый'])

    def test_my_slice_negative_over_len(self):
        self.assertEqual(arrs.my_slice(['Нулевой', 'Первый', 'Второй', 'Третий', 'Четвертый', 'Пятый'], -10),
                         ['Нулевой', 'Первый', 'Второй', 'Третий', 'Четвертый', 'Пятый'])

    def test_my_slice_empty(self):
        self.assertEqual(arrs.my_slice([], 2), [])
