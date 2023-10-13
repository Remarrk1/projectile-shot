import unittest
import tkinter as tk
from projectilshot.gui import create_interface


class TestGUIElements(unittest.TestCase):
    """
    Эти тесты предназначены для проверки корректности взаимодействия
    с элементами графического интерфейса, предоставляемыми модулем gui. В частности, они проверяют:

    test_entry_speed: Правильность ввода данных в поле скорости.

    test_entry_angle: Правильность ввода данных в поле угла.
    """

    def setUp(self):
        self.root = tk.Tk()
        self.canvas, self.entry_speed, self.entry_angle = create_interface(self.root, None)

    def test_entry_speed(self):
        # Проверка ввода данных в поле скорости
        expected_text = "50"  # Ожидаемый текст в поле
        self.entry_speed.insert(0, expected_text)  # Вставляем текст в поле
        actual_text = self.entry_speed.get()  # Получаем текущий текст
        self.assertEqual(actual_text, expected_text)

    def test_entry_angle(self):
        # Проверка ввода данных в поле угла
        expected_text = "45"  # Ожидаемый текст в поле
        self.entry_angle.insert(0, expected_text)  # Вставляем текст в поле
        actual_text = self.entry_angle.get()  # Получаем текущий текст
        self.assertEqual(actual_text, expected_text)

    def tearDown(self):
        self.root.destroy()

if __name__ == '__main__':
    unittest.main()
