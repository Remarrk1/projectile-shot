import unittest
from projectilshot import physics


class TestPhysicsFunctions(unittest.TestCase):

    def test_calculate_velocity(self):
        # Тест функции calculate_velocity

        """Тест проверяет функцию calculate_velocity из модуля physics. Конкретно, он проверяет,
        что функция корректно вычисляет горизонтальную (Vx) и вертикальную (Vy) компоненты скорости
        для заданных начальной скорости и градусов."""

        Vx, Vy = physics.calculate_velocity(30, 45)
        self.assertAlmostEqual(Vx, 21.21, places=2)
        self.assertAlmostEqual(Vy, 21.21, places=2)

    def test_calculate_coordinates(self):
        # Тест функции calculate_coordinates

        """Тест предназначен для проверки корректности работы функции calculate_coordinates из модуля physics.
        Эта функция используется для расчета координат снаряда в зависимости от начальной скорости, угла и ускорения свободного падения."""
        x, y = physics.calculate_coordinates(21.21, 21.21)
        self.assertAlmostEqual(x, 12.12, places=2)
        self.assertAlmostEqual(y, 12.07, places=2)

if __name__ == '__main__':
    unittest.main()
