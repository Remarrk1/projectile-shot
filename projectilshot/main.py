import tkinter as tk
import physics  # Импортируем модуль physics для физических вычислений
import gui  # Импортируем модуль gui для создания пользовательского интерфейса

animation_interval = 50  # Интервал обновления анимации (в миллисекундах)

def update_animation(canvas, projectile):
    """
    Обновляет анимацию движения снаряда на холсте.

    Args:
        canvas (tk.Canvas): Холст для отображения анимации.
        projectile (int): Идентификатор снаряда на холсте.
    """
    speed_str = entry_speed.get()  # Получаем введенное пользователем значение скорости
    angle_str = entry_angle.get()  # Получаем введенное пользователем значение угла

    if speed_str and angle_str:
        # Если значения скорости и угла доступны:

        # Рассчитываем горизонтальную (Vx) и вертикальную (Vy) составляющие скорости.
        Vx, Vy = physics.calculate_velocity(float(speed_str), float(angle_str))

        # Рассчитываем новые координаты снаряда на холсте.
        x, y = physics.calculate_coordinates(Vx, Vy)

        # Обновляем положение снаряда на холсте.
        canvas.coords(projectile, x - 5, 400 - y - 5, x + 5, 400 - y + 5)

        # Запускаем обновление анимации через определенный интервал времени.
        root.after(animation_interval, lambda: update_animation(canvas, projectile))

def shoot():
    """
    Обработчик события "Выстрел" - запускает анимацию движения снаряда.
    """
    update_animation(canvas, projectile)  # Запускаем анимацию

root = tk.Tk()  # Создаем главное окно приложения с использованием библиотеки tkinter

# Создаем интерфейс и получаем элементы
canvas, entry_speed, entry_angle = gui.create_interface(root, shoot)

# Создаем объект снаряда на холсте
projectile = canvas.create_oval(-5, -5, 5, 5, fill="red")

root.mainloop()
